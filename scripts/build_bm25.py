import argparse
import os
import sys
import time
from typing import List, Optional


def main(argv: Optional[List[str]] = None) -> int:
    try:
        from dotenv import load_dotenv  # type: ignore
        load_dotenv(override=True)
    except Exception:
        pass

    parser = argparse.ArgumentParser(description="Build BM25 index from debate CSV.")
    parser.add_argument(
        "--csv",
        default="debate_transcripts_v3_2020-02-26.csv",
        help="Path to the transcripts CSV (default: %(default)s)",
    )
    parser.add_argument(
        "--output",
        default="data/bm25_index.pkl",
        help="Output pickle path (default: %(default)s)",
    )
    args = parser.parse_args(argv)

    if not os.path.exists(args.csv):
        print("CSV not found: %s" % args.csv)
        return 1

    # Add project root to path so backend imports work
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    from backend.rag.bm25_index import BM25Index

    print("Building BM25 index from %s..." % args.csv)
    t0 = time.time()
    index = BM25Index.from_csv(args.csv)
    dt = time.time() - t0
    print("Built index with %d documents in %.1fs" % (index.num_documents, dt))

    index.save(args.output)
    size_kb = os.path.getsize(args.output) / 1024
    print("Saved to %s (%.0f KB)" % (args.output, size_kb))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
