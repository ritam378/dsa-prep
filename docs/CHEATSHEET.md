# DSA Patterns Cheatsheet

Quick reference for pattern recognition and complexity analysis.

## Pattern Recognition Table

| Problem Keywords | Pattern | Example Problems |
|------------------|---------|------------------|
| **Sorted array** | Binary Search, Two Pointer | Search in Rotated Array, Two Sum II |
| **Find pair with sum** | Two Pointer, Hash Map | Two Sum, Three Sum |
| **Contiguous subarray/substring** | Sliding Window | Max Sum Subarray, Longest Substring |
| **Linked list cycle** | Fast & Slow Pointer | Detect Cycle, Find Middle |
| **Tree/graph traversal** | DFS, BFS | Path Sum, Level Order |
| **Shortest path** | BFS, Dijkstra | Word Ladder, Network Delay |
| **Optimization (min/max)** | Dynamic Programming | Coin Change, LIS |
| **Counting ways** | Dynamic Programming | Climbing Stairs, Unique Paths |
| **Generate all combinations** | Backtracking | Subsets, Permutations |
| **Overlapping intervals** | Merge Intervals | Merge Intervals, Meeting Rooms |
| **2D grid traversal** | DFS/BFS | Number of Islands, Word Search |
| **Task dependencies** | Topological Sort | Course Schedule |
| **Network connectivity** | Union-Find | Connected Components |
| **Next greater/smaller** | Monotonic Stack | Next Greater Element |
| **Top k elements** | Heap | Kth Largest, Top K Frequent |
| **Array range [1,n]** | Cyclic Sort | Find Missing Number |
| **Median from stream** | Two Heaps | Find Median from Data Stream |
| **Prefix matching** | Trie | Autocomplete, Word Search II |

---

## Time Complexity Cheatsheet

### Common Patterns

| Pattern | Time | Space | Notes |
|---------|------|-------|-------|
| Two Pointer | O(n) | O(1) | Linear scan |
| Sliding Window | O(n) | O(k) | k = window size |
| Fast & Slow Pointer | O(n) | O(1) | Cycle detection |
| Binary Search | O(log n) | O(1) | Sorted input |
| DFS | O(V + E) | O(h) | h = height |
| BFS | O(V + E) | O(w) | w = width |
| Backtracking | O(2^n) or O(n!) | O(n) | Exponential |
| Dynamic Programming | O(n) to O(n²) | O(n) to O(n²) | Varies |
| Merge Intervals | O(n log n) | O(n) | Sorting + merge |
| Topological Sort | O(V + E) | O(V + E) | Graph |
| Union-Find | O(α(n)) ≈ O(1) | O(n) | Amortized |
| Monotonic Stack | O(n) | O(n) | Each element once |
| Heap (Top K) | O(n log k) | O(k) | Min/max heap |
| Cyclic Sort | O(n) | O(1) | Array range [1,n] |
| Trie | O(m) | O(ALPHABET × m × n) | m = length |

### Data Structure Operations

| Data Structure | Access | Search | Insert | Delete |
|----------------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1)* | O(1)* |
| Stack | O(n) | O(n) | O(1) | O(1) |
| Queue | O(n) | O(n) | O(1) | O(1) |
| Hash Table | N/A | O(1)† | O(1)† | O(1)† |
| Binary Search Tree | O(log n)† | O(log n)† | O(log n)† | O(log n)† |
| Heap | N/A | O(n) | O(log n) | O(log n) |
| Trie | O(m) | O(m) | O(m) | O(m) |

*At known position
†Average case

---

## Pattern Templates

### Two Pointer
```python
left, right = 0, len(arr) - 1
while left < right:
    if condition:
        left += 1
        right -= 1
```

### Sliding Window
```python
window_start = 0
for window_end in range(len(arr)):
    # Expand window
    while shrink_condition:
        # Shrink window
        window_start += 1
```

### Binary Search
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
```

### DFS (Recursive)
```python
def dfs(node):
    if not node:
        return
    # Process
    dfs(node.left)
    dfs(node.right)
