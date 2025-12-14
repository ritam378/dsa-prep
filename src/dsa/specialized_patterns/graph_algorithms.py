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
