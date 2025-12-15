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

    @staticmethod
    def search_range(nums: List[int], target: int) -> List[int]:
        """
        Find first and last position of element in sorted array.

        Difficulty: Medium
        Frequency: HIGH - Amazon, Facebook, Google

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Interview Tips:
        - Use binary search twice: once for left bound, once for right bound
        - Can also use find_first_occurrence and find_last_occurrence
        - Watch out for edge cases: target not found, single element

        Example:
            >>> BinarySearchSolutions.search_range([5,7,7,8,8,10], 8)
            [3, 4]
            >>> BinarySearchSolutions.search_range([5,7,7,8,8,10], 6)
            [-1, -1]
        """
        def find_bound(is_first: bool) -> int:
            left, right = 0, len(nums) - 1
            result = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    result = mid
                    if is_first:
                        right = mid - 1  # Search left for first occurrence
                    else:
                        left = mid + 1   # Search right for last occurrence
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return result

        if not nums:
            return [-1, -1]

        return [find_bound(True), find_bound(False)]

    @staticmethod
    def search_matrix(matrix: List[List[int]], target: int) -> bool:
        """
        Search a 2D matrix where each row is sorted and first element of each
        row is greater than last element of previous row.

        Difficulty: Medium
        Frequency: HIGH - Microsoft, Amazon

        Time Complexity: O(log(m*n))
        Space Complexity: O(1)

        Interview Tips:
        - Treat 2D matrix as 1D sorted array
        - Convert 1D index to 2D: row = idx // n, col = idx % n
        - This is basically binary search on flattened array

        Example:
            >>> matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
            >>> BinarySearchSolutions.search_matrix(matrix, 3)
            True
            >>> BinarySearchSolutions.search_matrix(matrix, 13)
            False
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1

        while left <= right:
            mid = left + (right - left) // 2
            # Convert 1D index to 2D coordinates
            mid_val = matrix[mid // n][mid % n]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    @staticmethod
    def search_matrix_ii(matrix: List[List[int]], target: int) -> bool:
        """
        Search a 2D matrix where rows and columns are sorted independently.

        Difficulty: Medium
        Frequency: HIGH - Amazon, Google, Microsoft

        Time Complexity: O(m + n)
        Space Complexity: O(1)

        Interview Tips:
        - Start from top-right (or bottom-left) corner
        - If current > target, move left; if current < target, move down
        - This is NOT pure binary search but uses sorted property
        - Can also binary search each row: O(m log n)

        Example:
            >>> matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
            >>> BinarySearchSolutions.search_matrix_ii(matrix, 5)
            True
            >>> BinarySearchSolutions.search_matrix_ii(matrix, 20)
            False
        """
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        # Start from top-right corner
        row, col = 0, n - 1

        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down

        return False

    @staticmethod
    def first_bad_version(n: int, is_bad_version) -> int:
        """
        Find first bad version in versions 1 to n.

        Difficulty: Easy
        Frequency: HIGH - Facebook, Google

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Interview Tips:
        - Classic binary search to find first occurrence
        - Minimize API calls (is_bad_version)
        - Watch for integer overflow: use left + (right - left) // 2

        Args:
            n: Total number of versions
            is_bad_version: API function that returns True if version is bad

        Example:
            >>> def is_bad(v): return v >= 4
            >>> BinarySearchSolutions.first_bad_version(5, is_bad)
            4
        """
        left, right = 1, n

        while left < right:
            mid = left + (right - left) // 2

            if is_bad_version(mid):
                right = mid  # First bad is in left half (including mid)
            else:
                left = mid + 1  # First bad is in right half

        return left

    @staticmethod
    def koko_eating_bananas(piles: List[int], h: int) -> int:
        """
        Find minimum eating speed k such that Koko can eat all bananas within h hours.

        Difficulty: Medium
        Frequency: HIGH - Google, Facebook

        Time Complexity: O(n log m) where m is max(piles)
        Space Complexity: O(1)

        Interview Tips:
        - Binary search on the answer (eating speed)
        - Search range: [1, max(piles)]
        - For each speed k, calculate hours needed: sum(ceil(pile/k))
        - Find minimum k where hours <= h

        Example:
            >>> BinarySearchSolutions.koko_eating_bananas([3,6,7,11], 8)
            4
            >>> BinarySearchSolutions.koko_eating_bananas([30,11,23,4,20], 5)
            30
        """
        import math

        def can_finish(speed: int) -> bool:
            """Check if can finish all piles with given speed in h hours."""
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / speed)
            return hours <= h

        left, right = 1, max(piles)

        while left < right:
            mid = left + (right - left) // 2

            if can_finish(mid):
                right = mid  # Try slower speed
            else:
                left = mid + 1  # Need faster speed

        return left

    @staticmethod
    def find_min_rotated_with_duplicates(nums: List[int]) -> int:
        """
        Find minimum in rotated sorted array with duplicates.

        Difficulty: Hard
        Frequency: Medium - Amazon, Microsoft

        Time Complexity: O(log n) average, O(n) worst case
        Space Complexity: O(1)

        Interview Tips:
        - Similar to find_minimum_rotated_array but handles duplicates
        - When nums[mid] == nums[right], can't determine which half has min
        - Solution: shrink right boundary by 1
        - Worst case O(n): [1,1,1,1,1,0,1]

        Example:
            >>> BinarySearchSolutions.find_min_rotated_with_duplicates([2,2,2,0,1])
            0
            >>> BinarySearchSolutions.find_min_rotated_with_duplicates([1,3,5])
            1
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] > nums[right]:
                # Min is in right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # Min is in left half (including mid)
                right = mid
            else:
                # nums[mid] == nums[right], can't determine
                # Shrink right boundary
                right -= 1

        return nums[left]

    @staticmethod
    def single_non_duplicate(nums: List[int]) -> int:
        """
        Find single element in sorted array where every element appears twice except one.

        Difficulty: Medium
        Frequency: Medium - Google, Amazon

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Interview Tips:
        - XOR would be O(n); binary search achieves O(log n)
        - Key insight: pairs should start at even indices
        - If mid is even and nums[mid] == nums[mid+1], single is on right
        - If mid is even and nums[mid] != nums[mid+1], single is on left

        Example:
            >>> BinarySearchSolutions.single_non_duplicate([1,1,2,3,3,4,4,8,8])
            2
            >>> BinarySearchSolutions.single_non_duplicate([3,3,7,7,10,11,11])
            10
        """
        left, right = 0, len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Ensure mid is even for easier comparison
            if mid % 2 == 1:
                mid -= 1

            # Check if pair starts at mid
            if nums[mid] == nums[mid + 1]:
                # Pair is intact, single is on right
                left = mid + 2
            else:
                # Pair is broken, single is on left (including mid)
                right = mid

        return nums[left]

    @staticmethod
    def next_greatest_letter(letters: List[str], target: str) -> str:
        """
        Find smallest letter in sorted array greater than target.

        Difficulty: Easy
        Frequency: Medium - LinkedIn, Amazon

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Interview Tips:
        - Letters wrap around (if no letter > target, return first letter)
        - Binary search to find upper bound
        - Return letters[left % len(letters)]

        Example:
            >>> BinarySearchSolutions.next_greatest_letter(['c','f','j'], 'a')
            'c'
            >>> BinarySearchSolutions.next_greatest_letter(['c','f','j'], 'c')
            'f'
            >>> BinarySearchSolutions.next_greatest_letter(['c','f','j'], 'k')
            'c'
        """
        left, right = 0, len(letters) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid + 1
            else:
                right = mid - 1

        # Wrap around if left exceeds array bounds
        return letters[left % len(letters)]

    @staticmethod
    def search_insert_position(nums: List[int], target: int) -> int:
        """
        Find index where target should be inserted in sorted array.

        Difficulty: Easy
        Frequency: HIGH - Amazon, Microsoft

        Time Complexity: O(log n)
        Space Complexity: O(1)

        Interview Tips:
        - Standard binary search modification
        - If target not found, left pointer points to insertion position
        - Return left at the end

        Example:
            >>> BinarySearchSolutions.search_insert_position([1,3,5,6], 5)
            2
            >>> BinarySearchSolutions.search_insert_position([1,3,5,6], 2)
            1
            >>> BinarySearchSolutions.search_insert_position([1,3,5,6], 7)
            4
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

    @staticmethod
    def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
        """
        Find median of two sorted arrays.

        Difficulty: Hard
        Frequency: VERY HIGH - Google, Amazon, Microsoft, Facebook

        Time Complexity: O(log(min(m,n)))
        Space Complexity: O(1)

        Interview Tips:
        - One of the hardest binary search problems
        - Binary search on the smaller array to partition both arrays
        - Partition such that all elements on left <= all elements on right
        - Key: find correct partition where max_left <= min_right
        - Handle even/odd total length cases

        Example:
            >>> BinarySearchSolutions.find_median_sorted_arrays([1,3], [2])
            2.0
            >>> BinarySearchSolutions.find_median_sorted_arrays([1,2], [3,4])
            2.5
        """
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            partition1 = (left + right) // 2
            partition2 = (m + n + 1) // 2 - partition1

            # Get max of left parts and min of right parts
            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]

            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]

            # Check if we found the correct partition
            if max_left1 <= min_right2 and max_left2 <= min_right1:
                # Found the correct partition
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                # Too far right in nums1, move left
                right = partition1 - 1
            else:
                # Too far left in nums1, move right
                left = partition1 + 1

        raise ValueError("Input arrays are not sorted")