```

### BFS
```python
from collections import deque
queue = deque([start])
while queue:
    node = queue.popleft()
    # Process
    for neighbor in neighbors:
        queue.append(neighbor)
```

### Backtracking
```python
def backtrack(path):
    if is_solution(path):
        result.append(path[:])
        return
    for choice in choices:
        path.append(choice)
        backtrack(path)
        path.pop()
```

### Dynamic Programming
```python
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = optimal(dp[i-1], dp[i-2], ...)
```

---

## Space Complexity Guide

### O(1) - Constant
- Variables, pointers
- Two Pointer pattern
- Cyclic Sort
- Fast & Slow Pointer

### O(log n) - Logarithmic
- Binary search (recursive)
- Balanced tree height

### O(n) - Linear
- Hash table
- Dynamic programming (1D)
- Stack/Queue for traversal
- Single array/list

### O(n²) - Quadratic
- 2D DP table
- Adjacency matrix
- Nested arrays

### O(2^n) - Exponential
- Backtracking (worst case)
- All subsets storage

---

## Common Edge Cases

### Arrays
- Empty array []
- Single element [1]
- All same elements [5,5,5,5]
- Sorted vs unsorted
- Duplicates
- Negative numbers
- Integer overflow

### Strings
- Empty string ""
- Single character "a"
- All same characters "aaaa"
- Special characters
- Case sensitivity

### Linked Lists
- Empty list (null)
- Single node
- Two nodes
- Cycle vs no cycle
- Even vs odd length

### Trees
- Empty tree (null)
- Single node
- Left-skewed
- Right-skewed
- Balanced
- Complete vs incomplete

### Graphs
- Empty graph
- Single node
- Disconnected components
- Cycles
- Self-loops
- Directed vs undirected

---

## Interview Strategy

### 1. Clarify (2-3 min)
- Understand input/output
- Ask about edge cases
- Clarify constraints

### 2. Example (2-3 min)
- Walk through examples
- Include edge cases
- Verify understanding

### 3. Approach (5-10 min)
- Identify pattern
- Explain approach
- Discuss complexity
- Consider alternatives

### 4. Code (15-20 min)
- Write clean code
- Think out loud
- Handle edge cases

### 5. Test (5-10 min)
- Test with examples
- Test edge cases
- Fix bugs

### 6. Optimize (5 min)
- Discuss improvements
- Time/space trade-offs

---

## Python Built-in Complexity

| Operation | Complexity |
|-----------|------------|
| list.append() | O(1) |
| list.pop() | O(1) |
| list.insert(0, x) | O(n) |
| list.index(x) | O(n) |
| list.sort() | O(n log n) |
| dict.get() | O(1) |
| dict[key] = val | O(1) |
| set.add() | O(1) |
| set.remove() | O(1) |
| x in set | O(1) |
| x in list | O(n) |

---

## Common Mistakes

1. ❌ Not handling edge cases
2. ❌ Wrong complexity analysis
3. ❌ Off-by-one errors
4. ❌ Not initializing variables
5. ❌ Infinite loops
6. ❌ Modifying list while iterating
7. ❌ Integer overflow (in other languages)
8. ❌ Not clarifying assumptions

---

## Quick Decision Tree

```
Is input sorted?
├─ Yes → Binary Search or Two Pointer
└─ No
   └─ Need to find subarray/substring?
      ├─ Yes → Sliding Window
      └─ No
         └─ Tree/Graph problem?
            ├─ Yes → DFS or BFS
            └─ No
               └─ Optimization problem?
                  ├─ Yes → Dynamic Programming
                  └─ No → Consider Backtracking, Heap, etc.
```

---

## Interview Checklist

Before coding:
- [ ] Understood problem completely
- [ ] Identified pattern
- [ ] Discussed approach with interviewer
- [ ] Mentioned time/space complexity
- [ ] Considered edge cases

While coding:
- [ ] Thinking out loud
- [ ] Writing clean code
- [ ] Using good variable names
- [ ] Adding comments if needed

After coding:
- [ ] Tested with examples
- [ ] Tested edge cases
- [ ] Analyzed complexity
- [ ] Discussed optimizations

---

Print this and keep it handy during practice sessions!
