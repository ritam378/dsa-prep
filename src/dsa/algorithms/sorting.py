"""
Sorting Algorithms

This module contains implementations of fundamental sorting algorithms commonly asked
in technical interviews. Each algorithm includes detailed documentation on time/space
complexity, use cases, and implementation details.

INTERVIEW TIPS:
- Know when to use which sorting algorithm based on constraints
- Understand stability: maintains relative order of equal elements
- Recognize when in-place sorting is required (space constraint)
- Be able to explain tradeoffs between algorithms
- Quick Sort and Merge Sort are most commonly asked
- Counting Sort and Radix Sort for special cases (integers, limited range)

COMPLEXITY COMPARISON:
Algorithm        | Best Case | Average   | Worst Case | Space  | Stable | In-Place
-----------------------------------------------------------------------------
Bubble Sort      | O(n)      | O(n²)     | O(n²)      | O(1)   | Yes    | Yes
Insertion Sort   | O(n)      | O(n²)     | O(n²)      | O(1)   | Yes    | Yes
Selection Sort   | O(n²)     | O(n²)     | O(n²)      | O(1)   | No     | Yes
Merge Sort       | O(n log n)| O(n log n)| O(n log n) | O(n)   | Yes    | No
Quick Sort       | O(n log n)| O(n log n)| O(n²)      | O(log n)| No    | Yes
Heap Sort        | O(n log n)| O(n log n)| O(n log n) | O(1)   | No     | Yes
Counting Sort    | O(n+k)    | O(n+k)    | O(n+k)     | O(k)   | Yes    | No
Radix Sort       | O(d*n)    | O(d*n)    | O(d*n)     | O(n+k) | Yes    | No
"""

from typing import List


def bubble_sort(arr: List[int]) -> List[int]:
    """
    Bubble Sort - Repeatedly swap adjacent elements if they're in wrong order.

    Algorithm:
    1. Compare adjacent elements
    2. Swap if they're in wrong order
    3. Repeat until no swaps needed

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n²) average and worst case, O(n) best case (already sorted)
    Space Complexity: O(1) - in-place sorting

    Difficulty: Easy
    Interview Frequency: Low (mainly asked to explain why it's inefficient)
    Companies: Entry-level interviews
    Estimated Time: 10-15 minutes

    Example:
        >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
        [11, 12, 22, 25, 34, 64, 90]

    Interview Tips:
    - Mention optimization: stop if no swaps in a pass
    - Good for nearly sorted data
    - Easy to implement but inefficient for large datasets
    """
    n = len(arr)
    result = arr.copy()

    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # Optimization: if no swaps, array is sorted
        if not swapped:
            break

    return result


def insertion_sort(arr: List[int]) -> List[int]:
    """
    Insertion Sort - Build sorted array one element at a time by inserting elements
    into their correct position.

    Algorithm:
    1. Iterate from arr[1] to arr[n]
    2. For each element, find its correct position in sorted part
    3. Shift elements to make space and insert

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n²) average and worst case, O(n) best case
    Space Complexity: O(1) - in-place sorting

    Difficulty: Easy
    Interview Frequency: Medium (often asked for small datasets or nearly sorted data)
    Companies: Google, Amazon, Microsoft
    Estimated Time: 10-15 minutes

    Example:
        >>> insertion_sort([12, 11, 13, 5, 6])
        [5, 6, 11, 12, 13]

    Interview Tips:
    - Excellent for small datasets or nearly sorted data
    - Stable sort (maintains relative order)
    - Online algorithm (can sort as data comes in)
    - Used in hybrid sorting algorithms (Timsort uses insertion for small subarrays)
    """
    result = arr.copy()

    for i in range(1, len(result)):
        key = result[i]
        j = i - 1

        # Move elements greater than key one position ahead
        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key

    return result


def selection_sort(arr: List[int]) -> List[int]:
    """
    Selection Sort - Repeatedly find minimum element and place it at the beginning.

    Algorithm:
    1. Find minimum element in unsorted portion
    2. Swap with first unsorted element
    3. Move boundary of sorted portion

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n²) in all cases
    Space Complexity: O(1) - in-place sorting

    Difficulty: Easy
    Interview Frequency: Low
    Companies: Entry-level interviews
    Estimated Time: 10-15 minutes

    Example:
        >>> selection_sort([64, 25, 12, 22, 11])
        [11, 12, 22, 25, 64]

    Interview Tips:
    - Makes minimum number of swaps (n-1)
    - Not stable by default
    - Good when write operations are expensive
    - Never makes more than O(n) swaps
    """
    result = arr.copy()
    n = len(result)

    for i in range(n):
        # Find minimum in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if result[j] < result[min_idx]:
                min_idx = j

        # Swap minimum with first unsorted element
        result[i], result[min_idx] = result[min_idx], result[i]

    return result


