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
