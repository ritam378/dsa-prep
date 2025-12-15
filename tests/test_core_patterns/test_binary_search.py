"""
Tests for Binary Search pattern.
"""

import pytest
from dsa.core_patterns.binary_search import BinarySearchSolutions


class TestBinarySearchSolutions:
    """Test cases for binary search pattern."""

    def test_binary_search(self):
        """Test standard binary search."""
        assert BinarySearchSolutions.binary_search([1, 2, 3, 4, 5], 3) == 2
        assert BinarySearchSolutions.binary_search([1, 2, 3, 4, 5], 6) == -1
        assert BinarySearchSolutions.binary_search([], 1) == -1

    def test_find_first_occurrence(self):
        """Test finding first occurrence."""
        assert BinarySearchSolutions.find_first_occurrence([1, 2, 2, 2, 3], 2) == 1
        assert BinarySearchSolutions.find_first_occurrence([1, 2, 3, 4, 5], 6) == -1

    def test_find_last_occurrence(self):
        """Test finding last occurrence."""
        assert BinarySearchSolutions.find_last_occurrence([1, 2, 2, 2, 3], 2) == 3
        assert BinarySearchSolutions.find_last_occurrence([1, 2, 3, 4, 5], 6) == -1

    def test_search_rotated_sorted_array(self):
        """Test search in rotated sorted array."""
        assert BinarySearchSolutions.search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 0) == 4
        assert BinarySearchSolutions.search_rotated_sorted_array([4, 5, 6, 7, 0, 1, 2], 3) == -1

    def test_find_minimum_rotated_array(self):
        """Test finding minimum in rotated array."""
        assert BinarySearchSolutions.find_minimum_rotated_array([3, 4, 5, 1, 2]) == 1
        assert BinarySearchSolutions.find_minimum_rotated_array([4, 5, 6, 7, 0, 1, 2]) == 0

    def test_sqrt(self):
        """Test integer square root."""
        assert BinarySearchSolutions.sqrt(4) == 2
        assert BinarySearchSolutions.sqrt(8) == 2
        assert BinarySearchSolutions.sqrt(1) == 1

    def test_find_peak_element(self):
        """Test finding peak element."""
        result = BinarySearchSolutions.find_peak_element([1, 2, 3, 1])
        assert result == 2


class TestSearchRange:
    """Tests for Find First and Last Position problem."""

    def test_basic_example(self):
        assert BinarySearchSolutions.search_range([5,7,7,8,8,10], 8) == [3, 4]

    def test_target_not_found(self):
        assert BinarySearchSolutions.search_range([5,7,7,8,8,10], 6) == [-1, -1]

    def test_single_element_found(self):
        assert BinarySearchSolutions.search_range([1], 1) == [0, 0]

    def test_single_element_not_found(self):
        assert BinarySearchSolutions.search_range([1], 2) == [-1, -1]

    def test_empty_array(self):
        assert BinarySearchSolutions.search_range([], 0) == [-1, -1]

    def test_all_same_elements(self):
        assert BinarySearchSolutions.search_range([2,2,2,2,2], 2) == [0, 4]

    def test_target_at_boundaries(self):
        assert BinarySearchSolutions.search_range([1,2,3], 1) == [0, 0]
        assert BinarySearchSolutions.search_range([1,2,3], 3) == [2, 2]


