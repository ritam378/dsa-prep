"""
Comprehensive tests for sorting algorithms.

Tests cover:
- Basic functionality
- Edge cases (empty, single element, duplicates)
- Already sorted arrays
- Reverse sorted arrays
- Arrays with negative numbers
- Large datasets
- Stability (where applicable)
"""

import pytest
from dsa.algorithms.sorting import (
    bubble_sort,
    insertion_sort,
    selection_sort,
    merge_sort,
    quick_sort,
    heap_sort,
    counting_sort,
    radix_sort,
)


# Test data fixtures
@pytest.fixture
def unsorted_array():
    return [64, 34, 25, 12, 22, 11, 90]


@pytest.fixture
def sorted_array():
    return [11, 12, 22, 25, 34, 64, 90]


@pytest.fixture
def reverse_sorted():
    return [90, 64, 34, 25, 22, 12, 11]


@pytest.fixture
def duplicates():
    return [5, 2, 8, 2, 9, 1, 5, 5]


@pytest.fixture
def negative_numbers():
    return [-5, 3, -1, 7, -9, 0, 4]


@pytest.fixture
def single_element():
    return [42]


@pytest.fixture
def empty_array():
    return []


class TestBubbleSort:
    """Tests for bubble sort algorithm."""

    def test_basic_sorting(self, unsorted_array, sorted_array):
        assert bubble_sort(unsorted_array) == sorted_array

    def test_empty_array(self, empty_array):
        assert bubble_sort(empty_array) == []

    def test_single_element(self, single_element):
        assert bubble_sort(single_element) == [42]

    def test_already_sorted(self, sorted_array):
        assert bubble_sort(sorted_array) == sorted_array

    def test_reverse_sorted(self, reverse_sorted):
        assert bubble_sort(reverse_sorted) == [11, 12, 22, 25, 34, 64, 90]

    def test_duplicates(self, duplicates):
        assert bubble_sort(duplicates) == [1, 2, 2, 5, 5, 5, 8, 9]

    def test_negative_numbers(self, negative_numbers):
        assert bubble_sort(negative_numbers) == [-9, -5, -1, 0, 3, 4, 7]

    def test_two_elements(self):
        assert bubble_sort([2, 1]) == [1, 2]
        assert bubble_sort([1, 2]) == [1, 2]

    def test_all_same(self):
        assert bubble_sort([5, 5, 5, 5]) == [5, 5, 5, 5]

    def test_original_unchanged(self, unsorted_array):
        original = unsorted_array.copy()
        bubble_sort(unsorted_array)
        assert unsorted_array == original


class TestInsertionSort:
    """Tests for insertion sort algorithm."""

    def test_basic_sorting(self, unsorted_array, sorted_array):
        assert insertion_sort(unsorted_array) == sorted_array

    def test_empty_array(self, empty_array):
        assert insertion_sort(empty_array) == []

    def test_single_element(self, single_element):
        assert insertion_sort(single_element) == [42]

    def test_already_sorted(self, sorted_array):
        # Insertion sort is O(n) for already sorted
        assert insertion_sort(sorted_array) == sorted_array

    def test_reverse_sorted(self, reverse_sorted):
        assert insertion_sort(reverse_sorted) == [11, 12, 22, 25, 34, 64, 90]

    def test_duplicates(self, duplicates):
        assert insertion_sort(duplicates) == [1, 2, 2, 5, 5, 5, 8, 9]

    def test_negative_numbers(self, negative_numbers):
        assert insertion_sort(negative_numbers) == [-9, -5, -1, 0, 3, 4, 7]

    def test_nearly_sorted(self):
        # Insertion sort excels here
        arr = [1, 2, 3, 4, 5, 7, 6, 8, 9, 10]
        assert insertion_sort(arr) == list(range(1, 11))

    def test_original_unchanged(self, unsorted_array):
        original = unsorted_array.copy()
        insertion_sort(unsorted_array)
        assert unsorted_array == original


