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

    @staticmethod
    def longest_common_subsequence(text1: str, text2: str) -> int:
        """
        Find length of longest common subsequence (LCS).

        LCS is the longest sequence that appears in both strings in the same order
        but not necessarily contiguous.

        Args:
            text1: First string
            text2: Second string

        Returns:
            Length of LCS

        Time Complexity: O(m * n) where m, n are string lengths
        Space Complexity: O(m * n) - can be optimized to O(min(m,n))

        Difficulty: Medium
        Interview Frequency: HIGH - Classic DP problem
        Companies: Google, Facebook, Amazon, Microsoft
        Estimated Time: 25-30 minutes

        Example:
            >>> DynamicProgrammingSolutions.longest_common_subsequence("abcde", "ace")
            3  # "ace" is the LCS

        Interview Tips:
        - Classic 2D DP problem
        - If chars match: dp[i][j] = dp[i-1][j-1] + 1
        - If no match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        - Can optimize space to O(min(m,n)) using rolling array
        - Variation: Print the actual LCS (backtrack through dp table)
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[m][n]

    @staticmethod
    def edit_distance(word1: str, word2: str) -> int:
        """
        Find minimum edit distance (Levenshtein distance) between two words.

        Operations allowed: insert, delete, replace

        Args:
            word1: Source word
            word2: Target word

        Returns:
            Minimum number of operations needed

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)

        Difficulty: Hard
        Interview Frequency: HIGH - Classic DP problem
        Companies: Google, Facebook, Amazon, Microsoft, Apple
        Estimated Time: 30-35 minutes

        Example:
            >>> DynamicProgrammingSolutions.edit_distance("horse", "ros")
            3  # horse -> rorse -> rose -> ros

        Interview Tips:
        - If chars match: dp[i][j] = dp[i-1][j-1]
        - If no match: min of (insert, delete, replace) + 1
        - dp[i][j] = min(dp[i-1][j] + 1,      # delete
                         dp[i][j-1] + 1,      # insert
                         dp[i-1][j-1] + 1)    # replace
        - Base cases: dp[0][j] = j, dp[i][0] = i
        - Space optimization possible (rolling array)
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],      # delete
                        dp[i][j-1],      # insert
                        dp[i-1][j-1]     # replace
                    )

        return dp[m][n]

    @staticmethod
    def can_partition(nums: List[int]) -> bool:
        """
        Determine if array can be partitioned into two subsets with equal sum.

        This is a variation of the subset sum problem.

        Args:
            nums: Array of positive integers

        Returns:
            True if can partition, False otherwise

        Time Complexity: O(n * sum)
        Space Complexity: O(sum)

        Difficulty: Medium
        Interview Frequency: HIGH
        Companies: Amazon, Facebook, Microsoft
        Estimated Time: 20-25 minutes

        Example:
            >>> DynamicProgrammingSolutions.can_partition([1, 5, 11, 5])
            True  # [1, 5, 5] and [11]

        Interview Tips:
        - Reduce to subset sum problem: target = total_sum / 2
        - If total sum is odd, return False immediately
        - Use 1D DP array: dp[i] = can we make sum i?
        - Similar to 0/1 knapsack
        """
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            # Traverse backwards to avoid using same element twice
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        return dp[target]

    @staticmethod
    def word_break(s: str, wordDict: List[str]) -> bool:
        """
        Determine if string can be segmented into dictionary words.

        Args:
            s: String to segment
            wordDict: List of valid words

        Returns:
            True if can be segmented, False otherwise

        Time Complexity: O(n² * m) where n is string length, m is avg word length
        Space Complexity: O(n)

        Difficulty: Medium
        Interview Frequency: HIGH
        Companies: Google, Facebook, Amazon, Microsoft
        Estimated Time: 20-25 minutes

        Example:
            >>> DynamicProgrammingSolutions.word_break("leetcode", ["leet", "code"])
            True

        Interview Tips:
        - dp[i] = can we break s[0:i]?
        - For each position i, check all possible last words ending at i
        - Use set for O(1) word lookup
        - Can also solve with BFS/DFS + memoization
        """
        word_set = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break

        return dp[n]

    @staticmethod
    def decode_ways(s: str) -> int:
        """
        Count number of ways to decode a string where 'A'=1, 'B'=2, ..., 'Z'=26.

        Args:
            s: String of digits

        Returns:
            Number of decode ways

        Time Complexity: O(n)
        Space Complexity: O(1) - using constant space

        Difficulty: Medium
        Interview Frequency: HIGH
        Companies: Google, Facebook, Amazon
        Estimated Time: 20-25 minutes

        Example:
            >>> DynamicProgrammingSolutions.decode_ways("226")
            3  # "BZ" (2 26), "VF" (22 6), "BBF" (2 2 6)

        Interview Tips:
        - Similar to climbing stairs but with constraints
        - Edge cases: '0' at start, consecutive '0's
        - dp[i] = ways to decode s[0:i]
        - If s[i-1] is valid (1-9): add dp[i-1]
        - If s[i-2:i] is valid (10-26): add dp[i-2]
        """
        if not s or s[0] == '0':
            return 0

        n = len(s)
        prev2, prev1 = 1, 1

        for i in range(1, n):
            current = 0

            # Single digit decode (1-9)
            if s[i] != '0':
                current += prev1

            # Two digit decode (10-26)
            two_digit = int(s[i-1:i+1])
            if 10 <= two_digit <= 26:
                current += prev2

            prev2, prev1 = prev1, current

        return prev1

    @staticmethod
    def unique_paths(m: int, n: int) -> int:
        """
        Count unique paths in m x n grid from top-left to bottom-right.
        Can only move right or down.

        Args:
            m: Number of rows
            n: Number of columns

        Returns:
            Number of unique paths

        Time Complexity: O(m * n)
        Space Complexity: O(n) - using 1D DP

        Difficulty: Medium
        Interview Frequency: Medium-High
        Companies: Google, Amazon, Microsoft
        Estimated Time: 15-20 minutes

        Example:
            >>> DynamicProgrammingSolutions.unique_paths(3, 7)
            28

        Interview Tips:
        - dp[i][j] = dp[i-1][j] + dp[i][j-1]
        - Base case: first row and column all have 1 path
        - Can optimize to 1D array (only need previous row)
        - Math solution: C(m+n-2, m-1) = (m+n-2)! / ((m-1)! * (n-1)!)
        """
        dp = [1] * n

        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j-1]

        return dp[n-1]

    @staticmethod
    def min_path_sum(grid: List[List[int]]) -> int:
        """
        Find minimum path sum from top-left to bottom-right in grid.
        Can only move right or down.

        Args:
            grid: 2D grid of non-negative integers

        Returns:
            Minimum path sum

        Time Complexity: O(m * n)
        Space Complexity: O(1) - modify grid in-place, or O(n) for extra space

        Difficulty: Medium
        Interview Frequency: Medium
        Companies: Amazon, Microsoft, Google
        Estimated Time: 15-20 minutes

        Example:
            >>> grid = [[1,3,1],[1,5,1],[4,2,1]]
            >>> DynamicProgrammingSolutions.min_path_sum(grid)
            7  # Path: 1->3->1->1->1

        Interview Tips:
        - dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        - Handle first row and column separately
        - Can modify grid in-place to save space
        """
        m, n = len(grid), len(grid[0])

        # Initialize first row
        for j in range(1, n):
            grid[0][j] += grid[0][j-1]

        # Initialize first column
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]

        # Fill rest of grid
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])

        return grid[m-1][n-1]

    @staticmethod
    def longest_palindromic_substring(s: str) -> str:
        """
        Find the longest palindromic substring.

        Args:
            s: Input string

        Returns:
            Longest palindromic substring

        Time Complexity: O(n²)
        Space Complexity: O(1) - expand around center approach

        Difficulty: Medium
        Interview Frequency: HIGH - Very popular
        Companies: Google, Facebook, Amazon, Microsoft, Apple
        Estimated Time: 25-30 minutes

        Example:
            >>> DynamicProgrammingSolutions.longest_palindromic_substring("babad")
            "bab"  # or "aba"

        Interview Tips:
        - Two approaches: DP O(n²) space, or expand around center O(1) space
        - Expand around center: try both odd and even length palindromes
        - For DP: dp[i][j] = is s[i:j+1] a palindrome?
        - Manacher's algorithm: O(n) but complex for interviews
        """
        if not s:
            return ""

        start, max_len = 0, 0

        def expand_around_center(left: int, right: int) -> int:
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1

        for i in range(len(s)):
            # Odd length palindrome (center is a single char)
            len1 = expand_around_center(i, i)
            # Even length palindrome (center is between two chars)
            len2 = expand_around_center(i, i + 1)

            curr_max = max(len1, len2)
            if curr_max > max_len:
                max_len = curr_max
                start = i - (curr_max - 1) // 2

        return s[start:start + max_len]

    @staticmethod
    def palindrome_partitioning_min_cuts(s: str) -> int:
        """
        Find minimum cuts needed to partition string into palindromes.

        Args:
            s: Input string

        Returns:
            Minimum number of cuts

        Time Complexity: O(n²)
        Space Complexity: O(n²)

        Difficulty: Hard
        Interview Frequency: Medium
        Companies: Amazon, Google
        Estimated Time: 35-40 minutes

        Example:
            >>> DynamicProgrammingSolutions.palindrome_partitioning_min_cuts("aab")
            1  # "aa" | "b"

        Interview Tips:
        - Two DP tables: is_palindrome[i][j] and min_cuts[i]
        - is_palindrome[i][j] = s[i]==s[j] and is_palindrome[i+1][j-1]
        - min_cuts[i] = min cuts for s[0:i+1]
        - If s[0:i+1] is palindrome: min_cuts[i] = 0
        - Else: min_cuts[i] = min(min_cuts[j] + 1) for all j where s[j+1:i+1] is palindrome
        """
        n = len(s)
        if n <= 1:
            return 0

        # Build palindrome lookup table
        is_palindrome = [[False] * n for _ in range(n)]

        for i in range(n):
            is_palindrome[i][i] = True

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    is_palindrome[i][j] = (length == 2) or is_palindrome[i+1][j-1]

        # DP for minimum cuts
        cuts = [0] * n

        for i in range(n):
            if is_palindrome[0][i]:
                cuts[i] = 0
            else:
                min_cut = float('inf')
                for j in range(i):
                    if is_palindrome[j+1][i]:
                        min_cut = min(min_cut, cuts[j] + 1)
                cuts[i] = min_cut

        return cuts[n-1]

    @staticmethod
    def regular_expression_matching(s: str, p: str) -> bool:
        """
        Implement regular expression matching with '.' and '*'.
        '.' matches any single character
        '*' matches zero or more of the preceding element

        Args:
            s: Input string
            p: Pattern

        Returns:
            True if pattern matches string

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)

        Difficulty: Hard
        Interview Frequency: Medium-High
        Companies: Google, Facebook, Amazon
        Estimated Time: 35-45 minutes

        Example:
            >>> DynamicProgrammingSolutions.regular_expression_matching("aa", "a*")
            True

        Interview Tips:
        - dp[i][j] = does s[0:i] match p[0:j]?
        - If p[j-1] is normal char or '.': check chars match and dp[i-1][j-1]
        - If p[j-1] is '*': two cases:
          - Zero occurrence: dp[i][j-2]
          - One or more: check char match and dp[i-1][j]
        - Very tricky edge cases with '*'
        """
        m, n = len(s), len(p)
        dp = [[False] * (n + 1) for _ in range(m + 1)]

        dp[0][0] = True

        # Handle patterns like a*, a*b*, a*b*c*
        for j in range(2, n + 1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j-1] == '*':
                    # Zero occurrence
                    dp[i][j] = dp[i][j-2]
                    # One or more occurrence
                    if p[j-2] == s[i-1] or p[j-2] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                elif p[j-1] == '.' or p[j-1] == s[i-1]:
                    dp[i][j] = dp[i-1][j-1]

        return dp[m][n]

    @staticmethod
    def word_break_ii(s: str, wordDict: List[str]) -> List[str]:
        """
        Return all possible ways to segment string into dictionary words.

        Args:
            s: String to segment
            wordDict: List of valid words

        Returns:
            List of all possible segmentations

        Time Complexity: O(n * 2^n) in worst case
        Space Complexity: O(n * 2^n)

        Difficulty: Hard
        Interview Frequency: Medium
        Companies: Google, Amazon, Facebook
        Estimated Time: 30-40 minutes

        Example:
            >>> DynamicProgrammingSolutions.word_break_ii("catsanddog", ["cat","cats","and","sand","dog"])
            ["cats and dog", "cat sand dog"]

        Interview Tips:
        - Use DFS with memoization
        - Check if word break is possible first (optimization)
        - Memoize by starting index
        - Backtracking + DP combination
        """
        word_set = set(wordDict)
        memo = {}

        def dfs(start: int) -> List[str]:
            if start in memo:
                return memo[start]

            if start == len(s):
                return [""]

            result = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    for sub_sentence in dfs(end):
                        if sub_sentence:
                            result.append(word + " " + sub_sentence)
                        else:
                            result.append(word)

            memo[start] = result
            return result

        return dfs(0)
