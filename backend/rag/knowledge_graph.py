import json
import os
import re
from collections import defaultdict
from typing import Any, Dict, List, Optional, Set, Tuple

import networkx as nx  # type: ignore


class KnowledgeGraph:

    def __init__(self, graph: nx.DiGraph):
        self.graph = graph
        # Build lowercase name -> node id index
        self._name_index: Dict[str, str] = {}
        for node_id, data in graph.nodes(data=True):
            name = data.get("name", node_id)
            self._name_index[name.lower().strip()] = node_id

    @classmethod
    def load(cls, json_path: str) -> "KnowledgeGraph":
        with open(json_path, "r") as f:
            data = json.load(f)
        graph = nx.node_link_graph(data)
        return cls(graph)

    def save(self, json_path: str) -> None:
        os.makedirs(os.path.dirname(json_path) or ".", exist_ok=True)
        data = nx.node_link_data(self.graph)
        with open(json_path, "w") as f:
            json.dump(data, f, indent=2)

    def find_entities(self, query: str) -> List[str]:
        """Find graph node IDs that match tokens in the query."""
        query_lower = query.lower()
        matched: List[Tuple[str, int]] = []

        for name, node_id in self._name_index.items():
            # Match if the entity name appears as a substring in the query
            if len(name) >= 3 and name in query_lower:
                matched.append((node_id, len(name)))

        # Sort by match length (prefer longer/more specific matches)
        matched.sort(key=lambda x: x[1], reverse=True)
        return [node_id for node_id, _ in matched]

    def _row_ids_from_entities(
        self,
        entity_ids: List[str],
        max_results: int,
    ) -> List[str]:
        """1-hop traversal from pre-computed entity IDs to source row IDs."""
        row_ids: List[str] = []
        seen: Set[str] = set()

        for entity_id in entity_ids[:5]:  # limit to top 5 matched entities
            for _src, _dst, edge_data in self.graph.edges(entity_id, data=True):
                for rid in edge_data.get("source_row_ids", []):
                    if rid not in seen:
                        seen.add(rid)
                        row_ids.append(rid)
            for _src, _dst, edge_data in self.graph.in_edges(entity_id, data=True):
                for rid in edge_data.get("source_row_ids", []):
                    if rid not in seen:
                        seen.add(rid)
                        row_ids.append(rid)
            if len(row_ids) >= max_results:
                break

        return row_ids[:max_results]

    def _context_from_entities(self, entity_ids: List[str]) -> Optional[str]:
        """Format graph context text from pre-computed entity IDs."""
        lines: List[str] = []
        for entity_id in entity_ids[:3]:
            node_data = self.graph.nodes.get(entity_id, {})
            entity_name = node_data.get("name", entity_id)
            entity_type = node_data.get("type", "entity")

            relations: Dict[str, List[str]] = defaultdict(list)
            for _src, dst, edge_data in self.graph.edges(entity_id, data=True):
                rel_type = edge_data.get("type", "related_to")
                dst_name = self.graph.nodes.get(dst, {}).get("name", dst)
                relations[rel_type].append(dst_name)
            for src, _dst, edge_data in self.graph.in_edges(entity_id, data=True):
                rel_type = edge_data.get("type", "related_to")
                src_name = self.graph.nodes.get(src, {}).get("name", src)
                relations[rel_type + "_by"].append(src_name)

            if not relations:
                continue

            parts = []
            for rel_type, targets in relations.items():
                parts.append("%s: %s" % (rel_type, ", ".join(targets[:4])))

            lines.append("%s (%s) - %s" % (entity_name, entity_type, "; ".join(parts)))

        return "\n".join(lines) if lines else None

    def get_context_and_row_ids(
        self,
        query: str,
        max_results: int = 3,
    ) -> Tuple[Optional[str], List[str]]:
        """Compute entity matches once, return both graph context and row IDs.

        Use this instead of calling format_graph_context + get_enrichment_row_ids
        separately to avoid the double find_entities scan.
        """
        entity_ids = self.find_entities(query)
        if not entity_ids:
            return None, []
        context = self._context_from_entities(entity_ids)
        row_ids = self._row_ids_from_entities(entity_ids, max_results)
        return context, row_ids

    # --- Convenience single-purpose methods (delegate to shared helpers) ---

    def get_enrichment_row_ids(self, query: str, max_results: int = 3) -> List[str]:
        """Find source row IDs related to entities in the query via 1-hop traversal."""
        return self._row_ids_from_entities(self.find_entities(query), max_results)

    def format_graph_context(self, query: str) -> Optional[str]:
        """Return a short summary of entity relationships relevant to the query."""
        return self._context_from_entities(self.find_entities(query))

    @property
    def num_nodes(self) -> int:
        return self.graph.number_of_nodes()

    @property
    def num_edges(self) -> int:
        return self.graph.number_of_edges()
