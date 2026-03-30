"""Unit tests for knowledge graph entity matching and enrichment."""

import networkx as nx

from backend.rag.knowledge_graph import KnowledgeGraph


def _build_test_graph() -> KnowledgeGraph:
    """Build a small graph for testing.

    Nodes: Biden (person), Trump (person), Healthcare (topic), Immigration (topic)
    Edges:
      Biden --discussed--> Healthcare  (source_row_ids: ["row-1", "row-2"])
      Trump --discussed--> Healthcare  (source_row_ids: ["row-3"])
      Biden --discussed--> Immigration (source_row_ids: ["row-4"])
      Trump --discussed--> Immigration (source_row_ids: ["row-5", "row-6"])
    """
    g = nx.DiGraph()
    g.add_node("biden", name="Biden", type="person")
    g.add_node("trump", name="Trump", type="person")
    g.add_node("healthcare", name="Healthcare", type="topic")
    g.add_node("immigration", name="Immigration", type="topic")

    g.add_edge("biden", "healthcare", type="discussed", source_row_ids=["row-1", "row-2"])
    g.add_edge("trump", "healthcare", type="discussed", source_row_ids=["row-3"])
    g.add_edge("biden", "immigration", type="discussed", source_row_ids=["row-4"])
    g.add_edge("trump", "immigration", type="discussed", source_row_ids=["row-5", "row-6"])

    return KnowledgeGraph(g)


class TestEntityMatching:

    def test_finds_entity_by_substring(self):
        kg = _build_test_graph()
        entities = kg.find_entities("What did Biden say about healthcare?")
        entity_ids = set(entities)
        assert "biden" in entity_ids
        assert "healthcare" in entity_ids

    def test_case_insensitive(self):
        kg = _build_test_graph()
        entities = kg.find_entities("BIDEN and TRUMP on immigration")
        entity_ids = set(entities)
        assert "biden" in entity_ids
        assert "trump" in entity_ids
        assert "immigration" in entity_ids

    def test_no_match_for_unknown_entity(self):
        kg = _build_test_graph()
        entities = kg.find_entities("What about climate change?")
        assert entities == []

    def test_short_names_excluded(self):
        """Entity names shorter than 3 chars should not match."""
        g = nx.DiGraph()
        g.add_node("ab", name="ab", type="test")
        kg = KnowledgeGraph(g)
        # "ab" is only 2 chars, should not match
        assert kg.find_entities("ab is here") == []

    def test_longer_matches_ranked_first(self):
        """More specific (longer) entity names should rank higher."""
        g = nx.DiGraph()
        g.add_node("health", name="Health", type="topic")
        g.add_node("healthcare", name="Healthcare", type="topic")
        kg = KnowledgeGraph(g)
        entities = kg.find_entities("Tell me about healthcare policy")
        # "Healthcare" (10 chars) should come before "Health" (6 chars)
        assert entities[0] == "healthcare"


class TestGraphEnrichment:

    def test_1hop_returns_row_ids(self):
        kg = _build_test_graph()
        row_ids = kg.get_enrichment_row_ids("Biden healthcare", max_results=10)
        # Should include row IDs from Biden's edges and Healthcare's edges
        assert "row-1" in row_ids
        assert "row-2" in row_ids

    def test_max_results_limits_output(self):
        kg = _build_test_graph()
        row_ids = kg.get_enrichment_row_ids("Biden healthcare", max_results=2)
        assert len(row_ids) <= 2

    def test_no_entities_returns_empty(self):
        kg = _build_test_graph()
        row_ids = kg.get_enrichment_row_ids("something totally unrelated xyz")
        assert row_ids == []

    def test_traverses_both_directions(self):
        """1-hop should follow both outgoing and incoming edges."""
        kg = _build_test_graph()
        # "Healthcare" has incoming edges from Biden and Trump
        row_ids = kg.get_enrichment_row_ids("healthcare debate", max_results=10)
        # Should include row IDs from edges pointing TO healthcare
        assert "row-1" in row_ids or "row-3" in row_ids

    def test_no_duplicate_row_ids(self):
        kg = _build_test_graph()
        row_ids = kg.get_enrichment_row_ids("Biden Trump healthcare immigration", max_results=20)
        assert len(row_ids) == len(set(row_ids))