def merge_sort(arr: List[int]) -> List[int]:
    """
    Merge Sort - Divide and conquer algorithm that divides array into halves,
    sorts them, and merges them back.

    Algorithm:
    1. Divide array into two halves
    2. Recursively sort each half
    3. Merge sorted halves

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n log n) in all cases
    Space Complexity: O(n) - requires auxiliary space for merging

    Difficulty: Medium
    Interview Frequency: HIGH - One of most commonly asked sorting algorithms
    Companies: Google, Facebook, Amazon, Microsoft, Apple
    Estimated Time: 20-30 minutes

    Example:
        >>> merge_sort([38, 27, 43, 3, 9, 82, 10])
        [3, 9, 10, 27, 38, 43, 82]

    Interview Tips:
    - Stable sort - maintains relative order
    - Guaranteed O(n log n) performance
    - Good for linked lists (no random access needed)
    - Used in external sorting (when data doesn't fit in memory)
    - Discuss space-time tradeoff with interviewer
    - Can be implemented iteratively or recursively
    """
    if len(arr) <= 1:
        return arr

    # Divide
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Conquer (merge)
    return _merge(left, right)


def _merge(left: List[int], right: List[int]) -> List[int]:
    """Helper function to merge two sorted arrays."""
    result = []
    i = j = 0

    # Merge elements in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(arr: List[int]) -> List[int]:
    """
    Quick Sort - Divide and conquer algorithm that picks a pivot and partitions
    array around it.

    Algorithm:
    1. Choose a pivot element
    2. Partition: elements smaller than pivot go left, larger go right
    3. Recursively sort left and right partitions

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n log n) average, O(n²) worst case
    Space Complexity: O(log n) for recursion stack

    Difficulty: Medium
    Interview Frequency: HIGH - Most commonly asked sorting algorithm
    Companies: Google, Facebook, Amazon, Microsoft, Apple, Netflix
    Estimated Time: 25-35 minutes

    Example:
        >>> quick_sort([10, 7, 8, 9, 1, 5])
        [1, 5, 7, 8, 9, 10]

    Interview Tips:
    - Discuss pivot selection strategies (first, last, median, random)
    - Mention worst case: already sorted with poor pivot choice
    - In-place sorting (better space complexity than merge sort)
    - Not stable by default
    - Preferred for arrays (cache-friendly)
    - Can be optimized with 3-way partitioning for duplicates
    - Discuss when to switch to insertion sort for small subarrays
    """
    if len(arr) <= 1:
        return arr

    result = arr.copy()
    return _quick_sort_helper(result, 0, len(result) - 1)


def _quick_sort_helper(arr: List[int], low: int, high: int) -> List[int]:
    """Helper function for quick sort."""
    if low < high:
        # Partition and get pivot index
        pivot_idx = _partition(arr, low, high)

        # Recursively sort left and right partitions
        _quick_sort_helper(arr, low, pivot_idx - 1)
        _quick_sort_helper(arr, pivot_idx + 1, high)

    return arr


def _partition(arr: List[int], low: int, high: int) -> int:
    """Partition helper using last element as pivot."""
    pivot = arr[high]
    i = low - 1  # Index of smaller element

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def heap_sort(arr: List[int]) -> List[int]:
    """
    Heap Sort - Uses binary heap data structure to sort elements.

    Algorithm:
    1. Build max heap from input array
    2. Repeatedly extract maximum (root) and rebuild heap
    3. Place extracted elements at end of array

    Args:
        arr: List of integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n log n) in all cases
    Space Complexity: O(1) - in-place sorting

    Difficulty: Medium-Hard
    Interview Frequency: Medium
    Companies: Google, Amazon, Microsoft
    Estimated Time: 30-40 minutes

    Example:
        >>> heap_sort([12, 11, 13, 5, 6, 7])
        [5, 6, 7, 11, 12, 13]

    Interview Tips:
    - In-place with O(1) space (unlike merge sort)
    - Guaranteed O(n log n) (unlike quick sort)
    - Not stable
    - Good when memory is limited
    - Slower in practice than quick sort due to cache behavior
    - Build heap is O(n), not O(n log n)
    """
    result = arr.copy()
    n = len(result)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        _heapify(result, n, i)

    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end
        result[0], result[i] = result[i], result[0]

        # Heapify reduced heap
        _heapify(result, i, 0)

    return result


def _heapify(arr: List[int], n: int, i: int) -> None:
    """Heapify subtree rooted at index i."""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Check if left child exists and is greater
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # Recursively heapify affected subtree
        _heapify(arr, n, largest)


