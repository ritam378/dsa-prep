"""
K-way Merge Pattern

Pattern: Merge k sorted arrays/lists using heap.
When to use:
- Merging k sorted lists
- Smallest range from k lists
- Kth smallest in sorted matrix

Time Complexity: O(N log k) where N is total elements
Space Complexity: O(k)
"""

from typing import List, Optional
import heapq
import sys
sys.path.append('..')
from data_structures.linked_list import ListNode


class KWayMergeSolutions:
    """Solutions using the k-way merge pattern."""

    @staticmethod
    def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
        """
        Merge k sorted arrays.

        Time Complexity: O(N log k)
        Space Complexity: O(k)
        """
        result = []
        min_heap = []

        # Initialize heap with first element from each array
        for i, arr in enumerate(arrays):
            if arr:
                heapq.heappush(min_heap, (arr[0], i, 0))

        while min_heap:
            val, arr_idx, elem_idx = heapq.heappop(min_heap)
            result.append(val)

            # Add next element from same array
            if elem_idx + 1 < len(arrays[arr_idx]):
                next_val = arrays[arr_idx][elem_idx + 1]
                heapq.heappush(min_heap, (next_val, arr_idx, elem_idx + 1))

        return result
