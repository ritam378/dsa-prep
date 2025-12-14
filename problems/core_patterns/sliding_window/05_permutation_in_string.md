# Permutation in String

## Difficulty: 🟡 Medium

## Pattern: Sliding Window

## LeetCode: [#567](https://leetcode.com/problems/)

## Description

Given two strings s1 and s2, return true if s2 contains a permutation of s1.

## Examples

### Example 1:
```
Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains "ba" which is a permutation of s1
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
