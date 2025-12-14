"""
Union-Find (Disjoint Set Union) Pattern

Pattern: Track connected components in graph.
When to use:
- Detecting cycles in undirected graphs
- Network connectivity
- Kruskal's MST algorithm
- Number of connected components

Time Complexity: O(α(n)) ≈ O(1) with path compression
Space Complexity: O(n)
"""

from typing import List


class UnionFind:
    """Union-Find data structure with path compression and union by rank."""

    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.components = size

    def find(self, x: int) -> int:
        """Find root with path compression."""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int) -> bool:
        """Union by rank. Returns True if union performed."""
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

        self.components -= 1
        return True

    def connected(self, x: int, y: int) -> bool:
        """Check if two elements are connected."""
        return self.find(x) == self.find(y)


class UnionFindSolutions:
    """Solutions using the union-find pattern."""

    @staticmethod
    def count_components(n: int, edges: List[List[int]]) -> int:
        """
        Count connected components in undirected graph.

        Time Complexity: O(E * α(n))
        Space Complexity: O(n)
        """
        uf = UnionFind(n)

        for u, v in edges:
            uf.union(u, v)

        return uf.components

    @staticmethod
    def has_cycle(n: int, edges: List[List[int]]) -> bool:
        """
        Detect cycle in undirected graph.

        Time Complexity: O(E * α(n))
        Space Complexity: O(n)
        """
        uf = UnionFind(n)

        for u, v in edges:
            if not uf.union(u, v):
                return True

        return False
