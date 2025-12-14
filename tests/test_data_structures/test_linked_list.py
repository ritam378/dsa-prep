"""
Tests for Linked List data structure.
"""

import pytest
from dsa.data_structures.linked_list import ListNode, LinkedList


class TestLinkedList:
    """Test cases for linked list."""

    def test_append(self):
        """Test appending to linked list."""
        ll = LinkedList()
        ll.append(1)
        ll.append(2)
        ll.append(3)
        assert ll.to_list() == [1, 2, 3]
        assert len(ll) == 3

    def test_prepend(self):
        """Test prepending to linked list."""
        ll = LinkedList()
        ll.prepend(1)
        ll.prepend(2)
        ll.prepend(3)
        assert ll.to_list() == [3, 2, 1]

    def test_delete(self):
        """Test deleting from linked list."""
        ll = LinkedList.from_list([1, 2, 3, 4, 5])
        assert ll.delete(3) == True
        assert ll.to_list() == [1, 2, 4, 5]
        assert ll.delete(10) == False

    def test_from_list(self):
        """Test creating linked list from list."""
        ll = LinkedList.from_list([1, 2, 3])
        assert ll.to_list() == [1, 2, 3]
