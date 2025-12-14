# Minimum Size Subarray Sum

## Difficulty: 🟡 Medium

## Pattern: Sliding Window

## LeetCode: [#209](https://leetcode.com/problems/)

## Description

Given an array of positive integers and a target, find the minimum length of contiguous subarray whose sum is greater than or equal to target.

## Examples

### Example 1:
```
Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: [4,3] is the smallest subarray with sum >= 7
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
