"""
Tests for Two Pointer pattern.
"""

import pytest
from dsa.core_patterns.two_pointer import TwoPointerSolutions


class TestTwoPointerSolutions:
    """Test cases for two pointer pattern."""

    def test_two_sum_sorted(self):
        """Test two sum in sorted array."""
        assert TwoPointerSolutions.two_sum_sorted([2, 7, 11, 15], 9) == [0, 1]
        assert TwoPointerSolutions.two_sum_sorted([2, 3, 4], 6) == [0, 2]
        assert TwoPointerSolutions.two_sum_sorted([1, 2, 3, 4], 10) == [-1, -1]

    def test_is_palindrome(self):
        """Test palindrome check."""
        assert TwoPointerSolutions.is_palindrome("A man, a plan, a canal: Panama") == True
        assert TwoPointerSolutions.is_palindrome("race a car") == False
        assert TwoPointerSolutions.is_palindrome("") == True

    def test_remove_duplicates(self):
        """Test remove duplicates."""
        nums = [1, 1, 2, 2, 3]
        length = TwoPointerSolutions.remove_duplicates(nums)
        assert length == 3
        assert nums[:length] == [1, 2, 3]

    def test_three_sum(self):
        """Test three sum."""
        result = TwoPointerSolutions.three_sum([-1, 0, 1, 2, -1, -4])
        assert len(result) == 2
        assert [-1, -1, 2] in result
        assert [-1, 0, 1] in result

    def test_container_with_most_water(self):
        """Test container with most water."""
        assert TwoPointerSolutions.container_with_most_water([1,8,6,2,5,4,8,3,7]) == 49
        assert TwoPointerSolutions.container_with_most_water([1,1]) == 1
