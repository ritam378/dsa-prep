# Find First and Last Position of Element in Sorted Array

## Difficulty: 🟡 Medium

## Pattern: Binary Search

## LeetCode: [#34](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)

## Description

Given an array of integers `nums` sorted in non-decreasing order, find the starting and ending position of a given `target` value.

If `target` is not found in the array, return `[-1, -1]`.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples

### Example 1:
```
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
```

### Example 2:
```
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
```

### Example 3:
```
Input: nums = [], target = 0
Output: [-1,-1]
```

## Constraints

- `0 <= nums.length <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- `nums` is a non-decreasing array
- `-10^9 <= target <= 10^9`

## Approach

**Pattern Recognition**: Modified binary search:
- ✅ Find first occurrence - binary search biased left
- ✅ Find last occurrence - binary search biased right
- ✅ Run binary search twice

**Algorithm**:
1. Find first occurrence:
   - When found, continue searching left half
2. Find last occurrence:
   - When found, continue searching right half
3. Return `[first, last]`

## Complexity Analysis

- **Time Complexity**: O(log n) - Two binary searches
- **Space Complexity**: O(1)

## Solution Location

[src/dsa/core_patterns/binary_search.py](../../../src/dsa/core_patterns/binary_search.py) - `find_first_occurrence()` and `find_last_occurrence()` methods

## Related Problems

- **First Bad Version** (LeetCode #278) - Easy
- **Count of Range Sum** (LeetCode #327) - Hard

## Tags

`Array` `Binary Search`
