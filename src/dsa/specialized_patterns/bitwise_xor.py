"""
Bitwise XOR Pattern

Pattern: Use XOR properties to solve problems efficiently.
When to use:
- Finding missing/duplicate numbers
- Single number problems
- Bit manipulation

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class BitwiseXORSolutions:
    """Solutions using bitwise XOR pattern."""

    @staticmethod
    def single_number(nums: List[int]) -> int:
        """
        Find number that appears once (others appear twice).

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = 0
        for num in nums:
            result ^= num
        return result

    @staticmethod
    def missing_number(nums: List[int]) -> int:
        """
        Find missing number in array [0, n].

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        result = len(nums)
        for i, num in enumerate(nums):
            result ^= i ^ num
        return result