def counting_sort(arr: List[int]) -> List[int]:
    """
    Counting Sort - Integer sorting algorithm using counting array.
    Works for non-negative integers within a known range.

    Algorithm:
    1. Find range of input (min to max)
    2. Count occurrences of each value
    3. Calculate cumulative counts
    4. Place elements in output array using counts

    Args:
        arr: List of non-negative integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(n + k) where k is range of input
    Space Complexity: O(k) for counting array

    Difficulty: Medium
    Interview Frequency: Medium (for special cases)
    Companies: Google, Facebook, Amazon
    Estimated Time: 20-25 minutes

    Example:
        >>> counting_sort([1, 4, 1, 2, 7, 5, 2])
        [1, 1, 2, 2, 4, 5, 7]

    Interview Tips:
    - Linear time when k = O(n)
    - Stable sort
    - Not comparison-based
    - Requires knowing range of values
    - Good when range is not significantly larger than n
    - Can be modified for negative numbers (offset by min value)
    - Used as subroutine in radix sort

    Limitations:
    - Only works for integers (or can be mapped to integers)
    - Inefficient when range >> n
    """
    if not arr:
        return arr

    # Handle negative numbers by offsetting
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1

    # Count occurrences
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1

    # Build output array
    result = []
    for i in range(range_size):
        result.extend([i + min_val] * count[i])

    return result


def radix_sort(arr: List[int]) -> List[int]:
    """
    Radix Sort - Non-comparison based sorting using digit-by-digit sorting.
    Sorts numbers by processing individual digits.

    Algorithm:
    1. Find maximum number to determine number of digits
    2. Sort by each digit position (starting from least significant)
    3. Use counting sort as subroutine for each digit

    Args:
        arr: List of non-negative integers to sort

    Returns:
        Sorted list in ascending order

    Time Complexity: O(d * n) where d is number of digits
    Space Complexity: O(n + k) where k is range of digits (usually 10)

    Difficulty: Medium-Hard
    Interview Frequency: Low-Medium
    Companies: Google, Facebook
    Estimated Time: 30-40 minutes

    Example:
        >>> radix_sort([170, 45, 75, 90, 802, 24, 2, 66])
        [2, 24, 45, 66, 75, 90, 170, 802]

    Interview Tips:
    - Linear time when d is constant
    - Stable sort
    - Not comparison-based
    - Good for integers with fixed number of digits
    - Can sort strings lexicographically
    - Used in suffix array construction
    - Discuss LSD (least significant digit) vs MSD (most significant digit)

    Variations:
    - LSD (Least Significant Digit): stable, simpler
    - MSD (Most Significant Digit): can stop early, harder to implement
    """
    if not arr:
        return arr

    # Handle negative numbers (separate, sort, merge)
    negatives = [x for x in arr if x < 0]
    positives = [x for x in arr if x >= 0]

    # Sort negatives separately by their absolute value
    if negatives:
        neg_abs = [-x for x in negatives]
        max_neg = max(neg_abs)
        exp = 1
        while max_neg // exp > 0:
            neg_abs = _counting_sort_by_digit(neg_abs, exp)
            exp *= 10
        # Convert back to negative and reverse
        negatives = [-x for x in reversed(neg_abs)]

    if not positives:
        return negatives

    # Find maximum to determine number of digits
    max_val = max(positives)

    # Sort by each digit position
    exp = 1  # 10^0, 10^1, 10^2, ...
    while max_val // exp > 0:
        positives = _counting_sort_by_digit(positives, exp)
        exp *= 10

    # Merge negatives and positives
    return negatives + positives


def _counting_sort_by_digit(arr: List[int], exp: int) -> List[int]:
    """
    Counting sort used as subroutine for radix sort.
    Sorts based on digit at position exp.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Digits 0-9

    # Count occurrences of digits
    for num in arr:
        digit = (num // exp) % 10
        count[digit] += 1

    # Calculate cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (traverse backwards for stability)
    for i in range(n - 1, -1, -1):
        digit = (arr[i] // exp) % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1

    return output


# Interview Quick Reference
SORTING_CHEATSHEET = """
WHEN TO USE WHICH SORTING ALGORITHM:

1. QUICK SORT: Default choice for arrays
   - Fast in practice
   - In-place
   - Watch for already sorted input (worst case)

2. MERGE SORT: When stability matters or for linked lists
   - Guaranteed O(n log n)
   - Stable
   - Good for external sorting

3. HEAP SORT: When memory is limited
   - In-place
   - Guaranteed O(n log n)
   - Slower than quick/merge in practice

4. INSERTION SORT: Small datasets or nearly sorted
   - Simple implementation
   - O(n) for nearly sorted
   - Used in hybrid algorithms

5. COUNTING SORT: Integer sorting with small range
   - Linear time when k = O(n)
   - Stable
   - Limited to integers

6. RADIX SORT: Fixed-length integers
   - Linear time when d is small
   - Stable
   - Good for sorting strings

INTERVIEW QUESTIONS TO EXPECT:
- Why is quick sort faster than merge sort in practice? (Cache locality)
- When would you use merge sort over quick sort? (Stability, linked lists)
- Can you make quick sort stable? (Yes, but complex)
- What's the fastest way to sort? (Depends on constraints)
- How would you sort 1 million 32-bit integers? (Radix sort)
- Sort an almost sorted array? (Insertion sort)
"""
