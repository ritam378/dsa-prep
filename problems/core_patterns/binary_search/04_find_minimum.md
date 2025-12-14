# Find Minimum in Rotated Sorted Array

## Difficulty: 🟡 Medium

## Pattern: Binary Search

## LeetCode: [#153](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## Description

Suppose an array of length `n` sorted in ascending order is **rotated** between `1` and `n` times.

Given the sorted rotated array `nums` of **unique** elements, return the minimum element of this array.

You must write an algorithm that runs in `O(log n)` time.

## Examples

### Example 1:
```
Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

### Example 2:
```
Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

### Example 3:
```
Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

## Constraints

- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All integers of `nums` are **unique**
- `nums` is sorted and rotated between `1` and `n` times

## Approach

**Pattern Recognition**: Binary search for minimum in rotated array:
- ✅ Minimum is at the rotation point
- ✅ Compare mid with right to determine which half has minimum

**Algorithm**:
1. Binary search: compare `nums[mid]` with `nums[right]`
2. If `nums[mid] > nums[right]`: minimum is in right half
3. Else: minimum is in left half (including mid)
4. Converge to minimum element

## Complexity Analysis

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

## Solution Location

[src/dsa/core_patterns/binary_search.py](../../../src/dsa/core_patterns/binary_search.py) - `find_minimum_rotated_array()` method

## Related Problems

- **Find Minimum in Rotated Sorted Array II** (LeetCode #154) - Hard
- **Search in Rotated Sorted Array** (LeetCode #33) - Medium

## Tags

`Array` `Binary Search`
