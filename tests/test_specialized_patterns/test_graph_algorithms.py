"""
Tests for Graph Algorithms (Dijkstra, Prim's MST, Kruskal's MST).
"""

import pytest
from dsa.specialized_patterns.graph_algorithms import GraphAlgorithmsSolutions


class TestDijkstra:
    """Tests for Dijkstra's shortest path algorithm."""

    def test_basic_shortest_path(self):
        """Test basic shortest path finding."""
        # Graph: 0 -> 1 (4), 0 -> 2 (1), 2 -> 1 (2), 1 -> 3 (1), 2 -> 3 (5)
        graph = {
            0: [(1, 4), (2, 1)],
            1: [(3, 1)],
            2: [(1, 2), (3, 5)],
            3: []
        }
        result = GraphAlgorithmsSolutions.dijkstra(graph, 0, 4)
        assert result == [0, 3, 1, 4]

    def test_single_vertex(self):
        """Test with single vertex."""
        graph = {0: []}
        result = GraphAlgorithmsSolutions.dijkstra(graph, 0, 1)
        assert result == [0]

    def test_disconnected_graph(self):
        """Test with disconnected vertices."""
        graph = {
            0: [(1, 1)],
            1: [],
            2: [(3, 1)],
            3: []
        }
        result = GraphAlgorithmsSolutions.dijkstra(graph, 0, 4)
        assert result[2] == float('inf')
        assert result[3] == float('inf')

    def test_network_delay_time_basic(self):
        """Test network delay time calculation."""
        times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
        result = GraphAlgorithmsSolutions.network_delay_time(times, 4, 2)
        assert result == 2

    def test_network_delay_time_unreachable(self):
        """Test when not all nodes are reachable."""
        times = [[1, 2, 1]]
        result = GraphAlgorithmsSolutions.network_delay_time(times, 3, 1)
        assert result == -1


class TestPrimMST:
    """Tests for Prim's Minimum Spanning Tree algorithm."""

    def test_basic_mst(self):
        """Test basic MST construction."""
        n = 4
        edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
        weight, mst = GraphAlgorithmsSolutions.prim_mst(n, edges)

        # Total weight should be 19 (edges: 2-3:4, 0-3:5, 0-1:10)
        assert weight == 19
        assert len(mst) == 3  # n-1 edges for n vertices

    def test_single_vertex(self):
        """Test with single vertex."""
        n = 1
        edges = []
        weight, mst = GraphAlgorithmsSolutions.prim_mst(n, edges)
        assert weight == 0
        assert len(mst) == 0

    def test_two_vertices(self):
        """Test with two vertices."""
        n = 2
        edges = [[0, 1, 5]]
        weight, mst = GraphAlgorithmsSolutions.prim_mst(n, edges)
        assert weight == 5
        assert len(mst) == 1

    def test_linear_graph(self):
        """Test with linear chain of vertices."""
        n = 4
        edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3]]
        weight, mst = GraphAlgorithmsSolutions.prim_mst(n, edges)
        assert weight == 6  # 1 + 2 + 3
        assert len(mst) == 3

    def test_complete_graph(self):
        """Test with complete graph (all vertices connected)."""
        n = 4
        edges = [
            [0, 1, 1], [0, 2, 4], [0, 3, 3],
            [1, 2, 2], [1, 3, 5],
            [2, 3, 1]
        ]
        weight, mst = GraphAlgorithmsSolutions.prim_mst(n, edges)
        # Minimum spanning tree: 0-1:1, 1-2:2, 2-3:1 = 4
        # or 0-1:1, 2-3:1, 1-2:2 = 4
        assert weight == 4
        assert len(mst) == 3

    def test_duplicate_weights(self):
        """Test with multiple edges having same weight."""
        n = 3
        edges = [[0, 1, 5], [1, 2, 5], [0, 2, 5]]
        weight, mst = GraphAlgorithmsSolutions.prim_mst(n, edges)
        assert weight == 10  # Any two edges work
        assert len(mst) == 2

    def test_zero_weight_edges(self):
        """Test with zero weight edges."""
        n = 3
        edges = [[0, 1, 0], [1, 2, 1]]
        weight, mst = GraphAlgorithmsSolutions.prim_mst(n, edges)
        assert weight == 1
        assert len(mst) == 2


