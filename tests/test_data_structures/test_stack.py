"""
Tests for Stack data structure.
"""

import pytest
from dsa.data_structures.stack import Stack, MinStack


class TestStack:
    """Test cases for stack."""

    def test_push_pop(self):
        """Test push and pop operations."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert stack.pop() == 3
        assert stack.pop() == 2
        assert len(stack) == 1

    def test_peek(self):
        """Test peek operation."""
        stack = Stack()
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2
        assert len(stack) == 2

    def test_is_empty(self):
        """Test is_empty check."""
        stack = Stack()
        assert stack.is_empty() == True
        stack.push(1)
        assert stack.is_empty() == False

    def test_pop_empty_stack(self):
        """Test popping from empty stack raises error."""
        stack = Stack()
        with pytest.raises(IndexError):
            stack.pop()


class TestMinStack:
    """Test cases for min stack."""

    def test_min_stack(self):
        """Test min stack operations."""
        stack = MinStack()
        stack.push(-2)
        stack.push(0)
        stack.push(-3)
        assert stack.get_min() == -3
        stack.pop()
        assert stack.top() == 0
        assert stack.get_min() == -2
