# Fruits Into Baskets

## Difficulty: 🟡 Medium

## Pattern: Sliding Window

## LeetCode: [#904](https://leetcode.com/problems/)

## Description

Given an array where each element represents a fruit type, find the maximum number of fruits you can collect with only 2 baskets (each basket can only hold one type of fruit).

## Examples

### Example 1:
```
Input: fruits = [1,2,1]
Output: 3
Explanation: We can collect [1,2,1]
```

## Constraints

- See problem description for specific constraints

## Approach

**Pattern Recognition**: This is a **sliding window** problem because:
- Uses the sliding window technique
- Requires window management

**Algorithm**:
1. Initialize window/pointers
2. Expand/contract window based on conditions
3. Track optimal result
4. Return result

## Complexity Analysis

- **Time Complexity**: O(n)
- **Space Complexity**: O(k)

## Solution Location

[src/dsa/core_patterns/sliding_window.py](../../../src/dsa/core_patterns/sliding_window.py)

## Related Problems

See problem description for related problems.

## Tags

`Sliding Window, Array, String`
