"""
Cache Data Structures (LRU Cache, LFU Cache)

These are extremely common interview problems, especially at FAANG companies.
Understanding these demonstrates knowledge of:
- Hash tables for O(1) lookup
- Doubly linked lists for O(1) insertion/deletion
- Design patterns and API design
- Time-space complexity tradeoffs

INTERVIEW FREQUENCY: VERY HIGH
Companies: Google, Facebook, Amazon, Microsoft, Apple, Netflix, Uber, Lyft

LRU Cache (Least Recently Used):
- Evicts least recently used item when capacity is reached
- get() and put() operations in O(1)
- Uses HashMap + Doubly Linked List

LFU Cache (Least Frequently Used):
- Evicts least frequently used item when capacity is reached
- Ties broken by least recently used among same frequency
- get() and put() operations in O(1)
- Uses multiple data structures (more complex than LRU)
"""

from typing import Optional
from collections import OrderedDict


class ListNode:
    """Doubly linked list node for LRU Cache."""

    def __init__(self, key: int = 0, value: int = 0):
        self.key = key
        self.value = value
        self.prev: Optional[ListNode] = None
        self.next: Optional[ListNode] = None


class LRUCache:
    """
    LRU (Least Recently Used) Cache implementation.

    Design Pattern:
    - Hash Map: for O(1) key lookup -> maps key to node
    - Doubly Linked List: maintains access order (most recent at head)

    Operations:
    - get(key): Return value if exists, -1 otherwise. Mark as recently used.
    - put(key, value): Insert or update key-value pair. Evict LRU if at capacity.

    Both operations are O(1) time complexity.

    Time Complexity: O(1) for both get and put
    Space Complexity: O(capacity)

    Difficulty: Medium
    Interview Frequency: VERY HIGH - One of most asked design problems
    Companies: Google, Facebook, Amazon, Microsoft, Apple, Netflix, Uber
    Estimated Time: 35-45 minutes

    Example:
        >>> cache = LRUCache(2)
        >>> cache.put(1, 1)
        >>> cache.put(2, 2)
        >>> cache.get(1)  # returns 1
        1
        >>> cache.put(3, 3)  # evicts key 2
        >>> cache.get(2)  # returns -1 (not found)
        -1
        >>> cache.put(4, 4)  # evicts key 1
        >>> cache.get(1)  # returns -1 (not found)
        -1
        >>> cache.get(3)  # returns 3
        3
        >>> cache.get(4)  # returns 4
        4

    Interview Tips:
    - Explain why you need both hash map AND linked list
    - Hash map alone: can't track order
    - Linked list alone: can't do O(1) lookup
    - Doubly linked list allows O(1) node removal from middle
    - Sentinel nodes (dummy head/tail) simplify edge cases
    - Draw the data structure during interview
    - Walk through example operations step-by-step
    - Discuss thread safety if asked (would need locks)

    Common Follow-ups:
    - What if we want LRU eviction per category/namespace?
    - How would you make it thread-safe?
    - What if capacity is very large - memory concerns?
    - How would you implement TTL (time to live)?
    """

    def __init__(self, capacity: int):
        """
        Initialize LRU cache with given capacity.

        Args:
            capacity: Maximum number of key-value pairs cache can hold
        """
        self.capacity = capacity
        self.cache = {}  # key -> node mapping

        # Sentinel nodes to avoid edge case handling
        # Most recent items near head, least recent near tail
        self.head = ListNode()  # dummy head (most recent side)
        self.tail = ListNode()  # dummy tail (least recent side)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _remove_node(self, node: ListNode) -> None:
        """Remove node from its current position in linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _add_to_head(self, node: ListNode) -> None:
        """Add node right after head (mark as most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _move_to_head(self, node: ListNode) -> None:
        """Move existing node to head (mark as recently used)."""
        self._remove_node(node)
        self._add_to_head(node)

    def _remove_tail(self) -> ListNode:
        """Remove and return least recently used node."""
        lru_node = self.tail.prev
        self._remove_node(lru_node)
        return lru_node

    def get(self, key: int) -> int:
        """
        Get value for key, mark as recently used.

        Args:
            key: Key to lookup

        Returns:
            Value if key exists, -1 otherwise

        Time Complexity: O(1)
        """
        if key not in self.cache:
            return -1

        node = self.cache[key]
        self._move_to_head(node)  # Mark as recently used
        return node.value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.

        If key exists: update value and mark as recently used
        If key doesn't exist: insert new pair
        If at capacity: evict least recently used item first

        Args:
            key: Key to insert/update
            value: Value to store

        Time Complexity: O(1)
        """
        if key in self.cache:
            # Update existing key
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            # Insert new key
            new_node = ListNode(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

            # Check capacity and evict if necessary
            if len(self.cache) > self.capacity:
                lru_node = self._remove_tail()
                del self.cache[lru_node.key]


class LFUCache:
    """
    LFU (Least Frequently Used) Cache implementation.

    Design Pattern:
    - Hash Map 1: key -> (value, frequency)
    - Hash Map 2: frequency -> doubly linked list of keys with that frequency
    - Track minimum frequency for O(1) eviction

    Operations:
    - get(key): Return value if exists, -1 otherwise. Increment frequency.
    - put(key, value): Insert or update. Evict LFU (ties broken by LRU) if at capacity.

    Both operations are O(1) time complexity.

    Time Complexity: O(1) for both get and put
    Space Complexity: O(capacity)

    Difficulty: Hard
    Interview Frequency: HIGH - Popular at top companies
    Companies: Google, Facebook, Amazon, Microsoft, Apple
    Estimated Time: 45-60 minutes

    Example:
        >>> cache = LFUCache(2)
        >>> cache.put(1, 1)
        >>> cache.put(2, 2)
        >>> cache.get(1)  # returns 1, freq of key 1 = 1
        1
        >>> cache.put(3, 3)  # evicts key 2 (freq=0, least frequent)
        >>> cache.get(2)  # returns -1 (evicted)
        -1
        >>> cache.get(3)  # returns 3
        3
        >>> cache.put(4, 4)  # evicts key 1 (both have freq=1, key 1 is LRU)
        >>> cache.get(1)  # returns -1 (evicted)
        -1

    Interview Tips:
    - More complex than LRU - expect to spend time on design
    - Need to handle frequency buckets
    - Within same frequency, use LRU order
    - Track min_frequency for fast eviction
    - Can use OrderedDict in Python for frequency buckets
    - Draw the multi-level data structure
    - Walk through state changes clearly

    Common Follow-ups:
    - How would you handle very large frequencies?
    - What if we want to decay frequency over time?
    - How to make it distributed?
    """

    def __init__(self, capacity: int):
        """
        Initialize LFU cache with given capacity.

        Args:
            capacity: Maximum number of key-value pairs cache can hold
        """
        self.capacity = capacity
        self.min_freq = 0

        # key -> (value, frequency)
        self.key_to_val_freq = {}

        # frequency -> OrderedDict of {key: value}
        # OrderedDict maintains insertion order (LRU within same frequency)
        self.freq_to_keys = {}

    def _update_freq(self, key: int) -> None:
        """Update frequency of a key (move to next frequency bucket)."""
        value, freq = self.key_to_val_freq[key]

        # Remove from current frequency bucket
        del self.freq_to_keys[freq][key]

        # If current frequency bucket is now empty and it was min_freq
        if not self.freq_to_keys[freq] and freq == self.min_freq:
            self.min_freq += 1
            # Clean up empty bucket
            del self.freq_to_keys[freq]

        # Add to next frequency bucket
        new_freq = freq + 1
        if new_freq not in self.freq_to_keys:
            self.freq_to_keys[new_freq] = OrderedDict()
        self.freq_to_keys[new_freq][key] = value

        # Update key's frequency
        self.key_to_val_freq[key] = (value, new_freq)

    def get(self, key: int) -> int:
        """
        Get value for key, increment frequency.

        Args:
            key: Key to lookup

        Returns:
            Value if key exists, -1 otherwise

        Time Complexity: O(1)
        """
        if key not in self.key_to_val_freq:
            return -1

        value, _ = self.key_to_val_freq[key]
        self._update_freq(key)
        return value

    def put(self, key: int, value: int) -> None:
        """
        Insert or update key-value pair.

        If key exists: update value and increment frequency
        If key doesn't exist: insert with frequency 1
        If at capacity: evict least frequently used (LRU among ties)

        Args:
            key: Key to insert/update
            value: Value to store

        Time Complexity: O(1)
        """
        if self.capacity <= 0:
            return

        if key in self.key_to_val_freq:
            # Update existing key
            _, freq = self.key_to_val_freq[key]
            self.key_to_val_freq[key] = (value, freq)
            self._update_freq(key)
        else:
            # Check capacity
            if len(self.key_to_val_freq) >= self.capacity:
                # Evict LFU (and LRU among same frequency)
                # Pop first item (oldest) from min_freq bucket
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.key_to_val_freq[evict_key]

            # Insert new key with frequency 1
            self.key_to_val_freq[key] = (value, 1)
            if 1 not in self.freq_to_keys:
                self.freq_to_keys[1] = OrderedDict()
            self.freq_to_keys[1][key] = value
            self.min_freq = 1


# Alternative LFU implementation using more explicit node structure
class LFUNode:
    """Node for LFU Cache with explicit frequency tracking."""

    def __init__(self, key: int, value: int, freq: int = 1):
        self.key = key
        self.value = value
        self.freq = freq
        self.prev: Optional['LFUNode'] = None
        self.next: Optional['LFUNode'] = None


# Comparison summary for interviews
CACHE_COMPARISON = """
LRU vs LFU CACHE - INTERVIEW CHEATSHEET

╔═══════════════╦═════════════════════╦═════════════════════════╗
║   Aspect      ║        LRU          ║          LFU            ║
╠═══════════════╬═════════════════════╬═════════════════════════╣
║ Eviction      ║ Least Recently Used ║ Least Frequently Used   ║
║ Complexity    ║ Medium              ║ Hard                    ║
║ Time: get()   ║ O(1)                ║ O(1)                    ║
║ Time: put()   ║ O(1)                ║ O(1)                    ║
║ Space         ║ O(capacity)         ║ O(capacity)             ║
║ Data Structs  ║ HashMap + DLL       ║ HashMap + Freq Buckets  ║
║ Interview %   ║ Very High (~70%)    ║ High (~30%)             ║
╚═══════════════╩═════════════════════╩═════════════════════════╝

WHEN TO USE WHICH:

LRU Cache:
✓ Access patterns favor recent items (temporal locality)
✓ Simpler to implement and maintain
✓ Most common in practice (browser cache, OS page cache)
✓ Examples: Web browser, CDN, database query cache

LFU Cache:
✓ Access patterns favor popular items
✓ Need to protect against cache flooding
✓ Long-running systems where frequency matters
✓ Examples: Video streaming (popular videos), DNS cache

KEY IMPLEMENTATION DETAILS:

LRU Cache Structure:
┌─────────────┐
│   HashMap   │ → O(1) lookup
└─────────────┘
       ↓
┌─────────────┐
│ Doubly LL   │ → O(1) move to front/remove tail
└─────────────┘
Head (MRU) ←→ Node ←→ Node ←→ Tail (LRU)

LFU Cache Structure:
┌─────────────┐
│   HashMap   │ → key → (value, freq)
└─────────────┘
       ↓
┌─────────────┐
│ Freq Buckets│ → freq → OrderedDict of keys
└─────────────┘
Freq 1: {k1, k2, k3}  (LRU order)
Freq 2: {k4, k5}
Freq 3: {k6}

COMMON INTERVIEW MISTAKES:

LRU:
✗ Using singly linked list (can't remove from middle in O(1))
✗ Forgetting to update on both get() and put()
✗ Not handling capacity = 1 edge case
✗ Forgetting to remove from hash map when evicting

LFU:
✗ Not handling LRU tie-breaking among same frequency
✗ Forgetting to update min_freq correctly
✗ Using list instead of OrderedDict for freq buckets (not O(1))
✗ Not cleaning up empty frequency buckets

FOLLOW-UP QUESTIONS TO EXPECT:

1. How would you make it thread-safe?
   → Add locks/mutex around get() and put()
   → Read-write locks for better concurrency
   → Consider lock-free data structures

2. How to add TTL (time-to-live)?
   → Add timestamp to nodes
   → Separate cleanup thread or lazy cleanup on access

3. How to make it distributed?
   → Consistent hashing for key distribution
   → Replication for availability
   → Cache coherence protocols

4. What if capacity is huge (millions)?
   → Memory-mapped files
   → Hybrid mem/disk cache
   → Approximation algorithms (not true LRU/LFU)
"""
