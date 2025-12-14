"""
Cyclic Sort Pattern

Pattern: Place elements at their correct indices in one pass.
When to use:
- Arrays with numbers in range [1, n]
- Finding missing/duplicate numbers
- First missing positive

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List


class CyclicSortSolutions:
    """Solutions using the cyclic sort pattern."""

    @staticmethod
    def cyclic_sort(nums: List[int]) -> None:
        """
        Sort array using cyclic sort (numbers 1 to n).

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

    @staticmethod
    def find_missing_number(nums: List[int]) -> int:
        """
        Find missing number in array containing [0, n].

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i, n = 0, len(nums)

        while i < n:
            correct_idx = nums[i]
            if correct_idx < n and nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i:
                return i

        return n

    @staticmethod
    def find_duplicate(nums: List[int]) -> int:
        """
        Find duplicate number in array.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        i = 0
        while i < len(nums):
            correct_idx = nums[i] - 1
            if nums[i] != nums[correct_idx]:
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]

        return len(nums)
