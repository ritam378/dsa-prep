"""
Topological Sort Pattern

Pattern: Linear ordering of vertices in DAG.
When to use:
- Course schedule problems
- Build order/dependency resolution
- Task scheduling
- Finding compilation order

Time Complexity: O(V + E)
Space Complexity: O(V + E)
"""

from typing import List, Dict
from collections import deque, defaultdict


class TopologicalSortSolutions:
    """Solutions using the topological sort pattern."""

    @staticmethod
    def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
        """
        Check if all courses can be finished (Course Schedule I).

        Time Complexity: O(V + E)
        Space Complexity: O(V + E)

        Example:
            >>> TopologicalSortSolutions.can_finish(2, [[1,0]])
            True
        """
        # Build adjacency list and in-degree count
        graph = defaultdict(list)
        in_degree = [0] * num_courses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        # Find all courses with no prerequisites
        queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
        completed = 0

        while queue:
            course = queue.popleft()
            completed += 1

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return completed == num_courses

    @staticmethod
    def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Find course order (Course Schedule II).

        Time Complexity: O(V + E)
        Space Complexity: O(V + E)
        """
        graph = defaultdict(list)
        in_degree = [0] * num_courses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        queue = deque([i for i in range(num_courses) if in_degree[i] == 0])
        order = []

        while queue:
            course = queue.popleft()
            order.append(course)

            for next_course in graph[course]:
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return order if len(order) == num_courses else []
