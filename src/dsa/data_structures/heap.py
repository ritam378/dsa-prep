"""
Heap Data Structure

Min heap and max heap implementations.
"""

from typing import List, Any
import heapq


class MinHeap:
    """Min heap implementation using Python's heapq."""

    def __init__(self):
        self._heap: List[Any] = []

    def push(self, item: Any) -> None:
        """Add an item to the heap."""
        heapq.heappush(self._heap, item)

    def pop(self) -> Any:
        """Remove and return the minimum item."""
        if not self._heap:
            raise IndexError("pop from empty heap")
        return heapq.heappop(self._heap)

    def peek(self) -> Any:
        """Return the minimum item without removing it."""
        if not self._heap:
            raise IndexError("peek from empty heap")
        return self._heap[0]

    def push_pop(self, item: Any) -> Any:
        """Push item and pop minimum in one operation."""
        return heapq.heappushpop(self._heap, item)

    def replace(self, item: Any) -> Any:
        """Pop minimum and push item in one operation."""
        if not self._heap:
            raise IndexError("replace on empty heap")
        return heapq.heapreplace(self._heap, item)

    def is_empty(self) -> bool:
        """Check if the heap is empty."""
        return len(self._heap) == 0

    def size(self) -> int:
        """Return the number of items in the heap."""
        return len(self._heap)

    def __len__(self) -> int:
        return len(self._heap)

    def __repr__(self) -> str:
        return f"MinHeap({self._heap})"


class MaxHeap:
    """Max heap implementation using Python's heapq with negation."""

    def __init__(self):
        self._heap: List[Any] = []

    def push(self, item: Any) -> None:
        """Add an item to the heap."""
        heapq.heappush(self._heap, -item)

    def pop(self) -> Any:
        """Remove and return the maximum item."""
        if not self._heap:
            raise IndexError("pop from empty heap")
        return -heapq.heappop(self._heap)

    def peek(self) -> Any:
        """Return the maximum item without removing it."""
        if not self._heap:
            raise IndexError("peek from empty heap")
        return -self._heap[0]

    def is_empty(self) -> bool:
        """Check if the heap is empty."""
        return len(self._heap) == 0

    def size(self) -> int:
        """Return the number of items in the heap."""
        return len(self._heap)

    def __len__(self) -> int:
        return len(self._heap)

    def __repr__(self) -> str:
        return f"MaxHeap({[-x for x in self._heap]})"


def heapify(arr: List[int]) -> List[int]:
    """Convert a list into a min heap in-place."""
    heapq.heapify(arr)
    return arr


def nlargest(n: int, iterable: List[Any]) -> List[Any]:
    """Return n largest elements from the iterable."""
    return heapq.nlargest(n, iterable)


def nsmallest(n: int, iterable: List[Any]) -> List[Any]:
    """Return n smallest elements from the iterable."""
    return heapq.nsmallest(n, iterable)
