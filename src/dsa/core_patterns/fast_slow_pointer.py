"""
Fast & Slow Pointer Pattern (Floyd's Algorithm)

Pattern: Use two pointers moving at different speeds.
When to use:
- Detecting cycles in linked lists
- Finding middle of linked list
- Finding cycle start
- Happy number problem

Time Complexity: Usually O(n)
Space Complexity: O(1)
"""

from typing import Optional
import sys
sys.path.append('..')
from data_structures.linked_list import ListNode


class FastSlowPointerSolutions:
    """Solutions using the fast and slow pointer pattern."""

    @staticmethod
    def has_cycle(head: Optional[ListNode]) -> bool:
        """
        Detect if linked list has a cycle.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return False

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    @staticmethod
    def find_middle(head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find middle node of linked list.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not head:
            return None

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    @staticmethod
    def is_happy_number(n: int) -> bool:
        """
        Determine if a number is happy.

        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        def get_next(num: int) -> int:
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total

        slow = fast = n

        while True:
            slow = get_next(slow)
            fast = get_next(get_next(fast))

            if fast == 1:
                return True
            if slow == fast:
                return False