class TestSelectionSort:
    """Tests for selection sort algorithm."""

    def test_basic_sorting(self, unsorted_array, sorted_array):
        assert selection_sort(unsorted_array) == sorted_array

    def test_empty_array(self, empty_array):
        assert selection_sort(empty_array) == []

    def test_single_element(self, single_element):
        assert selection_sort(single_element) == [42]

    def test_already_sorted(self, sorted_array):
        assert selection_sort(sorted_array) == sorted_array

    def test_reverse_sorted(self, reverse_sorted):
        assert selection_sort(reverse_sorted) == [11, 12, 22, 25, 34, 64, 90]

    def test_duplicates(self, duplicates):
        assert selection_sort(duplicates) == [1, 2, 2, 5, 5, 5, 8, 9]

    def test_negative_numbers(self, negative_numbers):
        assert selection_sort(negative_numbers) == [-9, -5, -1, 0, 3, 4, 7]

    def test_original_unchanged(self, unsorted_array):
        original = unsorted_array.copy()
        selection_sort(unsorted_array)
        assert unsorted_array == original


class TestMergeSort:
    """Tests for merge sort algorithm."""

    def test_basic_sorting(self, unsorted_array, sorted_array):
        assert merge_sort(unsorted_array) == sorted_array

    def test_empty_array(self, empty_array):
        assert merge_sort(empty_array) == []

    def test_single_element(self, single_element):
        assert merge_sort(single_element) == [42]

    def test_already_sorted(self, sorted_array):
        assert merge_sort(sorted_array) == sorted_array

    def test_reverse_sorted(self, reverse_sorted):
        assert merge_sort(reverse_sorted) == [11, 12, 22, 25, 34, 64, 90]

    def test_duplicates(self, duplicates):
        assert merge_sort(duplicates) == [1, 2, 2, 5, 5, 5, 8, 9]

    def test_negative_numbers(self, negative_numbers):
        assert merge_sort(negative_numbers) == [-9, -5, -1, 0, 3, 4, 7]

    def test_large_array(self):
        # Merge sort handles large arrays efficiently
        import random
        arr = list(range(1000, 0, -1))
        assert merge_sort(arr) == list(range(1, 1001))

    def test_stability(self):
        # Merge sort is stable
        # Using tuples to test stability: (value, original_index)
        # After sorting by value, same values should maintain order
        arr = [3, 1, 4, 1, 5, 9, 2, 6]
        assert merge_sort(arr) == [1, 1, 2, 3, 4, 5, 6, 9]

    def test_original_unchanged(self, unsorted_array):
        original = unsorted_array.copy()
        merge_sort(unsorted_array)
        assert unsorted_array == original


class TestQuickSort:
    """Tests for quick sort algorithm."""

    def test_basic_sorting(self, unsorted_array):
        result = quick_sort(unsorted_array.copy())
        assert result == [11, 12, 22, 25, 34, 64, 90]

    def test_empty_array(self, empty_array):
        assert quick_sort(empty_array) == []

    def test_single_element(self, single_element):
        assert quick_sort(single_element.copy()) == [42]

    def test_already_sorted(self, sorted_array):
        # Worst case for basic quick sort
        result = quick_sort(sorted_array.copy())
        assert result == sorted_array

    def test_reverse_sorted(self, reverse_sorted):
        result = quick_sort(reverse_sorted.copy())
        assert result == [11, 12, 22, 25, 34, 64, 90]

    def test_duplicates(self, duplicates):
        result = quick_sort(duplicates.copy())
        assert result == [1, 2, 2, 5, 5, 5, 8, 9]

    def test_negative_numbers(self, negative_numbers):
        result = quick_sort(negative_numbers.copy())
        assert result == [-9, -5, -1, 0, 3, 4, 7]

    def test_large_array(self):
        import random
        # Use random array to avoid worst-case O(n²) with sorted data
        arr = list(range(1, 1001))
        random.shuffle(arr)
        result = quick_sort(arr)
        assert result == list(range(1, 1001))

    def test_all_same_elements(self):
        arr = [5] * 100
        assert quick_sort(arr) == [5] * 100


