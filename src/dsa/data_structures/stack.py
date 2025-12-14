"""
Stack Data Structure

Stack implementation with common operations.
"""

from typing import Any, Optional


class Stack:
    """Stack implementation using a list."""

    def __init__(self):
        self._items: list = []

    def push(self, item: Any) -> None:
        """Push an item onto the stack."""
        self._items.append(item)

    def pop(self) -> Any:
        """
        Remove and return the top item from the stack.
        Raises IndexError if stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self) -> Any:
        """
        Return the top item without removing it.
        Raises IndexError if stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self) -> bool:
        """Check if the stack is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the stack."""
        return len(self._items)

    def clear(self) -> None:
        """Remove all items from the stack."""
        self._items.clear()

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Stack({self._items})"


class MinStack:
    """
    Stack that supports push, pop, top, and retrieving minimum element in O(1).
    """

    def __init__(self):
        self._stack: list = []
        self._min_stack: list = []

    def push(self, val: int) -> None:
        """Push an element onto the stack."""
        self._stack.append(val)
        if not self._min_stack or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        """Remove the top element from the stack."""
        if self._stack:
            val = self._stack.pop()
            if val == self._min_stack[-1]:
                self._min_stack.pop()

    def top(self) -> int:
        """Get the top element."""
        if not self._stack:
            raise IndexError("top from empty stack")
        return self._stack[-1]

    def get_min(self) -> int:
        """Retrieve the minimum element in O(1)."""
        if not self._min_stack:
            raise IndexError("get_min from empty stack")
        return self._min_stack[-1]
