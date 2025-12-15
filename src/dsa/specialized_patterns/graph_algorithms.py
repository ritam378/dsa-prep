"""
Graph Algorithms Pattern

Pattern: Advanced graph algorithms.
When to use:
- Shortest path (Dijkstra, Bellman-Ford)
- Minimum spanning tree (Kruskal, Prim)
- Strongly connected components

Time Complexity: Varies by algorithm
Space Complexity: O(V + E)
"""

from typing import List, Dict, Tuple
import heapq
from collections import defaultdict


class GraphAlgorithmsSolutions:
    """Advanced graph algorithm solutions."""

    @staticmethod
    def dijkstra(graph: Dict[int, List[Tuple[int, int]]], start: int, n: int) -> List[int]:
        """
        Dijkstra's shortest path algorithm.

        Time Complexity: O((V + E) log V)
        Space Complexity: O(V)

        Args:
            graph: Adjacency list with (neighbor, weight) tuples
            start: Starting vertex
            n: Number of vertices

        Returns:
            List of shortest distances from start to each vertex
        """
        distances = [float('inf')] * n
        distances[start] = 0
        pq = [(0, start)]  # (distance, vertex)

        while pq:
            curr_dist, u = heapq.heappop(pq)

            if curr_dist > distances[u]:
                continue

            for v, weight in graph.get(u, []):
                new_dist = curr_dist + weight

                if new_dist < distances[v]:
                    distances[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return distances

    @staticmethod
    def network_delay_time(times: List[List[int]], n: int, k: int) -> int:
        """
        Find minimum time for signal to reach all nodes.

        Time Complexity: O((V + E) log V)
        Space Complexity: O(V + E)
        """
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))

        distances = [float('inf')] * (n + 1)
        distances[k] = 0
        pq = [(0, k)]

        while pq:
            curr_time, node = heapq.heappop(pq)

            if curr_time > distances[node]:
                continue

            for neighbor, time in graph[node]:
                new_time = curr_time + time
                if new_time < distances[neighbor]:
                    distances[neighbor] = new_time
                    heapq.heappush(pq, (new_time, neighbor))

        max_time = max(distances[1:])
        return max_time if max_time != float('inf') else -1

    @staticmethod
    def prim_mst(n: int, edges: List[List[int]]) -> Tuple[int, List[Tuple[int, int, int]]]:
        """
        Prim's algorithm for Minimum Spanning Tree.

        Algorithm:
        1. Start with an arbitrary vertex
        2. Repeatedly add the minimum weight edge that connects a vertex in the MST
           to a vertex outside the MST
        3. Continue until all vertices are included

        Args:
            n: Number of vertices (0 to n-1)
            edges: List of [u, v, weight] representing undirected weighted edges

        Returns:
            Tuple of (total_weight, mst_edges) where mst_edges is list of (u, v, weight)

        Time Complexity: O(E log V) with min heap
        Space Complexity: O(V + E)

        Difficulty: Medium
        Interview Frequency: Medium
        Companies: Google, Facebook, Amazon, Microsoft
        Estimated Time: 30-35 minutes

        Example:
            >>> n = 4
            >>> edges = [[0,1,10], [0,2,6], [0,3,5], [1,3,15], [2,3,4]]
            >>> weight, mst = prim_mst(n, edges)
            >>> weight
            19

        Interview Tips:
        - Greedy algorithm - always pick minimum weight edge
        - Similar to Dijkstra's but builds tree instead of finding paths
        - Works only on connected graphs
        - Produces same total weight as Kruskal's but may have different edges
        - Good for dense graphs (many edges)
        - Can start from any vertex
        """
        if n == 0:
            return 0, []

        # Build adjacency list
        graph = defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        # Track visited vertices
        visited = set()
        mst_edges = []
        total_weight = 0

        # Min heap: (weight, from_vertex, to_vertex)
        # Start from vertex 0
        min_heap = [(0, -1, 0)]  # -1 indicates no parent for starting vertex

        while min_heap and len(visited) < n:
            weight, from_v, to_v = heapq.heappop(min_heap)

            # Skip if vertex already in MST
            if to_v in visited:
                continue

            # Add vertex to MST
            visited.add(to_v)
            if from_v != -1:  # Not the starting vertex
                mst_edges.append((from_v, to_v, weight))
                total_weight += weight

            # Add all edges from new vertex to heap
            for neighbor, edge_weight in graph[to_v]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (edge_weight, to_v, neighbor))

        return total_weight, mst_edges

    @staticmethod
    def kruskal_mst(n: int, edges: List[List[int]]) -> Tuple[int, List[Tuple[int, int, int]]]:
        """
        Kruskal's algorithm for Minimum Spanning Tree using Union-Find.

        Algorithm:
        1. Sort all edges by weight
        2. Initialize each vertex as its own component (Union-Find)
        3. For each edge in sorted order:
           - If it connects two different components, add it to MST
           - Union the two components
        4. Stop when we have n-1 edges (complete spanning tree)

        Args:
            n: Number of vertices (0 to n-1)
            edges: List of [u, v, weight] representing undirected weighted edges

        Returns:
            Tuple of (total_weight, mst_edges) where mst_edges is list of (u, v, weight)

        Time Complexity: O(E log E) for sorting edges
        Space Complexity: O(V)

        Difficulty: Medium
        Interview Frequency: Medium-High
        Companies: Google, Facebook, Amazon, Microsoft, Apple
        Estimated Time: 35-40 minutes

        Example:
            >>> n = 4
            >>> edges = [[0,1,10], [0,2,6], [0,3,5], [1,3,15], [2,3,4]]
            >>> weight, mst = kruskal_mst(n, edges)
            >>> weight
            19

        Interview Tips:
        - Greedy algorithm - process edges by increasing weight
        - Uses Union-Find (Disjoint Set Union) data structure
        - Naturally avoids cycles via Union-Find
        - Good for sparse graphs (fewer edges)
        - Edge-focused (vs Prim's vertex-focused approach)
        - Be ready to implement or explain Union-Find
        - Path compression and union by rank optimize Union-Find
        """
        if n == 0:
            return 0, []

        # Union-Find data structure
        parent = list(range(n))
        rank = [0] * n

        def find(x):
            """Find with path compression."""
            if parent[x] != x:
                parent[x] = find(parent[x])  # Path compression
            return parent[x]

        def union(x, y):
            """Union by rank."""
            px, py = find(x), find(y)
            if px == py:
                return False  # Already in same set

            # Union by rank
            if rank[px] < rank[py]:
                parent[px] = py
            elif rank[px] > rank[py]:
                parent[py] = px
            else:
                parent[py] = px
                rank[px] += 1
            return True

        # Sort edges by weight
        sorted_edges = sorted(edges, key=lambda x: x[2])

        mst_edges = []
        total_weight = 0

        for u, v, weight in sorted_edges:
            # If vertices are in different components, add edge
            if union(u, v):
                mst_edges.append((u, v, weight))
                total_weight += weight

                # MST complete when we have n-1 edges
                if len(mst_edges) == n - 1:
                    break

        return total_weight, mst_edges
