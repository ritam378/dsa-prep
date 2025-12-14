"""
Subsets Pattern (Combinations/Permutations)

Pattern: Generate all combinations or permutations.
When to use:
- Generating subsets
- Generating permutations
- Combination sum
- Letter combinations

Time Complexity: O(2^n) for subsets, O(n!) for permutations
Space Complexity: O(n)
"""

from typing import List


class SubsetsSolutions:
    """Solutions for generating subsets and permutations."""

    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        """Generate all subsets."""
        result = []

        def backtrack(start: int, path: List[int]) -> None:
            result.append(list(path))
            for i in range(start, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return result

    @staticmethod
    def permutations(nums: List[int]) -> List[List[int]]:
        """Generate all permutations."""
        result = []

        def backtrack(path: List[int], used: List[bool]) -> None:
            if len(path) == len(nums):
                result.append(list(path))
                return

            for i in range(len(nums)):
                if not used[i]:
                    used[i] = True
                    backtrack(path + [nums[i]], used)
                    used[i] = False

        backtrack([], [False] * len(nums))
        return result
