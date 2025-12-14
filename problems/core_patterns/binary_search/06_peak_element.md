# Find Peak Element

## Difficulty: 🟡 Medium

## Pattern: Binary Search

## LeetCode: [#162](https://leetcode.com/problems/find-peak-element/)

## Description

A peak element is an element that is strictly greater than its neighbors.

Given a **0-indexed** integer array `nums`, find a peak element, and return its index. If the array contains multiple peaks, return the index to **any of the peaks**.

You may imagine that `nums[-1] = nums[n] = -∞`. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in `O(log n)` time.

## Examples

### Example 1:
```
Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
```

### Example 2:
```
Input: nums = [1,2,1,3,5,6,4]
Output: 5
Explanation: Your function can return either index 1 where the peak element is 2, or index 5 where the peak element is 6.
```

## Constraints

- `1 <= nums.length <= 1000`
- `-2^31 <= nums[i] <= 2^31 - 1`
- `nums[i] != nums[i + 1]` for all valid `i`

## Approach

**Pattern Recognition**: Binary search to find peak:
- ✅ If nums[mid] > nums[mid+1], peak is in left half (including mid)
- ✅ Else, peak is in right half
- ✅ Always moves toward higher values

**Algorithm**:
1. Binary search
2. Compare nums[mid] with nums[mid+1]
3. Move toward increasing side
4. Converge to peak

## Complexity Analysis

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

## Solution Location

[src/dsa/core_patterns/binary_search.py](../../../src/dsa/core_patterns/binary_search.py) - `find_peak_element()` method

## Related Problems

- **Find Peak Element II** (LeetCode #1901) - Medium
- **Peak Index in a Mountain Array** (LeetCode #852) - Medium

## Tags

`Array` `Binary Search`
