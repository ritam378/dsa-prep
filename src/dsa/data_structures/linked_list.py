"""
Linked List Data Structure

Common linked list implementations and utilities.
"""

from typing import Optional, Any


class ListNode:
    """Singly linked list node."""

    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


class DoublyListNode:
    """Doubly linked list node."""

    def __init__(
        self,
        val: int = 0,
        prev: Optional['DoublyListNode'] = None,
        next: Optional['DoublyListNode'] = None
    ):
        self.val = val
        self.prev = prev
        self.next = next

    def __repr__(self) -> str:
        return f"DoublyListNode({self.val})"


class LinkedList:
    """Singly linked list implementation with common operations."""

    def __init__(self):
        self.head: Optional[ListNode] = None
        self.size: int = 0

    def append(self, val: int) -> None:
        """Add a node at the end of the list."""
        if not self.head:
            self.head = ListNode(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = ListNode(val)
        self.size += 1

    def prepend(self, val: int) -> None:
        """Add a node at the beginning of the list."""
        new_node = ListNode(val, self.head)
        self.head = new_node
        self.size += 1

    def delete(self, val: int) -> bool:
        """Delete the first occurrence of a value."""
        if not self.head:
            return False

        if self.head.val == val:
            self.head = self.head.next
            self.size -= 1
            return True

        current = self.head
        while current.next:
            if current.next.val == val:
                current.next = current.next.next
                self.size -= 1
                return True
            current = current.next

        return False

    def to_list(self) -> list:
        """Convert linked list to Python list."""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result

    @staticmethod
    def from_list(values: list) -> 'LinkedList':
        """Create a linked list from a Python list."""
        ll = LinkedList()
        for val in values:
            ll.append(val)
        return ll

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return f"LinkedList({self.to_list()})"
