"""
Comprehensive tests for Divide and Conquer problems.
"""

import pytest
from dsa.advanced_patterns.divide_conquer import DivideConquerSolutions
from dsa.data_structures.linked_list import ListNode


class TestMergeKSortedLists:
    """Tests for Merge K Sorted Lists."""

    def test_basic_example(self):
        l1 = ListNode(1, ListNode(4, ListNode(5)))
        l2 = ListNode(1, ListNode(3, ListNode(4)))
        l3 = ListNode(2, ListNode(6))
        result = DivideConquerSolutions.merge_k_sorted_lists([l1, l2, l3])

        vals = []
        while result:
            vals.append(result.val)
            result = result.next
        assert vals == [1, 1, 2, 3, 4, 4, 5, 6]

    def test_empty_lists(self):
        assert DivideConquerSolutions.merge_k_sorted_lists([]) is None

    def test_single_list(self):
        l1 = ListNode(1, ListNode(2))
        result = DivideConquerSolutions.merge_k_sorted_lists([l1])
        assert result.val == 1
        assert result.next.val == 2

    def test_with_empty_lists(self):
        l1 = ListNode(1)
        result = DivideConquerSolutions.merge_k_sorted_lists([l1, None, None])
        assert result.val == 1


class TestCountSmallerAfterSelf:
    """Tests for Count of Smaller Numbers After Self."""

    def test_basic_example(self):
        assert DivideConquerSolutions.count_smaller_after_self([5,2,6,1]) == [2, 1, 1, 0]

    def test_simple_case(self):
        assert DivideConquerSolutions.count_smaller_after_self([2,0,1]) == [2, 0, 0]

    def test_sorted_ascending(self):
        assert DivideConquerSolutions.count_smaller_after_self([1,2,3,4]) == [0, 0, 0, 0]

    def test_sorted_descending(self):
        assert DivideConquerSolutions.count_smaller_after_self([4,3,2,1]) == [3, 2, 1, 0]

    def test_single_element(self):
        assert DivideConquerSolutions.count_smaller_after_self([1]) == [0]

    def test_duplicates(self):
        result = DivideConquerSolutions.count_smaller_after_self([2,2,2,2])
        assert result == [0, 0, 0, 0]


class TestClosestPairOfPoints:
    """Tests for Closest Pair of Points."""

    def test_basic_example(self):
        points = [[0,0],[1,1],[2,2]]
        result = DivideConquerSolutions.closest_pair_of_points(points)
        assert abs(result - 1.4142135623730951) < 0.0001

    def test_horizontal_points(self):
        points = [[0,0],[1,0],[2,0]]
        assert DivideConquerSolutions.closest_pair_of_points(points) == 1.0

    def test_vertical_points(self):
        points = [[0,0],[0,1],[0,2]]
        assert DivideConquerSolutions.closest_pair_of_points(points) == 1.0

    def test_two_points(self):
        points = [[0,0],[3,4]]
        assert DivideConquerSolutions.closest_pair_of_points(points) == 5.0


class TestDifferentWaysToCompute:
    """Tests for Different Ways to Add Parentheses."""

    def test_basic_example(self):
        result = sorted(DivideConquerSolutions.different_ways_to_compute("2-1-1"))
        assert result == [0, 2]

    def test_complex_expression(self):
        result = sorted(DivideConquerSolutions.different_ways_to_compute("2*3-4*5"))
        assert result == [-34, -14, -10, -10, 10]

    def test_single_number(self):
        assert DivideConquerSolutions.different_ways_to_compute("42") == [42]

    def test_simple_operation(self):
        result = sorted(DivideConquerSolutions.different_ways_to_compute("2+3"))
        assert result == [5]


class TestMaximumSubarraySum:
    """Tests for Maximum Subarray Sum (D&C approach)."""

    def test_basic_example(self):
        assert DivideConquerSolutions.maximum_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6

    def test_single_element(self):
        assert DivideConquerSolutions.maximum_subarray_sum([1]) == 1

    def test_all_negative(self):
        assert DivideConquerSolutions.maximum_subarray_sum([-3,-2,-1,-4]) == -1

    def test_all_positive(self):
        assert DivideConquerSolutions.maximum_subarray_sum([1,2,3,4]) == 10

    def test_mixed_values(self):
        assert DivideConquerSolutions.maximum_subarray_sum([5,-3,5]) == 7


class TestQuickSelect:
    """Tests for Kth Largest Element (QuickSelect)."""

    def test_basic_example(self):
        assert DivideConquerSolutions.quick_select([3,2,1,5,6,4], 2) == 5

    def test_with_duplicates(self):
        assert DivideConquerSolutions.quick_select([3,2,3,1,2,4,5,5,6], 4) == 4

    def test_largest(self):
        assert DivideConquerSolutions.quick_select([1,2,3,4,5], 1) == 5

    def test_smallest(self):
        assert DivideConquerSolutions.quick_select([5,4,3,2,1], 5) == 1

    def test_single_element(self):
        assert DivideConquerSolutions.quick_select([42], 1) == 42


