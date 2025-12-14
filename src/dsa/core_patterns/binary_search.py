"""
Binary Search Pattern

Pattern: Divide search space in half repeatedly.
When to use:
- Searching in sorted arrays
- Finding boundaries (first/last occurrence)
- Search in rotated sorted array
- Finding peak element

Time Complexity: O(log n)
Space Complexity: O(1) iterative, O(log n) recursive
"""

from typing import List


class BinarySearchSolutions:
    """Solutions using the binary search pattern."""

    @staticmethod
    def binary_search(arr: List[int], target: int) -> int:
        """
        Standard binary search in sorted array.

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Example:
            >>> BinarySearchSolutions.binary_search([1, 2, 3, 4, 5], 3)
            2
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    @staticmethod
    def find_first_occurrence(arr: List[int], target: int) -> int:
        """
        Find the first occurrence of target in sorted array with duplicates.

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Example:
            >>> BinarySearchSolutions.find_first_occurrence([1, 2, 2, 2, 3], 2)
            1
        """
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                result = mid
                right = mid - 1  # Continue searching in left half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    @staticmethod
    def find_last_occurrence(arr: List[int], target: int) -> int:
        """
        Find the last occurrence of target in sorted array with duplicates.

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Example:
            >>> BinarySearchSolutions.find_last_occurrence([1, 2, 2, 2, 3], 2)
            3
        """
        left, right = 0, len(arr) - 1
        result = -1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                result = mid
                left = mid + 1  # Continue searching in right half
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return result

    @staticmethod
    def search_rotated_sorted_array(arr: List[int], target: int) -> int:
        """
        Search in rotated sorted array.

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Example:
            >>> BinarySearchSolutions.search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0)
            4
        """
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if arr[mid] == target:
                return mid

            # Determine which half is sorted
            if arr[left] <= arr[mid]:
                # Left half is sorted
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                # Right half is sorted
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

    @staticmethod
    def find_minimum_rotated_array(arr: List[int]) -> int:
        """
        Find minimum element in rotated sorted array.

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Example:
            >>> BinarySearchSolutions.find_minimum_rotated_array([3, 4, 5, 1, 2])
            1
        """
        left, right = 0, len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] > arr[right]:
                # Minimum is in right half
                left = mid + 1
            else:
                # Minimum is in left half (including mid)
                right = mid

        return arr[left]

    @staticmethod
    def sqrt(x: int) -> int:
        """
        Compute square root using binary search (integer part).

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Example:
            >>> BinarySearchSolutions.sqrt(8)
            2
        """
        if x < 2:
            return x

        left, right = 1, x // 2

        while left <= right:
            mid = left + (right - left) // 2
            square = mid * mid

            if square == x:
                return mid
            elif square < x:
                left = mid + 1
            else:
                right = mid - 1

        return right

    @staticmethod
    def find_peak_element(arr: List[int]) -> int:
        """
        Find a peak element (greater than neighbors).

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Example:
            >>> BinarySearchSolutions.find_peak_element([1, 2, 3, 1])
            2
        """
        left, right = 0, len(arr) - 1

        while left < right:
            mid = left + (right - left) // 2

            if arr[mid] > arr[mid + 1]:
                # Peak is in left half (including mid)
                right = mid
            else:
                # Peak is in right half
                left = mid + 1

        return left
