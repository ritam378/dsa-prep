# Maximum Sum Subarray of Size K

## Difficulty: 🟢 Easy

## Pattern: Sliding Window

## LeetCode: -

## Description

Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

## Examples

### Example 1:
```
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3]
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
