# Search in Rotated Sorted Array

## Difficulty: 🟡 Medium

## Pattern: Binary Search

## LeetCode: [#33](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## Description

There is an integer array `nums` sorted in ascending order (with **distinct** values).

Prior to being passed to your function, `nums` is **possibly rotated** at an unknown pivot index `k` such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]`.

For example, `[0,1,2,4,5,6,7]` might be rotated at pivot index 3 and become `[4,5,6,7,0,1,2]`.

Given the array `nums` **after** the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples

### Example 1:
```
Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
```

### Example 2:
```
Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
```

### Example 3:
```
Input: nums = [1], target = 0
Output: -1
```

## Constraints

- `1 <= nums.length <= 5000`
- `-10^4 <= nums[i] <= 10^4`
- All values of `nums` are **unique**
- `nums` is an ascending array that is possibly rotated
- `-10^4 <= target <= 10^4`

## Approach

**Pattern Recognition**: Modified binary search on rotated array:
- ✅ One half is always sorted
- ✅ Determine which half is sorted
- ✅ Check if target is in sorted half

**Algorithm**:
1. Binary search with modification
2. At each step, determine which half is sorted
3. Check if target is in sorted half
4. Search appropriate half

## Complexity Analysis

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

## Solution Location

[src/dsa/core_patterns/binary_search.py](../../../src/dsa/core_patterns/binary_search.py) - `search_rotated_sorted_array()` method

## Related Problems

- **Search in Rotated Sorted Array II** (LeetCode #81) - Medium
- **Find Minimum in Rotated Sorted Array** (LeetCode #153) - Medium

## Tags

`Array` `Binary Search`
