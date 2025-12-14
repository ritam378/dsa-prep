"""
Queue Data Structure

Queue and Deque implementations with common operations.
"""

from typing import Any, Optional
from collections import deque


class Queue:
    """Queue implementation using collections.deque."""

    def __init__(self):
        self._items = deque()

    def enqueue(self, item: Any) -> None:
        """Add an item to the rear of the queue."""
        self._items.append(item)

    def dequeue(self) -> Any:
        """
        Remove and return the front item from the queue.
        Raises IndexError if queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def front(self) -> Any:
        """
        Return the front item without removing it.
        Raises IndexError if queue is empty.
        """
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[0]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return len(self._items) == 0

    def size(self) -> int:
        """Return the number of items in the queue."""
        return len(self._items)

    def __len__(self) -> int:
        return len(self._items)

    def __repr__(self) -> str:
        return f"Queue({list(self._items)})"


class CircularQueue:
    """Circular queue with fixed capacity."""

    def __init__(self, capacity: int):
        self.capacity = capacity
        self._items = [None] * capacity
        self._front = 0
        self._rear = -1
        self._size = 0

    def enqueue(self, item: Any) -> bool:
        """Add an item to the queue. Returns False if queue is full."""
        if self.is_full():
            return False
        self._rear = (self._rear + 1) % self.capacity
        self._items[self._rear] = item
        self._size += 1
        return True

    def dequeue(self) -> Any:
        """Remove and return the front item. Raises IndexError if empty."""
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        item = self._items[self._front]
        self._items[self._front] = None
        self._front = (self._front + 1) % self.capacity
        self._size -= 1
        return item

    def front(self) -> Any:
        """Return the front item without removing it."""
        if self.is_empty():
            raise IndexError("front from empty queue")
        return self._items[self._front]

    def is_empty(self) -> bool:
        """Check if the queue is empty."""
        return self._size == 0

    def is_full(self) -> bool:
        """Check if the queue is full."""
        return self._size == self.capacity

    def __len__(self) -> int:
        return self._size
