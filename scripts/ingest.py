import argparse
import csv
import os
import sys
import time
from typing import Any, Dict, Iterable, Iterator, List, Optional, Tuple


def _load_dotenv_if_available() -> None:
    try:
        from dotenv import load_dotenv  # type: ignore
    except Exception:
        return
    load_dotenv()


def _require(name: str) -> str:
    v = os.getenv(name)
    if not v:
        raise RuntimeError("Missing required environment variable: %s" % name)
    return v


def _open_csv_with_guess(path: str) -> Tuple[Any, str]:
    # The dataset is "unknown-8bit" per `file`; cp1252 typically preserves curly quotes.
    encodings = ["utf-8-sig", "utf-8", "cp1252", "latin-1"]
    for enc in encodings:
        try:
            f = open(path, "r", encoding=enc, newline="")
            f.read(4096)
            f.seek(0)
            return f, enc
        except UnicodeDecodeError:
            continue
    f = open(path, "r", encoding="utf-8", errors="replace", newline="")
    return f, "utf-8(replace)"


def iter_records(csv_path: str, *, embed_field: str) -> Iterator[Dict[str, Any]]:
    f, enc = _open_csv_with_guess(csv_path)
    with f:
        reader = csv.DictReader(f)
        row_id = 0
        for row in reader:
            row_id += 1
            speech = (row.get("speech") or "").strip()
            if not speech:
                continue
            speaker = (row.get("speaker") or "").strip()
            chunk_text = ("%s: %s" % (speaker, speech)).strip() if speaker else speech

            rec: Dict[str, Any] = {
                "_id": "row-%d" % row_id,
                embed_field: chunk_text,
                "speech": speech,
                "speaker": speaker,
                "date": (row.get("date") or "").strip(),
                "debate_name": (row.get("debate_name") or "").strip(),
                "debate_section": (row.get("debate_section") or "").strip(),
                "source_file": os.path.basename(csv_path),
            }

            sts = (row.get("speaking_time_seconds") or "").strip()
            if sts:
                try:
                    rec["speaking_time_seconds"] = float(sts)
                except Exception:
                    rec["speaking_time_seconds"] = sts
            yield rec


def batched(it: Iterable[Dict[str, Any]], batch_size: int) -> Iterator[List[Dict[str, Any]]]:
    buf: List[Dict[str, Any]] = []
    for x in it:
        buf.append(x)
        if len(buf) >= batch_size:
            yield buf
            buf = []
    if buf:
        yield buf


def _is_index_ready(desc: Any) -> bool:
    # Pinecone returns either a dict or a model; normalize.
    status = None
    if isinstance(desc, dict):
        status = desc.get("status")
    else:
        status = getattr(desc, "status", None)
    if isinstance(status, dict):
        ready = status.get("ready")
        return bool(ready)
    if status is None:
        return True
    return bool(getattr(status, "ready", True))


def ensure_index(
    pc: Any,
    *,
    index_name: str,
    cloud: str,
    region: str,
    embed_model: str,
    embed_field: str,
) -> None:
    exists = False
    if hasattr(pc, "has_index"):
        exists = bool(pc.has_index(index_name))
    else:
        try:
            names = [x.get("name") for x in pc.list_indexes()]  # type: ignore[attr-defined]
            exists = index_name in names
        except Exception:
            exists = False

    if exists:
        return

    if not hasattr(pc, "create_index_for_model"):
        raise RuntimeError(
            "Your Pinecone Python SDK is missing create_index_for_model(). "
            "Upgrade the `pinecone` package to a recent version."
        )

    print("Creating Pinecone index %r (model=%s)..." % (index_name, embed_model))
    pc.create_index_for_model(
        name=index_name,
        cloud=cloud,
        region=region,
        embed={"model": embed_model, "field_map": {"text": embed_field}},
    )

    # Wait until ready (best-effort).
    for _ in range(90):
        try:
            desc = pc.describe_index(index_name)
            if _is_index_ready(desc):
                print("Index is ready.")
                return
        except Exception:
            pass
        time.sleep(2)
    print("Timed out waiting for index readiness; continuing anyway.")


def main(argv: Optional[List[str]] = None) -> int:
    _load_dotenv_if_available()

    parser = argparse.ArgumentParser(description="Ingest debate transcripts CSV into Pinecone (integrated embeddings).")
    parser.add_argument(
        "--csv",
        default="debate_transcripts_v3_2020-02-26.csv",
        help="Path to the transcripts CSV (default: %(default)s)",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=96,
        help="Records per upsert batch (default: %(default)s). Pinecone records upsert max is 96.",
    )
    parser.add_argument(
        "--skip-create-index",
        action="store_true",
        help="Do not create the index automatically if missing.",
    )
    args = parser.parse_args(argv)
    if args.batch_size > 96:
        print("Requested --batch-size %d exceeds Pinecone max (96). Using 96." % args.batch_size)
        args.batch_size = 96

    pinecone_api_key = _require("PINECONE_API_KEY")
    index_name = os.getenv("PINECONE_INDEX_NAME", "dem-debates-transcripts")
    namespace = os.getenv("PINECONE_NAMESPACE", "debates")
    cloud = os.getenv("PINECONE_CLOUD", "aws")
    region = os.getenv("PINECONE_REGION", "us-east-1")
    index_host = os.getenv("PINECONE_INDEX_HOST") or None
    embed_model = os.getenv("PINECONE_EMBED_MODEL", "multilingual-e5-large")
    embed_field = os.getenv("PINECONE_EMBED_FIELD", "chunk_text")

    from pinecone import Pinecone  # type: ignore

    pc = Pinecone(api_key=pinecone_api_key)
    if not args.skip_create_index:
        ensure_index(
            pc,
            index_name=index_name,
            cloud=cloud,
            region=region,
            embed_model=embed_model,
            embed_field=embed_field,
        )

    if index_host:
        index = pc.Index(host=index_host)
    else:
        index = pc.Index(index_name)

    if not hasattr(index, "upsert_records"):
        raise RuntimeError(
            "Your Pinecone Index object is missing upsert_records(). "
            "Install/upgrade `pinecone` and `pinecone-plugin-records`."
        )

    total = 0
    t0 = time.time()
    for batch in batched(iter_records(args.csv, embed_field=embed_field), args.batch_size):
        try:
            index.upsert_records(namespace=namespace, records=batch)
        except TypeError:
            index.upsert_records(namespace, batch)
        total += len(batch)
        if total % (args.batch_size * 10) == 0:
            dt = max(0.001, time.time() - t0)
            print("Upserted %d records (%.1f rec/s)" % (total, total / dt))

    dt = max(0.001, time.time() - t0)
    print("Done. Upserted %d records into namespace %r (%.1f rec/s)." % (total, namespace, total / dt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
