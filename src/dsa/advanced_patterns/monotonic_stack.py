"""
Monotonic Stack Pattern

Pattern: Maintain stack in increasing or decreasing order.
When to use:
- Next greater/smaller element
- Daily temperatures
- Largest rectangle in histogram
- Trapping rain water

Time Complexity: O(n)
Space Complexity: O(n)
"""

from typing import List


class MonotonicStackSolutions:
    """Solutions using the monotonic stack pattern."""

    @staticmethod
    def next_greater_element(nums: List[int]) -> List[int]:
        """
        Find next greater element for each element.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Example:
            >>> MonotonicStackSolutions.next_greater_element([2,1,2,4,3])
            [4, 2, 4, -1, -1]
        """
        result = [-1] * len(nums)
        stack = []  # Store indices

        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = nums[i]
            stack.append(i)

        return result

    @staticmethod
    def daily_temperatures(temperatures: List[int]) -> List[int]:
        """
        Days until warmer temperature.

        Time Complexity: O(n)
        Space Complexity: O(n)

        Example:
            >>> MonotonicStackSolutions.daily_temperatures([73,74,75,71,69,72,76,73])
            [1, 1, 4, 2, 1, 1, 0, 0]
        """
        result = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                idx = stack.pop()
                result[idx] = i - idx
            stack.append(i)

        return result

    @staticmethod
    def largest_rectangle_histogram(heights: List[int]) -> int:
        """
        Find largest rectangle in histogram.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        stack = []
        max_area = 0
        heights.append(0)  # Sentinel

        for i in range(len(heights)):
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h * w)
            stack.append(i)

        heights.pop()  # Remove sentinel
        return max_area