class TestSearchMatrix:
    """Tests for Search 2D Matrix problem."""

    def test_basic_example(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        assert BinarySearchSolutions.search_matrix(matrix, 3) == True

    def test_target_not_found(self):
        matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
        assert BinarySearchSolutions.search_matrix(matrix, 13) == False

    def test_single_element(self):
        assert BinarySearchSolutions.search_matrix([[5]], 5) == True
        assert BinarySearchSolutions.search_matrix([[5]], 1) == False

    def test_empty_matrix(self):
        assert BinarySearchSolutions.search_matrix([], 1) == False
        assert BinarySearchSolutions.search_matrix([[]], 1) == False

    def test_first_element(self):
        matrix = [[1,3,5,7],[10,11,16,20]]
        assert BinarySearchSolutions.search_matrix(matrix, 1) == True

    def test_last_element(self):
        matrix = [[1,3,5,7],[10,11,16,20]]
        assert BinarySearchSolutions.search_matrix(matrix, 20) == True

    def test_single_row(self):
        assert BinarySearchSolutions.search_matrix([[1,3,5,7]], 5) == True

    def test_single_column(self):
        assert BinarySearchSolutions.search_matrix([[1],[3],[5],[7]], 5) == True


class TestSearchMatrixII:
    """Tests for Search 2D Matrix II problem."""

    def test_basic_example(self):
        matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
        assert BinarySearchSolutions.search_matrix_ii(matrix, 5) == True

    def test_target_not_found(self):
        matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
        assert BinarySearchSolutions.search_matrix_ii(matrix, 20) == False

    def test_single_element(self):
        assert BinarySearchSolutions.search_matrix_ii([[5]], 5) == True
        assert BinarySearchSolutions.search_matrix_ii([[5]], 1) == False

    def test_empty_matrix(self):
        assert BinarySearchSolutions.search_matrix_ii([], 1) == False
        assert BinarySearchSolutions.search_matrix_ii([[]], 1) == False

    def test_first_element(self):
        matrix = [[1,4],[2,5]]
        assert BinarySearchSolutions.search_matrix_ii(matrix, 1) == True

    def test_last_element(self):
        matrix = [[1,4],[2,5]]
        assert BinarySearchSolutions.search_matrix_ii(matrix, 5) == True

    def test_diagonal(self):
        matrix = [[1,2,3],[4,5,6],[7,8,9]]
        assert BinarySearchSolutions.search_matrix_ii(matrix, 5) == True


class TestFirstBadVersion:
    """Tests for First Bad Version problem."""

    def test_basic_example(self):
        def is_bad(v): return v >= 4
        assert BinarySearchSolutions.first_bad_version(5, is_bad) == 4

    def test_all_bad(self):
        def is_bad(v): return True
        assert BinarySearchSolutions.first_bad_version(10, is_bad) == 1

    def test_last_bad(self):
        def is_bad(v): return v >= 100
        assert BinarySearchSolutions.first_bad_version(100, is_bad) == 100

    def test_single_version(self):
        def is_bad(v): return True
        assert BinarySearchSolutions.first_bad_version(1, is_bad) == 1

    def test_large_n(self):
        def is_bad(v): return v >= 1000000
        assert BinarySearchSolutions.first_bad_version(2000000, is_bad) == 1000000


class TestKokoEatingBananas:
    """Tests for Koko Eating Bananas problem."""

    def test_basic_example(self):
        assert BinarySearchSolutions.koko_eating_bananas([3,6,7,11], 8) == 4

    def test_minimum_hours(self):
        assert BinarySearchSolutions.koko_eating_bananas([30,11,23,4,20], 5) == 30

    def test_single_pile(self):
        assert BinarySearchSolutions.koko_eating_bananas([1000000000], 2) == 500000000

    def test_more_hours_than_piles(self):
        assert BinarySearchSolutions.koko_eating_bananas([3,6,7,11], 100) == 1

    def test_exact_hours(self):
        assert BinarySearchSolutions.koko_eating_bananas([10,10,10], 3) == 10

    def test_need_max_speed(self):
        assert BinarySearchSolutions.koko_eating_bananas([10,10,10,10], 4) == 10


class TestFindMinRotatedWithDuplicates:
    """Tests for Find Min in Rotated Array with Duplicates."""

    def test_basic_example(self):
        assert BinarySearchSolutions.find_min_rotated_with_duplicates([2,2,2,0,1]) == 0

    def test_no_rotation(self):
        assert BinarySearchSolutions.find_min_rotated_with_duplicates([1,3,5]) == 1

    def test_all_duplicates(self):
        assert BinarySearchSolutions.find_min_rotated_with_duplicates([1,1,1,1]) == 1

    def test_worst_case(self):
        # O(n) worst case
        assert BinarySearchSolutions.find_min_rotated_with_duplicates([1,1,1,0,1]) == 0

    def test_single_element(self):
        assert BinarySearchSolutions.find_min_rotated_with_duplicates([5]) == 5

    def test_two_elements(self):
        assert BinarySearchSolutions.find_min_rotated_with_duplicates([2,1]) == 1
        assert BinarySearchSolutions.find_min_rotated_with_duplicates([1,2]) == 1

    def test_duplicates_at_pivot(self):
        assert BinarySearchSolutions.find_min_rotated_with_duplicates([3,3,1,3]) == 1


class TestSingleNonDuplicate:
    """Tests for Single Element in Sorted Array."""

    def test_basic_example(self):
        assert BinarySearchSolutions.single_non_duplicate([1,1,2,3,3,4,4,8,8]) == 2

    def test_single_at_end(self):
        assert BinarySearchSolutions.single_non_duplicate([3,3,7,7,10,11,11]) == 10

    def test_single_at_beginning(self):
        assert BinarySearchSolutions.single_non_duplicate([1,2,2,3,3,4,4]) == 1

    def test_single_at_actual_end(self):
        assert BinarySearchSolutions.single_non_duplicate([1,1,2,2,3]) == 3

    def test_three_elements(self):
        assert BinarySearchSolutions.single_non_duplicate([1,1,2]) == 2
        assert BinarySearchSolutions.single_non_duplicate([1,2,2]) == 1

    def test_single_element_only(self):
        assert BinarySearchSolutions.single_non_duplicate([1]) == 1


class TestNextGreatestLetter:
    """Tests for Find Smallest Letter Greater Than Target."""

    def test_basic_examples(self):
        assert BinarySearchSolutions.next_greatest_letter(['c','f','j'], 'a') == 'c'
        assert BinarySearchSolutions.next_greatest_letter(['c','f','j'], 'c') == 'f'

    def test_wrap_around(self):
        assert BinarySearchSolutions.next_greatest_letter(['c','f','j'], 'k') == 'c'
        assert BinarySearchSolutions.next_greatest_letter(['c','f','j'], 'z') == 'c'

    def test_target_equals_last(self):
        assert BinarySearchSolutions.next_greatest_letter(['c','f','j'], 'j') == 'c'

    def test_single_letter(self):
        assert BinarySearchSolutions.next_greatest_letter(['a'], 'z') == 'a'

    def test_duplicates(self):
        assert BinarySearchSolutions.next_greatest_letter(['a','b','b','b','c'], 'b') == 'c'

    def test_all_same(self):
        assert BinarySearchSolutions.next_greatest_letter(['a','a','a'], 'a') == 'a'


class TestSearchInsertPosition:
    """Tests for Search Insert Position."""

    def test_basic_examples(self):
        assert BinarySearchSolutions.search_insert_position([1,3,5,6], 5) == 2
        assert BinarySearchSolutions.search_insert_position([1,3,5,6], 2) == 1
        assert BinarySearchSolutions.search_insert_position([1,3,5,6], 7) == 4

    def test_insert_at_beginning(self):
        assert BinarySearchSolutions.search_insert_position([1,3,5,6], 0) == 0

    def test_empty_array(self):
        assert BinarySearchSolutions.search_insert_position([], 5) == 0

    def test_single_element(self):
        assert BinarySearchSolutions.search_insert_position([5], 3) == 0
        assert BinarySearchSolutions.search_insert_position([5], 7) == 1
        assert BinarySearchSolutions.search_insert_position([5], 5) == 0

    def test_target_exists(self):
        assert BinarySearchSolutions.search_insert_position([1,3,5,6], 3) == 1

    def test_duplicates(self):
        assert BinarySearchSolutions.search_insert_position([1,3,3,3,5], 3) in [1, 2, 3]


class TestFindMedianSortedArrays:
    """Tests for Median of Two Sorted Arrays."""

    def test_basic_examples(self):
        assert BinarySearchSolutions.find_median_sorted_arrays([1,3], [2]) == 2.0
        assert BinarySearchSolutions.find_median_sorted_arrays([1,2], [3,4]) == 2.5

    def test_empty_arrays(self):
        assert BinarySearchSolutions.find_median_sorted_arrays([], [1]) == 1.0
        assert BinarySearchSolutions.find_median_sorted_arrays([2], []) == 2.0

    def test_different_sizes(self):
        assert BinarySearchSolutions.find_median_sorted_arrays([1,2,3,4,5], [6,7,8]) == 4.5

    def test_single_elements(self):
        assert BinarySearchSolutions.find_median_sorted_arrays([1], [2]) == 1.5

    def test_all_in_first_array(self):
        assert BinarySearchSolutions.find_median_sorted_arrays([1,2,3], [4,5,6]) == 3.5

    def test_interleaved(self):
        assert BinarySearchSolutions.find_median_sorted_arrays([1,3,5], [2,4,6]) == 3.5

    def test_duplicates(self):
        assert BinarySearchSolutions.find_median_sorted_arrays([1,1,1], [1,1,1]) == 1.0

    def test_negative_numbers(self):
        assert BinarySearchSolutions.find_median_sorted_arrays([-5,-3,-1], [0,2,4]) == -0.5

    def test_large_difference(self):
        assert BinarySearchSolutions.find_median_sorted_arrays([1,2], [100,101,102]) == 100.0


class TestBinarySearchEdgeCases:
    """Test edge cases across binary search problems."""

    def test_empty_inputs(self):
        assert BinarySearchSolutions.binary_search([], 1) == -1
        assert BinarySearchSolutions.search_range([], 1) == [-1, -1]

    def test_single_elements(self):
        assert BinarySearchSolutions.binary_search([5], 5) == 0
        assert BinarySearchSolutions.sqrt(0) == 0
        assert BinarySearchSolutions.sqrt(1) == 1

    def test_large_numbers(self):
        # Test with large numbers to ensure no overflow
        assert BinarySearchSolutions.sqrt(2147395599) == 46339

    def test_performance(self):
        # Test with large arrays
        large_array = list(range(1000000))
        assert BinarySearchSolutions.binary_search(large_array, 999999) == 999999
        assert BinarySearchSolutions.binary_search(large_array, 500000) == 500000
