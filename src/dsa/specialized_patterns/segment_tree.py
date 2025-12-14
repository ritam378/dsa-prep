"""
Segment Tree Pattern

Pattern: Tree structure for range queries and updates.
When to use:
- Range sum/min/max queries
- Range updates
- Interval problems

Time Complexity: O(log n) for query/update, O(n) for build
Space Complexity: O(n)
"""

from typing import List


class SegmentTree:
    """Segment Tree for range sum queries."""

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0] * (4 * self.n)
        if nums:
            self._build(nums, 0, 0, self.n - 1)

    def _build(self, nums: List[int], node: int, start: int, end: int) -> None:
        """Build segment tree."""
        if start == end:
            self.tree[node] = nums[start]
        else:
            mid = (start + end) // 2
            self._build(nums, 2*node+1, start, mid)
            self._build(nums, 2*node+2, mid+1, end)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def update(self, idx: int, val: int) -> None:
        """Update value at index."""
        self._update_helper(0, 0, self.n - 1, idx, val)

    def _update_helper(self, node: int, start: int, end: int, idx: int, val: int) -> None:
        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self._update_helper(2*node+1, start, mid, idx, val)
            else:
                self._update_helper(2*node+2, mid+1, end, idx, val)
            self.tree[node] = self.tree[2*node+1] + self.tree[2*node+2]

    def query(self, left: int, right: int) -> int:
        """Query sum in range [left, right]."""
        return self._query_helper(0, 0, self.n - 1, left, right)

    def _query_helper(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if start > right or end < left:
            return 0
        if start >= left and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self._query_helper(2*node+1, start, mid, left, right)
        right_sum = self._query_helper(2*node+2, mid+1, end, left, right)
        return left_sum + right_sum
