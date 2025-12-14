# Time Complexity Analysis Guide

Complete guide to analyzing time and space complexity.

## Big O Notation

### What is Big O?

Big O notation describes the upper bound of time or space complexity in terms of input size n.

### Common Complexities (Best to Worst)

| Notation | Name | Example | Description |
|----------|------|---------|-------------|
| O(1) | Constant | Array access, hash table lookup | Fixed time |
| O(log n) | Logarithmic | Binary search | Halves each iteration |
| O(n) | Linear | Linear search, single loop | Proportional to input |
| O(n log n) | Linearithmic | Merge sort, quick sort | Efficient sorting |
| O(n²) | Quadratic | Nested loops, bubble sort | Grows quickly |
| O(n³) | Cubic | Triple nested loops | Very slow |
| O(2^n) | Exponential | Fibonacci (naive), subsets | Extremely slow |
| O(n!) | Factorial | Permutations | Impossibly slow for large n |

### Visual Growth Rates

For n = 100:
- O(1) = 1 operation
- O(log n) ≈ 7 operations
- O(n) = 100 operations
- O(n log n) ≈ 664 operations
- O(n²) = 10,000 operations
- O(2^n) = 1.27 × 10³⁰ operations
- O(n!) = Way too many!

---

## How to Calculate Time Complexity

### Rule 1: Drop Constants

O(2n) → O(n)
O(n/2) → O(n)
O(100) → O(1)

### Rule 2: Drop Non-Dominant Terms

O(n² + n) → O(n²)
O(n + log n) → O(n)
O(5n² + 3n + 20) → O(n²)

### Rule 3: Different Inputs Use Different Variables

```python
def func(arr1, arr2):
    for x in arr1:  # O(n)
        print(x)
    for y in arr2:  # O(m)
        print(y)
# Total: O(n + m), NOT O(n)
```

### Rule 4: Multiplication for Nested Loops

```python
for i in range(n):      # O(n)
    for j in range(m):  # O(m)
        print(i, j)
# Total: O(n × m)
```

---

## Common Patterns

### Loops

#### Single Loop
```python
for i in range(n):
    print(i)
# O(n)
```

#### Nested Loops
```python
for i in range(n):
    for j in range(n):
        print(i, j)
# O(n²)
```

#### Sequential Loops
```python
for i in range(n):
    print(i)
for j in range(m):
    print(j)
# O(n + m)
```

### Recursion

#### Single Recursive Call
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)
# O(n) - n recursive calls
```

#### Multiple Recursive Calls
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
# O(2^n) - exponential tree
```

#### With Memoization
```python
def fib_memo(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]
# O(n) - each subproblem solved once
```

---

## Analyzing Common Algorithms

### Binary Search
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
# O(log n) - halves search space each iteration
```

### Merge Sort
```python
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])   # T(n/2)
    right = merge_sort(arr[mid:])  # T(n/2)
    return merge(left, right)      # O(n)
# O(n log n) - log n levels, n work per level
```

### Two Pointer
```python
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    while left < right:
        current_sum = arr[left] + arr[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []
# O(n) - single pass through array
```

### Sliding Window
```python
def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i-k] + arr[i]
        max_sum = max(max_sum, window_sum)
    return max_sum
# O(n) - single pass
```

---

## Space Complexity

### Types of Space

1. **Input Space**: Space for input (usually not counted)
2. **Auxiliary Space**: Extra space used by algorithm
3. **Total Space**: Input + Auxiliary

When we say space complexity, we usually mean **auxiliary space**.

### Common Space Complexities

#### O(1) - Constant
```python
def sum_array(arr):
    total = 0  # O(1) space
    for num in arr:
        total += num
    return total
```

#### O(n) - Linear
```python
def copy_array(arr):
    new_arr = []  # O(n) space
    for num in arr:
        new_arr.append(num)
    return new_arr
```

#### O(log n) - Logarithmic
```python
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    # ... recursion
# O(log n) space for recursion stack
```

#### O(n²) - Quadratic
```python
def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]  # O(n²) space
    return matrix
