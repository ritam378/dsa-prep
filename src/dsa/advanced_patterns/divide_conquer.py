"""
Divide and Conquer Pattern

Pattern: Break problem into smaller subproblems, solve recursively, combine results.
When to use:
- Problem can be divided into independent subproblems
- Optimal solution can be constructed from subproblem solutions
- Classic examples: merge sort, quick sort, binary search

Time Complexity: Often O(n log n) or O(log n)
Space Complexity: O(log n) for recursion stack

Key Characteristics:
1. Divide: Break into smaller subproblems
2. Conquer: Solve subproblems recursively
3. Combine: Merge solutions
"""

from typing import List, Optional, Tuple
from dsa.data_structures.tree import TreeNode
from dsa.data_structures.linked_list import ListNode


class DivideConquerSolutions:
    """Solutions using the divide and conquer pattern."""

    @staticmethod
    def merge_k_sorted_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Merge k sorted linked lists using divide and conquer.

        Difficulty: Hard
        Frequency: VERY HIGH - Amazon, Google, Facebook, Microsoft

        Time Complexity: O(N log k) where N is total nodes, k is number of lists
        Space Complexity: O(log k) for recursion

        Interview Tips:
        - Divide and conquer is more efficient than merging one by one
        - Alternative: use min heap for O(N log k) time
        - Pair-wise merge reduces comparisons

        Example:
            >>> lists = [ListNode(1, ListNode(4)), ListNode(1, ListNode(3)), ListNode(2)]
            >>> result = DivideConquerSolutions.merge_k_sorted_lists(lists)
            >>> # Result: 1->1->2->3->4
        """
        def merge_two_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            """Helper to merge two sorted lists."""
            dummy = ListNode(0)
            curr = dummy

            while l1 and l2:
                if l1.val < l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next

            curr.next = l1 if l1 else l2
            return dummy.next

        def merge_lists(lists: List[Optional[ListNode]], left: int, right: int) -> Optional[ListNode]:
            """Divide and conquer merge."""
            if left > right:
                return None
            if left == right:
                return lists[left]

            mid = (left + right) // 2
            left_merged = merge_lists(lists, left, mid)
            right_merged = merge_lists(lists, mid + 1, right)

            return merge_two_lists(left_merged, right_merged)

        if not lists:
            return None
        return merge_lists(lists, 0, len(lists) - 1)

    @staticmethod
    def count_smaller_after_self(nums: List[int]) -> List[int]:
        """
        Count numbers smaller than current number to its right.

        Difficulty: Hard
        Frequency: HIGH - Google, Amazon

        Time Complexity: O(n log n)
        Space Complexity: O(n)

        Interview Tips:
        - Use modified merge sort to count inversions
        - Track original indices during sorting
        - Update counts during merge step
        - Alternative: Binary Indexed Tree (Fenwick Tree)

        Example:
            >>> DivideConquerSolutions.count_smaller_after_self([5,2,6,1])
            [2, 1, 1, 0]
            >>> DivideConquerSolutions.count_smaller_after_self([2,0,1])
            [2, 0, 0]
        """
        def merge_sort(arr: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
            """Modified merge sort that counts smaller elements."""
            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            # Merge and count
            merged = []
            i = j = 0
            right_count = 0

            while i < len(left) or j < len(right):
                if j == len(right) or (i < len(left) and left[i][0] <= right[j][0]):
                    # Element from left is being placed
                    # All elements in right[:j] are smaller
                    counts[left[i][1]] += right_count
                    merged.append(left[i])
                    i += 1
                else:
                    # Element from right is being placed
                    right_count += 1
                    merged.append(right[j])
                    j += 1

            return merged

        # Create list of (value, original_index)
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        counts = [0] * len(nums)

        merge_sort(indexed_nums)
        return counts

    @staticmethod
    def closest_pair_of_points(points: List[List[int]]) -> float:
        """
        Find minimum distance between any two points in 2D plane.

        Difficulty: Hard
        Frequency: Medium - Google, Microsoft

        Time Complexity: O(n log n)
        Space Complexity: O(n)

        Interview Tips:
        - Brute force is O(n²)
        - Divide and conquer achieves O(n log n)
        - Key: check strip between left and right halves
        - Sort by x, then check y-sorted strip

        Example:
            >>> points = [[0,0],[1,1],[2,2]]
            >>> DivideConquerSolutions.closest_pair_of_points(points)
            1.4142135623730951
        """
        def distance(p1: List[int], p2: List[int]) -> float:
            return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2) ** 0.5

        def brute_force(points: List[List[int]]) -> float:
            """For small arrays, use brute force."""
            min_dist = float('inf')
            for i in range(len(points)):
                for j in range(i + 1, len(points)):
                    min_dist = min(min_dist, distance(points[i], points[j]))
            return min_dist

        def strip_closest(strip: List[List[int]], d: float) -> float:
            """Find closest pair in strip."""
            min_dist = d
            # Strip is sorted by y-coordinate
            strip.sort(key=lambda p: p[1])

            for i in range(len(strip)):
                j = i + 1
                # Only check points within distance d
                while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
                    min_dist = min(min_dist, distance(strip[i], strip[j]))
                    j += 1

            return min_dist

        def closest_util(px: List[List[int]]) -> float:
            """Recursive divide and conquer."""
            n = len(px)

            # Use brute force for small arrays
            if n <= 3:
                return brute_force(px)

            # Divide
            mid = n // 2
            midpoint = px[mid]

            left_min = closest_util(px[:mid])
            right_min = closest_util(px[mid:])

            # Find minimum of two
            d = min(left_min, right_min)

            # Build strip of points closer than d to dividing line
            strip = [p for p in px if abs(p[0] - midpoint[0]) < d]

            # Find closest in strip
            return min(d, strip_closest(strip, d))

        # Sort by x-coordinate
        px = sorted(points, key=lambda p: p[0])
        return closest_util(px)

    @staticmethod
    def different_ways_to_compute(expression: str) -> List[int]:
        """
        Compute all possible results from different ways to group numbers and operators.

        Difficulty: Medium
        Frequency: Medium - Google, Amazon

        Time Complexity: O(2^n) where n is number of operators
        Space Complexity: O(2^n)

        Interview Tips:
        - Classic divide and conquer problem
        - Divide at each operator
        - Combine results from left and right
        - Use memoization to optimize

        Example:
            >>> sorted(DivideConquerSolutions.different_ways_to_compute("2-1-1"))
            [0, 2]
            >>> sorted(DivideConquerSolutions.different_ways_to_compute("2*3-4*5"))
            [-34, -14, -10, -10, 10]
        """
        memo = {}

        def compute(expr: str) -> List[int]:
            if expr in memo:
                return memo[expr]

            results = []

            for i, char in enumerate(expr):
                if char in ['+', '-', '*']:
                    # Divide at this operator
                    left_results = compute(expr[:i])
                    right_results = compute(expr[i+1:])

                    # Combine all results
                    for left in left_results:
                        for right in right_results:
                            if char == '+':
                                results.append(left + right)
                            elif char == '-':
                                results.append(left - right)
                            else:  # char == '*'
                                results.append(left * right)

            # Base case: expression is just a number
            if not results:
                results.append(int(expr))

            memo[expr] = results
            return results

        return compute(expression)

    @staticmethod
    def maximum_subarray_sum(nums: List[int]) -> int:
        """
        Find contiguous subarray with largest sum using divide and conquer.

        Difficulty: Medium (Easy with Kadane's)
        Frequency: VERY HIGH - Amazon, Microsoft, Google

        Time Complexity: O(n log n) - Kadane's is O(n)
        Space Complexity: O(log n)

        Interview Tips:
        - Kadane's algorithm is simpler and O(n)
        - Divide and conquer is educational
        - Max can be in left, right, or crossing middle
        - This demonstrates the D&C paradigm

        Example:
            >>> DivideConquerSolutions.maximum_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])
            6
            >>> DivideConquerSolutions.maximum_subarray_sum([1])
            1
        """
        def max_crossing_sum(arr: List[int], left: int, mid: int, right: int) -> int:
            """Find max sum crossing the middle."""
            # Include elements on left of mid
            left_sum = float('-inf')
            curr_sum = 0
            for i in range(mid, left - 1, -1):
                curr_sum += arr[i]
                left_sum = max(left_sum, curr_sum)

            # Include elements on right of mid
            right_sum = float('-inf')
            curr_sum = 0
            for i in range(mid + 1, right + 1):
                curr_sum += arr[i]
                right_sum = max(right_sum, curr_sum)

            return left_sum + right_sum

        def max_subarray_util(arr: List[int], left: int, right: int) -> int:
            """Recursive divide and conquer."""
            if left == right:
                return arr[left]

            mid = (left + right) // 2

            # Maximum is either in left, right, or crossing middle
            left_max = max_subarray_util(arr, left, mid)
            right_max = max_subarray_util(arr, mid + 1, right)
            cross_max = max_crossing_sum(arr, left, mid, right)

            return max(left_max, right_max, cross_max)

        return max_subarray_util(nums, 0, len(nums) - 1)

    @staticmethod
    def quick_select(nums: List[int], k: int) -> int:
        """
        Find kth largest element using QuickSelect (divide and conquer).

        Difficulty: Medium
        Frequency: VERY HIGH - Amazon, Facebook, Google

        Time Complexity: O(n) average, O(n²) worst case
        Space Complexity: O(1)

        Interview Tips:
        - Based on QuickSort partition
        - Don't need to sort entire array
        - Randomized pivot gives O(n) expected time
        - Alternative: Min heap of size k is O(n log k)

        Example:
            >>> DivideConquerSolutions.quick_select([3,2,1,5,6,4], 2)
            5
            >>> DivideConquerSolutions.quick_select([3,2,3,1,2,4,5,5,6], 4)
            4
        """
        import random

        def partition(left: int, right: int, pivot_idx: int) -> int:
            """Partition array around pivot."""
            pivot_value = nums[pivot_idx]

            # Move pivot to end
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            # Move all larger elements to the left
            store_idx = left
            for i in range(left, right):
                if nums[i] > pivot_value:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            # Move pivot to final position
            nums[right], nums[store_idx] = nums[store_idx], nums[right]
            return store_idx

        def select(left: int, right: int, k_smallest: int) -> int:
            """Find kth largest element."""
            if left == right:
                return nums[left]

            # Random pivot for expected O(n)
            pivot_idx = random.randint(left, right)
            pivot_idx = partition(left, right, pivot_idx)

            # The pivot is in its final sorted position
            if k_smallest == pivot_idx:
                return nums[k_smallest]
            elif k_smallest < pivot_idx:
                return select(left, pivot_idx - 1, k_smallest)
            else:
                return select(pivot_idx + 1, right, k_smallest)

        # kth largest = (k-1)th in descending order (0-indexed)
        return select(0, len(nums) - 1, k - 1)

    @staticmethod
    def reverse_pairs(nums: List[int]) -> int:
        """
        Count reverse pairs where i < j and nums[i] > 2*nums[j].

        Difficulty: Hard
        Frequency: Medium - Google, Amazon

        Time Complexity: O(n log n)
        Space Complexity: O(n)

        Interview Tips:
        - Modified merge sort to count pairs
        - Similar to count inversions
        - Count pairs before merging
        - Two pointers to count efficiently

        Example:
            >>> DivideConquerSolutions.reverse_pairs([1,3,2,3,1])
            2
            >>> DivideConquerSolutions.reverse_pairs([2,4,3,5,1])
            3
        """
        def merge_sort_count(arr: List[int], temp: List[int], left: int, right: int) -> int:
            """Modified merge sort that counts reverse pairs."""
            if left >= right:
                return 0

            mid = (left + right) // 2
            count = 0

            count += merge_sort_count(arr, temp, left, mid)
            count += merge_sort_count(arr, temp, mid + 1, right)

            # Count reverse pairs before merging
            j = mid + 1
            for i in range(left, mid + 1):
                while j <= right and arr[i] > 2 * arr[j]:
                    j += 1
                count += j - (mid + 1)

            # Merge
            i = left
            j = mid + 1
            k = left

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            # Copy back
            for i in range(left, right + 1):
                arr[i] = temp[i]

            return count

        temp = [0] * len(nums)
        return merge_sort_count(nums, temp, 0, len(nums) - 1)

    @staticmethod
    def search_2d_matrix_dc(matrix: List[List[int]], target: int) -> bool:
        """
        Search in 2D matrix using divide and conquer.

        Difficulty: Medium
        Frequency: Medium - Microsoft, Google

        Time Complexity: O(m + n)
        Space Complexity: O(log(m+n)) for recursion

        Interview Tips:
        - Start from top-right or bottom-left
        - Eliminate row or column each step
        - Iterative approach is simpler
        - This shows D&C thinking

        Example:
            >>> matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16]]
            >>> DivideConquerSolutions.search_2d_matrix_dc(matrix, 5)
            True
        """
        def search(top: int, left: int, bottom: int, right: int) -> bool:
            """Recursive search in submatrix."""
            if top > bottom or left > right:
                return False
            if target < matrix[top][left] or target > matrix[bottom][right]:
                return False

            # Choose middle column
            mid = (left + right) // 2

            # Binary search in middle column for row where target could be
            row = top
            while row <= bottom and matrix[row][mid] <= target:
                if matrix[row][mid] == target:
                    return True
                row += 1

            # Search in two quadrants
            # Bottom-left quadrant and top-right quadrant
            return (search(row, left, bottom, mid - 1) or
                    search(top, mid + 1, row - 1, right))

        if not matrix or not matrix[0]:
            return False

        return search(0, 0, len(matrix) - 1, len(matrix[0]) - 1)

    @staticmethod
    def sort_array_dc(nums: List[int]) -> List[int]:
        """
        Sort array using merge sort (classic divide and conquer).

        Difficulty: Medium
        Frequency: HIGH - Educational purpose

        Time Complexity: O(n log n) guaranteed
        Space Complexity: O(n)

        Interview Tips:
        - Merge sort is stable
        - Guaranteed O(n log n)
        - Good for linked lists (O(1) extra space)
        - Preferred when stability matters

        Example:
            >>> DivideConquerSolutions.sort_array_dc([5,2,3,1])
            [1, 2, 3, 5]
            >>> DivideConquerSolutions.sort_array_dc([5,1,1,2,0,0])
            [0, 0, 1, 1, 2, 5]
        """
        def merge(left: List[int], right: List[int]) -> List[int]:
            """Merge two sorted arrays."""
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            result.extend(left[i:])
            result.extend(right[j:])
            return result

        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = DivideConquerSolutions.sort_array_dc(nums[:mid])
        right = DivideConquerSolutions.sort_array_dc(nums[mid:])

        return merge(left, right)

    @staticmethod
    def inversion_count(nums: List[int]) -> int:
        """
        Count inversions: pairs (i, j) where i < j and nums[i] > nums[j].

        Difficulty: Hard
        Frequency: Medium - Amazon, Microsoft

        Time Complexity: O(n log n)
        Space Complexity: O(n)

        Interview Tips:
        - Brute force is O(n²)
        - Modified merge sort achieves O(n log n)
        - Count inversions during merge step
        - Similar to reverse pairs problem

        Example:
            >>> DivideConquerSolutions.inversion_count([2,4,1,3,5])
            3
            >>> DivideConquerSolutions.inversion_count([1,2,3,4,5])
            0
        """
        def merge_count(arr: List[int], temp: List[int], left: int, mid: int, right: int) -> int:
            """Merge and count inversions."""
            i = left
            j = mid + 1
            k = left
            inv_count = 0

            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp[k] = arr[i]
                    i += 1
                else:
                    temp[k] = arr[j]
                    # All remaining elements in left half are greater
                    inv_count += (mid - i + 1)
                    j += 1
                k += 1

            while i <= mid:
                temp[k] = arr[i]
                i += 1
                k += 1

            while j <= right:
                temp[k] = arr[j]
                j += 1
                k += 1

            # Copy back
            for i in range(left, right + 1):
                arr[i] = temp[i]

            return inv_count

        def merge_sort_count(arr: List[int], temp: List[int], left: int, right: int) -> int:
            """Recursively count inversions."""
            inv_count = 0
            if left < right:
                mid = (left + right) // 2

                inv_count += merge_sort_count(arr, temp, left, mid)
                inv_count += merge_sort_count(arr, temp, mid + 1, right)
                inv_count += merge_count(arr, temp, left, mid, right)

            return inv_count

        n = len(nums)
        temp = [0] * n
        arr_copy = nums.copy()
        return merge_sort_count(arr_copy, temp, 0, n - 1)
