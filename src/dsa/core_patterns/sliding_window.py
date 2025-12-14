"""
Sliding Window Pattern

Pattern: Maintain a window that slides through the array/string.
When to use:
- Finding subarrays/substrings with specific properties
- Maximum/minimum sum of subarray of size k
- Longest substring with k distinct characters

Time Complexity: Usually O(n)
Space Complexity: Usually O(k) where k is window size
"""

from typing import List, Dict
from collections import defaultdict


class SlidingWindowSolutions:
    """Solutions using the sliding window pattern."""

    @staticmethod
    def max_sum_subarray(arr: List[int], k: int) -> int:
        """
        Find maximum sum of any contiguous subarray of size k.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Example:
            >>> SlidingWindowSolutions.max_sum_subarray([2, 1, 5, 1, 3, 2], 3)
            9
        """
        if not arr or k > len(arr):
            return 0

        window_sum = sum(arr[:k])
        max_sum = window_sum

        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i - k] + arr[i]
            max_sum = max(max_sum, window_sum)

        return max_sum

    @staticmethod
    def longest_substring_k_distinct(s: str, k: int) -> int:
        """
        Find the longest substring with at most k distinct characters.

        Time Complexity: O(n)
        Space Complexity: O(k)

        Example:
            >>> SlidingWindowSolutions.longest_substring_k_distinct("araaci", 2)
            4
        """
        if not s or k == 0:
            return 0

        char_frequency: Dict[str, int] = {}
        window_start = 0
        max_length = 0

        for window_end in range(len(s)):
            right_char = s[window_end]
            char_frequency[right_char] = char_frequency.get(right_char, 0) + 1

            # Shrink window if we have more than k distinct characters
            while len(char_frequency) > k:
                left_char = s[window_start]
                char_frequency[left_char] -= 1
                if char_frequency[left_char] == 0:
                    del char_frequency[left_char]
                window_start += 1

            max_length = max(max_length, window_end - window_start + 1)

        return max_length

    @staticmethod
    def min_subarray_sum(target: int, arr: List[int]) -> int:
        """
        Find minimum length of contiguous subarray with sum >= target.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Example:
            >>> SlidingWindowSolutions.min_subarray_sum(7, [2, 3, 1, 2, 4, 3])
            2
        """
        min_length = float('inf')
        window_sum = 0
        window_start = 0

        for window_end in range(len(arr)):
            window_sum += arr[window_end]

            while window_sum >= target:
                min_length = min(min_length, window_end - window_start + 1)
                window_sum -= arr[window_start]
                window_start += 1

        return 0 if min_length == float('inf') else min_length

    @staticmethod
    def longest_substring_without_repeating(s: str) -> int:
        """
        Find length of longest substring without repeating characters.

        Time Complexity: O(n)
        Space Complexity: O(min(n, m)) where m is charset size

        Example:
            >>> SlidingWindowSolutions.longest_substring_without_repeating("abcabcbb")
            3
        """
        char_index_map: Dict[str, int] = {}
        max_length = 0
        window_start = 0

        for window_end in range(len(s)):
            right_char = s[window_end]

            # If character is already in window, shrink from left
            if right_char in char_index_map:
                window_start = max(window_start, char_index_map[right_char] + 1)

            char_index_map[right_char] = window_end
            max_length = max(max_length, window_end - window_start + 1)

        return max_length

    @staticmethod
    def permutation_in_string(s1: str, s2: str) -> bool:
        """
        Check if s2 contains a permutation of s1.

        Time Complexity: O(n)
        Space Complexity: O(1) - fixed 26 letters

        Example:
            >>> SlidingWindowSolutions.permutation_in_string("ab", "eidbaooo")
            True
        """
        if len(s1) > len(s2):
            return False

        s1_count: Dict[str, int] = {}
        window_count: Dict[str, int] = {}

        # Count frequency of characters in s1
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1

        window_size = len(s1)

        # Initialize first window
        for i in range(window_size):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) + 1

        if window_count == s1_count:
            return True

        # Slide the window
        for i in range(window_size, len(s2)):
            # Add new character
            new_char = s2[i]
            window_count[new_char] = window_count.get(new_char, 0) + 1

            # Remove old character
            old_char = s2[i - window_size]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]

            if window_count == s1_count:
                return True

        return False
