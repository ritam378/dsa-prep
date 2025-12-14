# Longest Substring Without Repeating Characters

## Difficulty: 🟡 Medium

## Pattern: Sliding Window

## LeetCode: [#3](https://leetcode.com/problems/)

## Description

Given a string s, find the length of the longest substring without repeating characters.

## Examples

### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: "abc" is the longest substring without repeating characters
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
