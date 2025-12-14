# Maximum Sum Subarray of Size K

## Difficulty: Easy

## Pattern: Sliding Window

## Description

Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.

## Examples

### Example 1:
```
Input: arr = [2, 1, 5, 1, 3, 2], k = 3
Output: 9
Explanation: Subarray with maximum sum is [5, 1, 3]
```

### Example 2:
```
Input: arr = [2, 3, 4, 1, 5], k = 2
Output: 7
Explanation: Subarray with maximum sum is [3, 4]
```

## Constraints

- `1 <= arr.length <= 10^5`
- `-10^4 <= arr[i] <= 10^4`
- `1 <= k <= arr.length`

## Approach

**Pattern Recognition**: This is a sliding window problem because:
- We need to find something about a contiguous subarray
- The subarray has a fixed size (k)
- We can efficiently slide a window through the array

**Algorithm**:
1. Calculate sum of first k elements (initial window)
2. Slide the window by:
   - Removing leftmost element
   - Adding new rightmost element
3. Track maximum sum seen

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass through array
- **Space Complexity**: O(1) - Only variables for sum tracking

## Solution Location

[src/dsa/core_patterns/sliding_window.py](../../../src/dsa/core_patterns/sliding_window.py#L20)

## Related Problems

- Minimum Size Subarray Sum
- Longest Substring with K Distinct Characters
- Maximum Average Subarray
