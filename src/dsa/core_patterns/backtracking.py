"""
Backtracking Pattern

Pattern: Build solution incrementally and backtrack when constraint violated.
When to use:
- Generating combinations/permutations
- Constraint satisfaction problems
- N-Queens, Sudoku solver
- Path finding with constraints

Time Complexity: Usually exponential O(2^n) or O(n!)
Space Complexity: O(n) for recursion stack
"""

from typing import List


class BacktrackingSolutions:
    """Solutions using the backtracking pattern."""

    @staticmethod
    def subsets(nums: List[int]) -> List[List[int]]:
        """
        Generate all subsets.

        Time Complexity: O(2^n)
        Space Complexity: O(n)
        """
        result = []

        def backtrack(start: int, path: List[int]) -> None:
            result.append(list(path))

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result

    @staticmethod
    def permutations(nums: List[int]) -> List[List[int]]:
        """
        Generate all permutations.

        Time Complexity: O(n!)
        Space Complexity: O(n)
        """
        result = []

        def backtrack(path: List[int], remaining: List[int]) -> None:
            if not remaining:
                result.append(list(path))
                return

            for i in range(len(remaining)):
                backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtrack([], nums)
        return result

    @staticmethod
    def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
        """
        Find all combinations that sum to target.

        Time Complexity: O(2^n)
        Space Complexity: O(n)
        """
        result = []

        def backtrack(start: int, path: List[int], remaining: int) -> None:
            if remaining == 0:
                result.append(list(path))
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, path, remaining - candidates[i])
                path.pop()

        backtrack(0, [], target)
        return result

    @staticmethod
    def generate_parentheses(n: int) -> List[str]:
        """
        Generate all valid parentheses combinations.

        Time Complexity: O(4^n / sqrt(n))
        Space Complexity: O(n)
        """
        result = []

        def backtrack(current: str, open_count: int, close_count: int) -> None:
            if len(current) == 2 * n:
                result.append(current)
                return

            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)

            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)

        backtrack('', 0, 0)
        return result