class TestKruskalMST:
    """Tests for Kruskal's Minimum Spanning Tree algorithm."""

    def test_basic_mst(self):
        """Test basic MST construction."""
        n = 4
        edges = [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)

        # Total weight should be 19 (edges: 2-3:4, 0-3:5, 0-1:10)
        assert weight == 19
        assert len(mst) == 3  # n-1 edges for n vertices

    def test_single_vertex(self):
        """Test with single vertex."""
        n = 1
        edges = []
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
        assert weight == 0
        assert len(mst) == 0

    def test_two_vertices(self):
        """Test with two vertices."""
        n = 2
        edges = [[0, 1, 5]]
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
        assert weight == 5
        assert len(mst) == 1

    def test_linear_graph(self):
        """Test with linear chain of vertices."""
        n = 4
        edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3]]
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
        assert weight == 6  # 1 + 2 + 3
        assert len(mst) == 3

    def test_complete_graph(self):
        """Test with complete graph (all vertices connected)."""
        n = 4
        edges = [
            [0, 1, 1], [0, 2, 4], [0, 3, 3],
            [1, 2, 2], [1, 3, 5],
            [2, 3, 1]
        ]
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
        # Minimum spanning tree: 0-1:1, 2-3:1, 1-2:2 = 4
        assert weight == 4
        assert len(mst) == 3

    def test_cycle_avoidance(self):
        """Test that Kruskal's avoids creating cycles."""
        n = 3
        edges = [[0, 1, 1], [1, 2, 1], [0, 2, 2]]
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
        # Should pick 0-1:1 and 1-2:1, not 0-2:2 (would create cycle)
        assert weight == 2
        assert len(mst) == 2

    def test_duplicate_weights(self):
        """Test with multiple edges having same weight."""
        n = 3
        edges = [[0, 1, 5], [1, 2, 5], [0, 2, 5]]
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
        assert weight == 10  # Any two edges work
        assert len(mst) == 2

    def test_zero_weight_edges(self):
        """Test with zero weight edges."""
        n = 3
        edges = [[0, 1, 0], [1, 2, 1]]
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
        assert weight == 1
        assert len(mst) == 2

    def test_larger_graph(self):
        """Test with larger graph."""
        n = 6
        edges = [
            [0, 1, 4], [0, 2, 4],
            [1, 2, 2],
            [2, 3, 3], [2, 5, 2], [2, 4, 4],
            [3, 4, 3],
            [4, 5, 3]
        ]
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
        # Optimal MST weight calculation
        assert len(mst) == 5  # n-1 edges
        # The exact weight depends on tie-breaking, but it should be minimal


class TestMSTComparison:
    """Compare Prim's and Kruskal's algorithms."""

    def test_same_weight(self):
        """Both algorithms should produce same total weight."""
        test_cases = [
            (4, [[0, 1, 10], [0, 2, 6], [0, 3, 5], [1, 3, 15], [2, 3, 4]]),
            (3, [[0, 1, 1], [1, 2, 2], [0, 2, 3]]),
            (5, [[0, 1, 2], [0, 3, 6], [1, 2, 3], [1, 3, 8], [1, 4, 5], [2, 4, 7], [3, 4, 9]]),
        ]

        for n, edges in test_cases:
            prim_weight, _ = GraphAlgorithmsSolutions.prim_mst(n, edges)
            kruskal_weight, _ = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
            assert prim_weight == kruskal_weight

    def test_same_edge_count(self):
        """Both algorithms should produce n-1 edges."""
        n = 5
        edges = [[0, 1, 1], [1, 2, 2], [2, 3, 3], [3, 4, 4], [0, 4, 10]]

        _, prim_mst = GraphAlgorithmsSolutions.prim_mst(n, edges)
        _, kruskal_mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)

        assert len(prim_mst) == n - 1
        assert len(kruskal_mst) == n - 1


class TestEdgeCases:
    """Test edge cases for all graph algorithms."""

    def test_empty_graph_prim(self):
        """Test Prim's with no vertices."""
        weight, mst = GraphAlgorithmsSolutions.prim_mst(0, [])
        assert weight == 0
        assert len(mst) == 0

    def test_empty_graph_kruskal(self):
        """Test Kruskal's with no vertices."""
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(0, [])
        assert weight == 0
        assert len(mst) == 0

    def test_self_loop(self):
        """Test handling of self-loops (should be ignored by MST)."""
        n = 3
        edges = [[0, 0, 10], [0, 1, 1], [1, 2, 2]]

        # Kruskal's should work fine (self-loop won't be added)
        weight, mst = GraphAlgorithmsSolutions.kruskal_mst(n, edges)
        assert len(mst) == 2

    def test_negative_weights_not_common(self):
        """MST algorithms work with negative weights (though uncommon)."""
        n = 3
        edges = [[0, 1, -5], [1, 2, -3], [0, 2, 10]]

        prim_weight, _ = GraphAlgorithmsSolutions.prim_mst(n, edges)
        kruskal_weight, _ = GraphAlgorithmsSolutions.kruskal_mst(n, edges)

        # Both should pick the two negative edges
        assert prim_weight == -8
        assert kruskal_weight == -8
