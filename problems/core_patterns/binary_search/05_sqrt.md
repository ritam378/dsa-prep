# Sqrt(x)

## Difficulty: 🟢 Easy

## Pattern: Binary Search

## LeetCode: [#69](https://leetcode.com/problems/sqrtx/)

## Description

Given a non-negative integer `x`, return the square root of `x` rounded down to the nearest integer. The returned integer should be **non-negative** as well.

You **must not use** any built-in exponent function or operator.

## Examples

### Example 1:
```
Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
```

### Example 2:
```
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round down, 2 is returned.
```

## Constraints

- `0 <= x <= 2^31 - 1`

## Approach

**Pattern Recognition**: Binary search on answer space:
- ✅ Search for largest integer whose square ≤ x
- ✅ Search space: [0, x]
- ✅ Binary search to find answer

**Algorithm**:
1. Binary search from 0 to x
2. Check if mid * mid equals/exceeds x
3. Narrow search based on comparison
4. Return floor value

## Complexity Analysis

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

## Solution Location

[src/dsa/core_patterns/binary_search.py](../../../src/dsa/core_patterns/binary_search.py) - `sqrt()` method

## Related Problems

- **Pow(x, n)** (LeetCode #50) - Medium
- **Valid Perfect Square** (LeetCode #367) - Easy

## Tags

`Math` `Binary Search`
