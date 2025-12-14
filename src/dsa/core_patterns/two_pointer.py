"""
Two Pointer Pattern

Pattern: Use two pointers to iterate through an array or linked list.
When to use:
- Problems involving sorted arrays
- Finding pairs with a specific sum
- Removing duplicates
- Palindrome problems

Time Complexity: Usually O(n)
Space Complexity: Usually O(1)
"""

from typing import List, Optional


class TwoPointerSolutions:
    """Solutions using the two pointer pattern."""

    @staticmethod
    def two_sum_sorted(numbers: List[int], target: int) -> List[int]:
        """
        Find two numbers in a sorted array that add up to target.

        Problem: Given a sorted array, find indices of two numbers that add up to target.
        Approach: Use two pointers from start and end, move based on sum comparison.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Example:
            >>> TwoPointerSolutions.two_sum_sorted([2, 7, 11, 15], 9)
            [0, 1]
        """
        left, right = 0, len(numbers) - 1

        while left < right:
            current_sum = numbers[left] + numbers[right]

            if current_sum == target:
                return [left, right]
            elif current_sum < target:
                left += 1
            else:
                right -= 1

        return [-1, -1]

    @staticmethod
    def is_palindrome(s: str) -> bool:
        """
        Check if a string is a palindrome, ignoring non-alphanumeric characters.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Example:
            >>> TwoPointerSolutions.is_palindrome("A man, a plan, a canal: Panama")
            True
        """
        left, right = 0, len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        """
        Remove duplicates from sorted array in-place.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Example:
            >>> nums = [1, 1, 2, 2, 3]
            >>> length = TwoPointerSolutions.remove_duplicates(nums)
            >>> nums[:length]
            [1, 2, 3]
        """
        if not nums:
            return 0

        write_pointer = 1

        for read_pointer in range(1, len(nums)):
            if nums[read_pointer] != nums[read_pointer - 1]:
                nums[write_pointer] = nums[read_pointer]
                write_pointer += 1

        return write_pointer

    @staticmethod
    def three_sum(nums: List[int]) -> List[List[int]]:
        """
        Find all unique triplets that sum to zero.

        Time Complexity: O(n²)
        Space Complexity: O(1) excluding output

        Example:
            >>> TwoPointerSolutions.three_sum([-1, 0, 1, 2, -1, -4])
            [[-1, -1, 2], [-1, 0, 1]]
        """
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if current_sum == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    # Skip duplicates for second number
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for third number
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1
                elif current_sum < 0:
                    left += 1
                else:
                    right -= 1

        return result

    @staticmethod
    def container_with_most_water(height: List[int]) -> int:
        """
        Find two lines that form a container with maximum water.

        Time Complexity: O(n)
        Space Complexity: O(1)

        Example:
            >>> TwoPointerSolutions.container_with_most_water([1,8,6,2,5,4,8,3,7])
            49
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            current_area = min(height[left], height[right]) * width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
