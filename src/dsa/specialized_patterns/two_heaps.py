"""
Two Heaps Pattern

Pattern: Use min and max heap to track median or split data.
When to use:
- Find median from data stream
- Sliding window median
- IPO problem

Time Complexity: O(log n) for insertions
Space Complexity: O(n)
"""

import heapq


class MedianFinder:
    """Find median from data stream using two heaps."""

    def __init__(self):
        self.max_heap = []  # Lower half (negated for max heap)
        self.min_heap = []  # Upper half

    def add_num(self, num: int) -> None:
        """
        Add number to data structure.

        Time Complexity: O(log n)
        """
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        # Balance heaps
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self) -> float:
        """
        Find median of all numbers.

        Time Complexity: O(1)
        """
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0
        return -self.max_heap[0]