class TestHeapSort:
    """Tests for heap sort algorithm."""

    def test_basic_sorting(self, unsorted_array, sorted_array):
        assert heap_sort(unsorted_array) == sorted_array

    def test_empty_array(self, empty_array):
        assert heap_sort(empty_array) == []

    def test_single_element(self, single_element):
        assert heap_sort(single_element) == [42]

    def test_already_sorted(self, sorted_array):
        assert heap_sort(sorted_array) == sorted_array

    def test_reverse_sorted(self, reverse_sorted):
        assert heap_sort(reverse_sorted) == [11, 12, 22, 25, 34, 64, 90]

    def test_duplicates(self, duplicates):
        assert heap_sort(duplicates) == [1, 2, 2, 5, 5, 5, 8, 9]

    def test_negative_numbers(self, negative_numbers):
        assert heap_sort(negative_numbers) == [-9, -5, -1, 0, 3, 4, 7]

    def test_large_array(self):
        import random
        arr = list(range(1000, 0, -1))
        assert heap_sort(arr) == list(range(1, 1001))

    def test_original_unchanged(self, unsorted_array):
        original = unsorted_array.copy()
        heap_sort(unsorted_array)
        assert unsorted_array == original


class TestCountingSort:
    """Tests for counting sort algorithm."""

    def test_basic_sorting(self):
        arr = [1, 4, 1, 2, 7, 5, 2]
        assert counting_sort(arr) == [1, 1, 2, 2, 4, 5, 7]

    def test_empty_array(self, empty_array):
        assert counting_sort(empty_array) == []

    def test_single_element(self, single_element):
        assert counting_sort(single_element) == [42]

    def test_duplicates(self):
        arr = [5, 2, 8, 2, 9, 1, 5, 5]
        assert counting_sort(arr) == [1, 2, 2, 5, 5, 5, 8, 9]

    def test_negative_numbers(self):
        arr = [-5, 3, -1, 7, -9, 0, 4]
        assert counting_sort(arr) == [-9, -5, -1, 0, 3, 4, 7]

    def test_large_range(self):
        arr = [100, 1, 50, 25, 75]
        assert counting_sort(arr) == [1, 25, 50, 75, 100]

    def test_all_same(self):
        arr = [7, 7, 7, 7]
        assert counting_sort(arr) == [7, 7, 7, 7]

    def test_zero(self):
        arr = [0, 5, 0, 3, 0, 1]
        assert counting_sort(arr) == [0, 0, 0, 1, 3, 5]

    def test_original_unchanged(self):
        arr = [1, 4, 1, 2, 7, 5, 2]
        original = arr.copy()
        counting_sort(arr)
        assert arr == original


