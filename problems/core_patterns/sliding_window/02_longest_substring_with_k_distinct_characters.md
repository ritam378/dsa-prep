# Longest Substring with K Distinct Characters

## Difficulty: 🟡 Medium

## Pattern: Sliding Window

## LeetCode: [#340](https://leetcode.com/problems/)

## Description

Given a string, find the length of the longest substring with at most k distinct characters.

## Examples

### Example 1:
```
Input: s = "araaci", k = 2
Output: 4
Explanation: The longest substring with at most 2 distinct characters is "araa"
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
