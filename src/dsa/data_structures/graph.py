"""
Graph Data Structure

Graph representations and common graph utilities.
"""

from typing import List, Dict, Set, Optional
from collections import defaultdict, deque


class Graph:
    """Graph implementation using adjacency list."""

    def __init__(self, directed: bool = False):
        self.graph: Dict[int, List[int]] = defaultdict(list)
        self.directed = directed

    def add_edge(self, u: int, v: int) -> None:
        """Add an edge from u to v."""
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def add_vertex(self, v: int) -> None:
        """Add a vertex to the graph."""
        if v not in self.graph:
            self.graph[v] = []

    def get_vertices(self) -> List[int]:
        """Get all vertices in the graph."""
        return list(self.graph.keys())

    def get_neighbors(self, v: int) -> List[int]:
        """Get all neighbors of a vertex."""
        return self.graph.get(v, [])

    def has_edge(self, u: int, v: int) -> bool:
        """Check if there's an edge from u to v."""
        return v in self.graph.get(u, [])

    def __repr__(self) -> str:
        return f"Graph({dict(self.graph)})"


class WeightedGraph:
    """Weighted graph implementation using adjacency list."""

    def __init__(self, directed: bool = False):
        self.graph: Dict[int, List[tuple]] = defaultdict(list)
        self.directed = directed

    def add_edge(self, u: int, v: int, weight: int) -> None:
        """Add a weighted edge from u to v."""
        self.graph[u].append((v, weight))
        if not self.directed:
            self.graph[v].append((u, weight))

    def get_neighbors(self, v: int) -> List[tuple]:
        """Get all neighbors of a vertex with weights."""
        return self.graph.get(v, [])

    def __repr__(self) -> str:
        return f"WeightedGraph({dict(self.graph)})"


class GraphMatrix:
    """Graph implementation using adjacency matrix."""

    def __init__(self, num_vertices: int, directed: bool = False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u: int, v: int, weight: int = 1) -> None:
        """Add an edge from u to v with optional weight."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            self.matrix[u][v] = weight
            if not self.directed:
                self.matrix[v][u] = weight

    def has_edge(self, u: int, v: int) -> bool:
        """Check if there's an edge from u to v."""
        if 0 <= u < self.num_vertices and 0 <= v < self.num_vertices:
            return self.matrix[u][v] != 0
        return False

    def get_neighbors(self, v: int) -> List[int]:
        """Get all neighbors of a vertex."""
        if 0 <= v < self.num_vertices:
            return [i for i in range(self.num_vertices) if self.matrix[v][i] != 0]
        return []

    def __repr__(self) -> str:
        return f"GraphMatrix({self.matrix})"
