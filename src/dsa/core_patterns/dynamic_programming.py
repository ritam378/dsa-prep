"""
Dynamic Programming Pattern

Pattern: Break problem into overlapping subproblems, store results.
When to use:
- Optimization problems (min/max)
- Counting problems
- Problems with overlapping subproblems
- Fibonacci, knapsack, LCS, etc.

Time Complexity: Varies (usually O(n) to O(n²))
Space Complexity: O(n) to O(n²)
"""

from typing import List


class DynamicProgrammingSolutions:
    """Solutions using the dynamic programming pattern."""

    @staticmethod
    def fibonacci(n: int) -> int:
        """
        Calculate nth Fibonacci number.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n <= 1:
            return n

        prev, curr = 0, 1

        for _ in range(2, n + 1):
            prev, curr = curr, prev + curr

        return curr

    @staticmethod
    def climb_stairs(n: int) -> int:
        """
        Count ways to climb n stairs (1 or 2 steps at a time).

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n <= 2:
            return n

        prev, curr = 1, 2

        for _ in range(3, n + 1):
            prev, curr = curr, prev + curr

        return curr

    @staticmethod
    def coin_change(coins: List[int], amount: int) -> int:
        """
        Find minimum coins needed to make amount.

        Time Complexity: O(amount * n)
        Space Complexity: O(amount)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1

    @staticmethod
    def longest_increasing_subsequence(nums: List[int]) -> int:
        """
        Find length of longest increasing subsequence.

        Time Complexity: O(n²)
        Space Complexity: O(n)
        """
        if not nums:
            return 0

        dp = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)

    @staticmethod
    def max_subarray_sum(nums: List[int]) -> int:
        """
        Find maximum sum of contiguous subarray (Kadane's algorithm).

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        max_sum = current_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum

    @staticmethod
    def house_robber(nums: List[int]) -> int:
        """
        Maximum money can rob without alerting police (no adjacent houses).

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        prev, curr = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            prev, curr = curr, max(curr, prev + nums[i])

        return curr

    @staticmethod
    def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
        """
        0/1 Knapsack problem.

        Time Complexity: O(n * capacity)
        Space Complexity: O(capacity)
        """
        n = len(weights)
        dp = [0] * (capacity + 1)

        for i in range(n):
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])

        return dp[capacity]
