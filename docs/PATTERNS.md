# DSA Patterns Guide

Complete guide to all coding patterns with explanations, when to use them, and example problems.

## Table of Contents

- [Core Patterns](#core-patterns)
- [Advanced Patterns](#advanced-patterns)
- [Specialized Patterns](#specialized-patterns)

---

## Core Patterns

These patterns solve 80% of interview problems. Master these first.

### 1. Two Pointer

**Concept**: Use two pointers to iterate through data structure, usually from different positions.

**When to Use**:
- Sorted arrays
- Finding pairs with specific sum
- Palindrome problems
- Removing duplicates
- Partitioning arrays

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Key Problems**:
- Two Sum II (Sorted Array)
- Three Sum
- Container With Most Water
- Valid Palindrome
- Remove Duplicates from Sorted Array

**Template**:
```python
left, right = 0, len(arr) - 1

while left < right:
    if condition:
        # Process
        left += 1
        right -= 1
    elif arr[left] + arr[right] < target:
        left += 1
    else:
        right -= 1
```

---

### 2. Sliding Window

**Concept**: Maintain a window that slides through array/string.

**When to Use**:
- Contiguous subarrays/substrings
- Maximum/minimum sum of subarray of size k
- Longest/shortest substring with condition
- Finding patterns in strings

**Time Complexity**: O(n)
**Space Complexity**: O(k) where k is window size

**Key Problems**:
- Maximum Sum Subarray of Size K
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Permutation in String
- Longest Substring with K Distinct Characters

**Template**:
```python
window_start = 0
for window_end in range(len(arr)):
    # Expand window
    # Add arr[window_end] to window

    while window needs shrinking:
        # Shrink window
        # Remove arr[window_start] from window
        window_start += 1

    # Update result
```

---

### 3. Fast & Slow Pointer

**Concept**: Use two pointers moving at different speeds.

**When to Use**:
- Detecting cycles in linked lists
- Finding middle of linked list
- Finding cycle start
- Happy number problem

**Time Complexity**: O(n)
**Space Complexity**: O(1)

**Key Problems**:
- Linked List Cycle
- Find Middle of Linked List
- Happy Number
- Palindrome Linked List

**Template**:
```python
slow = fast = head

while fast and fast.next:
    slow = slow.next
    fast = fast.next.next

    if slow == fast:
        # Cycle detected
        break
```

---

### 4. Binary Search

**Concept**: Divide search space in half repeatedly.

**When to Use**:
- Searching in sorted arrays
- Finding boundaries
- Search in rotated sorted array
- Finding peak element
- Binary search on answer

**Time Complexity**: O(log n)
**Space Complexity**: O(1) iterative, O(log n) recursive

**Key Problems**:
- Binary Search
- Search in Rotated Sorted Array
- Find First and Last Position
- Search Insert Position
- Find Peak Element

**Template**:
```python
left, right = 0, len(arr) - 1

while left <= right:
    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1
```

---

### 5. Depth-First Search (DFS)

**Concept**: Explore as far as possible along each branch before backtracking.

**When to Use**:
- Tree/graph traversal
- Path finding
- Detecting cycles
- Connected components

**Time Complexity**: O(V + E) for graphs, O(n) for trees
**Space Complexity**: O(h) where h is height (recursion stack)

**Key Problems**:
- Maximum Depth of Binary Tree
- Path Sum
- Number of Islands
- Validate BST
- Course Schedule

**Template**:
```python
def dfs(node):
    if not node:
        return

    # Process current node

    dfs(node.left)
    dfs(node.right)
```

---

### 6. Breadth-First Search (BFS)

**Concept**: Explore all neighbors before going deeper.

**When to Use**:
- Level-order traversal
- Shortest path in unweighted graphs
- Finding minimum depth
- Finding all nodes at distance k

**Time Complexity**: O(V + E)
**Space Complexity**: O(w) where w is maximum width

**Key Problems**:
- Binary Tree Level Order Traversal
- Minimum Depth of Binary Tree
- Word Ladder
- Shortest Path in Binary Matrix

**Template**:
```python
from collections import deque

queue = deque([start_node])

while queue:
    level_size = len(queue)

    for _ in range(level_size):
        node = queue.popleft()

        # Process node

        for neighbor in get_neighbors(node):
            queue.append(neighbor)
```

---

### 7. Backtracking

**Concept**: Build solution incrementally and backtrack when constraint violated.

**When to Use**:
- Generating combinations/permutations
- Constraint satisfaction problems
- N-Queens, Sudoku solver
- Path finding with constraints

**Time Complexity**: Usually O(2^n) or O(n!)
**Space Complexity**: O(n) for recursion stack

**Key Problems**:
- Subsets
- Permutations
- Combination Sum
- Generate Parentheses
- N-Queens

**Template**:
```python
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return

    for choice in choices:
        # Make choice
        path.append(choice)

        backtrack(path, next_choices)

        # Undo choice (backtrack)
        path.pop()
```

---

### 8. Dynamic Programming

**Concept**: Break problem into overlapping subproblems, store results.

**When to Use**:
- Optimization problems (min/max)
- Counting problems
- Problems with overlapping subproblems
- Fibonacci, knapsack, LCS, etc.

**Time Complexity**: O(n) to O(n³) depending on problem
**Space Complexity**: O(n) to O(n²)

**Key Problems**:
- Fibonacci Number
- Climbing Stairs
- Coin Change
- Longest Increasing Subsequence
- 0/1 Knapsack

**Template**:
```python
# Bottom-up approach
dp = [0] * (n + 1)
dp[0] = base_case

for i in range(1, n + 1):
    for choice in choices:
        dp[i] = optimal(dp[i], dp[i - choice] + cost)

return dp[n]
```

---

## Advanced Patterns

### 9. Merge Intervals

**When to Use**: Problems involving overlapping intervals, scheduling, ranges.

**Time Complexity**: O(n log n)
**Space Complexity**: O(n)

**Key Problems**: Merge Intervals, Insert Interval, Meeting Rooms

---

### 10. Matrix Traversal (Island Pattern)

**When to Use**: 2D grid traversal, island counting, flood fill.

**Time Complexity**: O(m × n)
**Space Complexity**: O(m × n)

**Key Problems**: Number of Islands, Max Area of Island, Surrounded Regions

---

### 11. Topological Sort

**When to Use**: Dependency resolution, task scheduling, course prerequisites.

**Time Complexity**: O(V + E)
**Space Complexity**: O(V + E)

**Key Problems**: Course Schedule, Course Schedule II, Alien Dictionary

---

### 12. Union-Find (DSU)

**When to Use**: Network connectivity, detecting cycles, connected components.

**Time Complexity**: O(α(n)) ≈ O(1) with path compression
**Space Complexity**: O(n)

**Key Problems**: Number of Connected Components, Redundant Connection

---

### 13. Monotonic Stack

**When to Use**: Next greater/smaller element, histogram problems.

**Time Complexity**: O(n)
**Space Complexity**: O(n)

**Key Problems**: Next Greater Element, Daily Temperatures, Largest Rectangle

---

### 14. Heap (Top K Elements)

**When to Use**: Finding k largest/smallest, maintaining sorted stream.

**Time Complexity**: O(n log k)
**Space Complexity**: O(k)

**Key Problems**: Kth Largest Element, K Closest Points, Top K Frequent

---

## Specialized Patterns

### 15. Cyclic Sort

**When to Use**: Arrays with numbers in range [1, n], finding missing/duplicate.

**Time Complexity**: O(n)
**Space Complexity**: O(1)

---

### 16. Two Heaps

**When to Use**: Finding median, sliding window median.

**Time Complexity**: O(log n) for insertions
**Space Complexity**: O(n)

---

### 17. Trie

**When to Use**: Autocomplete, spell checker, prefix matching.

**Time Complexity**: O(m) where m is string length
**Space Complexity**: O(ALPHABET_SIZE × m × n)

---

## Pattern Recognition Guide

| Problem Characteristic | Pattern to Consider |
|------------------------|---------------------|
| Sorted array | Binary Search, Two Pointer |
| Find pairs with sum | Two Pointer |
| Contiguous subarray | Sliding Window |
| Linked list cycle | Fast & Slow Pointer |
| Tree traversal | DFS or BFS |
| Graph traversal | DFS or BFS |
| Optimization problem | Dynamic Programming |
| Generate combinations | Backtracking |
| Overlapping intervals | Merge Intervals |
| 2D grid traversal | Matrix Traversal (DFS/BFS) |
| Task scheduling | Topological Sort |
| Network connectivity | Union-Find |
| Next greater element | Monotonic Stack |
| Top k elements | Heap |
| Array with range [1,n] | Cyclic Sort |
| Median from stream | Two Heaps |
| Prefix matching | Trie |

---

## How to Practice

1. **Learn one pattern at a time**
2. **Solve 3-5 problems per pattern**
3. **Identify pattern in new problems**
4. **Implement from scratch**
5. **Analyze time/space complexity**
6. **Practice pattern recognition**

## Resources

- LeetCode pattern-based problem lists
- Educational Codeforces
- GeeksforGeeks pattern articles
- System design interview books
