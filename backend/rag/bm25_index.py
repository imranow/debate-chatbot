import csv
import heapq
import os
import pickle
import re
from dataclasses import dataclass, field
from typing import Any, Dict, Iterator, List, Optional, Tuple

from backend.rag.retrieval import RetrievedChunk


def _tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", text.lower())


def _open_csv_with_guess(path: str) -> Tuple[Any, str]:
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


@dataclass
class BM25Document:
    id: str
    tokens: List[str]
    fields: Dict[str, Any]


class BM25Index:

    def __init__(self, documents: List[BM25Document]):
        from rank_bm25 import BM25Okapi  # type: ignore

        self._documents = documents
        self._id_to_idx = {d.id: i for i, d in enumerate(documents)}
        corpus = [d.tokens for d in documents]
        self._bm25 = BM25Okapi(corpus)

    @classmethod
    def from_csv(cls, csv_path: str, embed_field: str = "chunk_text") -> "BM25Index":
        documents: List[BM25Document] = []
        f, _enc = _open_csv_with_guess(csv_path)
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

                fields: Dict[str, Any] = {
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
                        fields["speaking_time_seconds"] = float(sts)
                    except Exception:
                        fields["speaking_time_seconds"] = sts

                documents.append(BM25Document(
                    id="row-%d" % row_id,
                    tokens=_tokenize(chunk_text),
                    fields=fields,
                ))
        return cls(documents)

    @classmethod
    def load(cls, pickle_path: str) -> "BM25Index":
        with open(pickle_path, "rb") as f:
            return pickle.load(f)

    def save(self, pickle_path: str) -> None:
        os.makedirs(os.path.dirname(pickle_path) or ".", exist_ok=True)
        with open(pickle_path, "wb") as f:
            pickle.dump(self, f)

    def search(self, query: str, top_k: int = 20) -> List[RetrievedChunk]:
        tokens = _tokenize(query)
        if not tokens:
            return []
        scores = self._bm25.get_scores(tokens)
        max_score = max(scores) if len(scores) > 0 else 1.0
        if max_score <= 0:
            return []

        # O(n log k) heap selection — faster than O(n log n) full sort for small top_k
        top_indices = heapq.nlargest(top_k, range(len(scores)), key=lambda i: scores[i])

        results: List[RetrievedChunk] = []
        for idx in top_indices:
            if scores[idx] <= 0:
                break
            doc = self._documents[idx]
            results.append(RetrievedChunk(
                id=doc.id,
                score=scores[idx] / max_score,  # normalize to [0, 1]
                fields=dict(doc.fields),
            ))
        return results

    def get_document_by_id(self, doc_id: str) -> Optional[BM25Document]:
        idx = self._id_to_idx.get(doc_id)
        if idx is None:
            return None
        return self._documents[idx]

    @property
    def num_documents(self) -> int:
        return len(self._documents)
