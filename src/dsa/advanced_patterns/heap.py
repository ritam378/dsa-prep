"""
Heap Pattern (Top K Elements)

Pattern: Use heap to efficiently find/maintain top k elements.
When to use:
- Finding k largest/smallest elements
- K closest points
- Top k frequent elements
- Kth largest element

Time Complexity: O(n log k)
Space Complexity: O(k)
"""

from typing import List
import heapq
from collections import Counter


class HeapSolutions:
    """Solutions using the heap pattern."""

    @staticmethod
    def kth_largest(nums: List[int], k: int) -> int:
        """
        Find kth largest element.

        Time Complexity: O(n log k)
        Space Complexity: O(k)

        Example:
            >>> HeapSolutions.kth_largest([3,2,1,5,6,4], 2)
            5
        """
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]

    @staticmethod
    def k_closest_points(points: List[List[int]], k: int) -> List[List[int]]:
        """
        Find k closest points to origin.

        Time Complexity: O(n log k)
        Space Complexity: O(k)
        """
        max_heap = []

        for x, y in points:
            dist = -(x*x + y*y)  # Negative for max heap
            if len(max_heap) < k:
                heapq.heappush(max_heap, (dist, [x, y]))
            elif dist > max_heap[0][0]:
                heapq.heapreplace(max_heap, (dist, [x, y]))

        return [point for _, point in max_heap]

    @staticmethod
    def top_k_frequent(nums: List[int], k: int) -> List[int]:
        """
        Find k most frequent elements.

        Time Complexity: O(n log k)
        Space Complexity: O(n)
        """
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
