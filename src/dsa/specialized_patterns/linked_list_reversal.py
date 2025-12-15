"""
In-place Linked List Reversal Pattern

Pattern: Reverse linked list or parts of it in-place.
When to use:
- Reverse linked list
- Reverse k-group
- Reverse between positions
- Palindrome linked list

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import Optional
from dsa.data_structures.linked_list import ListNode


class LinkedListReversalSolutions:
    """Solutions using linked list reversal pattern."""

    @staticmethod
    def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Reverse entire linked list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

    @staticmethod
    def reverse_between(head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Reverse linked list from position left to right.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head or left == right:
            return head

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        # Move to node before left
        for _ in range(left - 1):
            prev = prev.next

        # Reverse sublist
        current = prev.next
        for _ in range(right - left):
            next_node = current.next
            current.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node

        return dummy.next