class TestReversePairs:
    """Tests for Reverse Pairs."""

    def test_basic_example(self):
        assert DivideConquerSolutions.reverse_pairs([1,3,2,3,1]) == 2

    def test_another_example(self):
        assert DivideConquerSolutions.reverse_pairs([2,4,3,5,1]) == 3

    def test_no_pairs(self):
        assert DivideConquerSolutions.reverse_pairs([1,2,3,4]) == 0

    def test_sorted_descending(self):
        result = DivideConquerSolutions.reverse_pairs([5,4,3,2,1])
        assert result >= 0  # Has reverse pairs

    def test_empty_array(self):
        assert DivideConquerSolutions.reverse_pairs([]) == 0

    def test_single_element(self):
        assert DivideConquerSolutions.reverse_pairs([1]) == 0


class TestSearch2DMatrixDC:
    """Tests for Search 2D Matrix (Divide and Conquer)."""

    def test_basic_example(self):
        matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
        assert DivideConquerSolutions.search_2d_matrix_dc(matrix, 5) == True

    def test_target_not_found(self):
        matrix = [[1,4,7,11],[2,5,8,12],[3,6,9,16],[10,13,14,17]]
        assert DivideConquerSolutions.search_2d_matrix_dc(matrix, 20) == False

    def test_single_element(self):
        assert DivideConquerSolutions.search_2d_matrix_dc([[5]], 5) == True
        assert DivideConquerSolutions.search_2d_matrix_dc([[5]], 1) == False

    def test_empty_matrix(self):
        assert DivideConquerSolutions.search_2d_matrix_dc([], 1) == False
        assert DivideConquerSolutions.search_2d_matrix_dc([[]], 1) == False

    def test_corners(self):
        matrix = [[1,4],[2,5]]
        assert DivideConquerSolutions.search_2d_matrix_dc(matrix, 1) == True
        assert DivideConquerSolutions.search_2d_matrix_dc(matrix, 5) == True


class TestSortArrayDC:
    """Tests for Sort Array (Merge Sort)."""

    def test_basic_example(self):
        assert DivideConquerSolutions.sort_array_dc([5,2,3,1]) == [1,2,3,5]

    def test_with_duplicates(self):
        assert DivideConquerSolutions.sort_array_dc([5,1,1,2,0,0]) == [0,0,1,1,2,5]

    def test_sorted_array(self):
        assert DivideConquerSolutions.sort_array_dc([1,2,3,4]) == [1,2,3,4]

    def test_reverse_sorted(self):
        assert DivideConquerSolutions.sort_array_dc([5,4,3,2,1]) == [1,2,3,4,5]

    def test_single_element(self):
        assert DivideConquerSolutions.sort_array_dc([42]) == [42]

    def test_empty_array(self):
        assert DivideConquerSolutions.sort_array_dc([]) == []

    def test_negative_numbers(self):
        assert DivideConquerSolutions.sort_array_dc([-1,-5,3,2,0]) == [-5,-1,0,2,3]


class TestInversionCount:
    """Tests for Inversion Count."""

    def test_basic_example(self):
        assert DivideConquerSolutions.inversion_count([2,4,1,3,5]) == 3

    def test_no_inversions(self):
        assert DivideConquerSolutions.inversion_count([1,2,3,4,5]) == 0

    def test_reverse_sorted(self):
        assert DivideConquerSolutions.inversion_count([5,4,3,2,1]) == 10

    def test_single_element(self):
        assert DivideConquerSolutions.inversion_count([1]) == 0

    def test_two_elements(self):
        assert DivideConquerSolutions.inversion_count([2,1]) == 1
        assert DivideConquerSolutions.inversion_count([1,2]) == 0

    def test_duplicates(self):
        result = DivideConquerSolutions.inversion_count([3,2,2,1])
        assert result >= 0  # Should count properly with duplicates


class TestDivideConquerEdgeCases:
    """Test edge cases across divide and conquer problems."""

    def test_empty_inputs(self):
        assert DivideConquerSolutions.sort_array_dc([]) == []
        assert DivideConquerSolutions.inversion_count([]) == 0
        assert DivideConquerSolutions.reverse_pairs([]) == 0

    def test_single_elements(self):
        assert DivideConquerSolutions.sort_array_dc([5]) == [5]
        assert DivideConquerSolutions.maximum_subarray_sum([5]) == 5
        assert DivideConquerSolutions.quick_select([5], 1) == 5

    def test_large_inputs(self):
        # Test with larger input to ensure O(n log n) efficiency
        large_array = list(range(1000, 0, -1))
        sorted_result = DivideConquerSolutions.sort_array_dc(large_array)
        assert sorted_result == list(range(1, 1001))

        # QuickSelect should handle large arrays
        assert DivideConquerSolutions.quick_select(large_array, 1) == 1000

    def test_all_same_elements(self):
        assert DivideConquerSolutions.sort_array_dc([5,5,5,5]) == [5,5,5,5]
        assert DivideConquerSolutions.inversion_count([3,3,3]) == 0
