"""
Merge Intervals Pattern

Pattern: Sort intervals and merge overlapping ones.
When to use:
- Merging overlapping intervals
- Insert interval
- Finding free time slots
- Meeting rooms

Time Complexity: O(n log n) for sorting
Space Complexity: O(n) for result
"""

from typing import List


class MergeIntervalsSolutions:
    """Solutions using the merge intervals pattern."""

    @staticmethod
    def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.

        Time Complexity: O(n log n)
        Space Complexity: O(n)

        Example:
            >>> MergeIntervalsSolutions.merge_intervals([[1,3],[2,6],[8,10],[15,18]])
            [[1, 6], [8, 10], [15, 18]]
        """
        if not intervals:
            return []

        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for current in intervals[1:]:
            last = merged[-1]

            if current[0] <= last[1]:
                last[1] = max(last[1], current[1])
            else:
                merged.append(current)

        return merged

    @staticmethod
    def insert_interval(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        """
        Insert interval and merge if necessary.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        result = []
        i = 0
        n = len(intervals)

        # Add all intervals before new_interval
        while i < n and intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            i += 1

        # Merge overlapping intervals
        while i < n and intervals[i][0] <= new_interval[1]:
            new_interval[0] = min(new_interval[0], intervals[i][0])
            new_interval[1] = max(new_interval[1], intervals[i][1])
            i += 1

        result.append(new_interval)

        # Add remaining intervals
        while i < n:
            result.append(intervals[i])
            i += 1

        return result

    @staticmethod
    def can_attend_meetings(intervals: List[List[int]]) -> bool:
        """
        Check if person can attend all meetings.

        Time Complexity: O(n log n)
        Space Complexity: O(1)
        """
        intervals.sort()

        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True