```

---

## Advanced Analysis

### Amortized Analysis

Some operations may be expensive occasionally but cheap on average.

**Example: Dynamic Array**
- Append: Usually O(1)
- When full, resize: O(n)
- Amortized: O(1)

### Best, Average, Worst Case

**Quick Sort**:
- Best: O(n log n) - balanced partitions
- Average: O(n log n)
- Worst: O(n²) - already sorted with bad pivot

**Binary Search Tree**:
- Best/Average: O(log n) - balanced
- Worst: O(n) - skewed tree

---

## Pattern-Specific Complexities

### Two Pointer
- **Time**: O(n)
- **Space**: O(1)
- Each element processed once

### Sliding Window
- **Time**: O(n)
- **Space**: O(k) where k is window size
- Each element enters and leaves window once

### Binary Search
- **Time**: O(log n)
- **Space**: O(1) iterative, O(log n) recursive
- Search space halved each step

### DFS/BFS
- **Time**: O(V + E) where V = vertices, E = edges
- **Space**: O(V) for visited set
- Each vertex and edge visited once

### Dynamic Programming
- **Time**: O(states × transitions)
- **Space**: O(states)
- Example: Fibonacci: O(n) time and space

### Backtracking
- **Time**: O(2^n) for subsets, O(n!) for permutations
- **Space**: O(n) for recursion stack
- Explores all possibilities

---

## How to Improve Complexity

### Time Optimization Techniques

1. **Use Hash Table**: O(n) instead of O(n²)
```python
# O(n²)
for i in range(n):
    for j in range(n):
        if arr[i] == arr[j]:
            # ...

# O(n) with hash table
seen = set()
for num in arr:
    if num in seen:
        # ...
    seen.add(num)
```

2. **Sort First**: O(n log n) instead of O(n²)
```python
# Two Sum: O(n²)
for i in range(n):
    for j in range(i+1, n):
        if arr[i] + arr[j] == target:
            # ...

# O(n log n) with sorting + two pointer
arr.sort()
left, right = 0, len(arr) - 1
# ... two pointer logic
```

3. **Use Dynamic Programming**: O(n) instead of O(2^n)
```python
# O(2^n) - naive recursion
def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

# O(n) - with memoization
def fib_dp(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### Space Optimization Techniques

1. **In-place Modification**: O(1) instead of O(n)
```python
# O(n) space
def reverse_copy(arr):
    return arr[::-1]

# O(1) space
def reverse_inplace(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
```

2. **Use Constant Space DP**: O(1) instead of O(n)
```python
# O(n) space
def fib_array(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

# O(1) space
def fib_optimized(n):
    if n <= 1:
        return n
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr
```

---

## Interview Tips

### During Interview

1. **Always state complexity**: Don't make interviewer ask
2. **Explain your reasoning**: Show how you calculated
3. **Mention both time and space**: Both matter
4. **Consider trade-offs**: Sometimes time vs space trade-off

### Common Questions

**Q: "What's the time complexity?"**
- Walk through code line by line
- Identify loops and recursion
- Apply Big O rules

**Q: "Can you optimize this?"**
- Identify bottleneck
- Consider hash tables, sorting, DP
- Discuss trade-offs

**Q: "What about space complexity?"**
- Count extra data structures
- Consider recursion stack
- Mention in-place possibilities

---

## Practice Problems

Analyze complexity of:

1. Two Sum (Hash Map approach)
2. Binary Search Tree Search
3. Merge K Sorted Lists
4. Course Schedule (Topological Sort)
5. Longest Increasing Subsequence (DP)

---

## Complexity Decision Tree

```
How many elements processed?
├─ Constant → O(1)
├─ All once → O(n)
├─ All twice → O(n) - still linear
├─ Nested all × all → O(n²)
└─ Halving search space → O(log n)

Recursion?
├─ Single call, -1 each time → O(n)
├─ Two calls, -1 each time → O(2^n)
├─ Divide and conquer → O(n log n)
└─ With memoization → count unique states
```

---

Remember: In interviews, it's better to give a slightly loose bound quickly than to spend 5 minutes calculating the exact complexity!