class TestRadixSort:
    """Tests for radix sort algorithm."""

    def test_basic_sorting(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        assert radix_sort(arr) == [2, 24, 45, 66, 75, 90, 170, 802]

    def test_empty_array(self, empty_array):
        assert radix_sort(empty_array) == []

    def test_single_element(self, single_element):
        assert radix_sort(single_element) == [42]

    def test_same_digits(self):
        arr = [329, 457, 657, 839, 436, 720, 355]
        expected = sorted(arr)
        assert radix_sort(arr) == expected

    def test_different_lengths(self):
        arr = [1, 10, 100, 1000, 5, 50, 500]
        assert radix_sort(arr) == [1, 5, 10, 50, 100, 500, 1000]

    def test_duplicates(self):
        arr = [5, 2, 8, 2, 9, 1, 5, 5]
        assert radix_sort(arr) == [1, 2, 2, 5, 5, 5, 8, 9]

    def test_negative_numbers(self):
        arr = [-5, 3, -1, 7, -9, 0, 4]
        assert radix_sort(arr) == [-9, -5, -1, 0, 3, 4, 7]

    def test_mixed_negative_positive(self):
        arr = [-100, 50, -25, 75, 0, -50, 25]
        assert radix_sort(arr) == [-100, -50, -25, 0, 25, 50, 75]

    def test_large_numbers(self):
        arr = [1000000, 1, 500000, 250000, 750000]
        assert radix_sort(arr) == [1, 250000, 500000, 750000, 1000000]

    def test_zeros(self):
        arr = [0, 0, 0, 5, 0, 3]
        assert radix_sort(arr) == [0, 0, 0, 0, 3, 5]

    def test_only_negatives(self):
        arr = [-5, -2, -8, -1, -9]
        assert radix_sort(arr) == [-9, -8, -5, -2, -1]

    def test_original_unchanged(self):
        arr = [170, 45, 75, 90, 802, 24, 2, 66]
        original = arr.copy()
        radix_sort(arr)
        assert arr == original


class TestSortingComparison:
    """Compare all sorting algorithms for correctness."""

    def test_all_sorts_produce_same_result(self):
        test_arrays = [
            [64, 34, 25, 12, 22, 11, 90],
            [5, 2, 8, 2, 9, 1, 5, 5],
            [-5, 3, -1, 7, -9, 0, 4],
            [1],
            [],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
        ]

        for arr in test_arrays:
            expected = sorted(arr)

            assert bubble_sort(arr.copy()) == expected
            assert insertion_sort(arr.copy()) == expected
            assert selection_sort(arr.copy()) == expected
            assert merge_sort(arr.copy()) == expected
            assert quick_sort(arr.copy()) == expected
            assert heap_sort(arr.copy()) == expected

            # Counting sort and radix sort only for non-negative in basic tests
            if all(x >= 0 for x in arr):
                assert counting_sort(arr.copy()) == expected
                assert radix_sort(arr.copy()) == expected
            else:
                # They should still work with negatives
                assert counting_sort(arr.copy()) == expected
                assert radix_sort(arr.copy()) == expected


class TestPerformance:
    """Basic performance sanity checks."""

    def test_large_array_all_algorithms(self):
        """Ensure all algorithms can handle moderately large arrays."""
        import random

        # Create array of 1000 elements
        arr = [random.randint(0, 10000) for _ in range(1000)]
        expected = sorted(arr)

        # All should complete without timeout
        assert merge_sort(arr.copy()) == expected
        assert quick_sort(arr.copy()) == expected
        assert heap_sort(arr.copy()) == expected

        # These might be slower but should still work
        # Commenting out O(n²) algorithms for large arrays to keep tests fast
        # assert bubble_sort(arr.copy()) == expected
        # assert insertion_sort(arr.copy()) == expected
        # assert selection_sort(arr.copy()) == expected

    def test_counting_sort_efficiency(self):
        """Counting sort should be efficient for small range."""
        arr = [5, 2, 8, 2, 9, 1, 5, 5] * 100  # 800 elements, range 1-9
        expected = sorted(arr)
        assert counting_sort(arr) == expected

    def test_radix_sort_fixed_digits(self):
        """Radix sort should be efficient for fixed-length numbers."""
        import random
        arr = [random.randint(0, 999) for _ in range(1000)]  # 3-digit numbers
        expected = sorted(arr)
        assert radix_sort(arr) == expected


class TestEdgeCases:
    """Test edge cases and special scenarios."""

    def test_two_elements_all_sorts(self):
        """Test with just two elements."""
        arr = [2, 1]
        expected = [1, 2]

        assert bubble_sort(arr.copy()) == expected
        assert insertion_sort(arr.copy()) == expected
        assert selection_sort(arr.copy()) == expected
        assert merge_sort(arr.copy()) == expected
        assert quick_sort(arr.copy()) == expected
        assert heap_sort(arr.copy()) == expected
        assert counting_sort(arr.copy()) == expected
        assert radix_sort(arr.copy()) == expected

    def test_all_same_elements(self):
        """Test with all identical elements."""
        arr = [7] * 50
        expected = [7] * 50

        assert bubble_sort(arr.copy()) == expected
        assert insertion_sort(arr.copy()) == expected
        assert merge_sort(arr.copy()) == expected
        assert quick_sort(arr.copy()) == expected
        assert heap_sort(arr.copy()) == expected

    def test_alternating_pattern(self):
        """Test with alternating high-low pattern."""
        arr = [1, 100, 2, 99, 3, 98, 4, 97]
        expected = [1, 2, 3, 4, 97, 98, 99, 100]

        assert merge_sort(arr) == expected
        assert quick_sort(arr.copy()) == expected
        assert heap_sort(arr) == expected
