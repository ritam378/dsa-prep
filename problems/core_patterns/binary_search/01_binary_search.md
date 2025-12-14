# Binary Search

## Difficulty: 🟢 Easy

## Pattern: Binary Search

## LeetCode: [#704](https://leetcode.com/problems/binary-search/)

## Description

Given an array of integers `nums` which is sorted in ascending order, and an integer `target`, write a function to search `target` in `nums`. If `target` exists, then return its index. Otherwise, return `-1`.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples

### Example 1:
```
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
```

### Example 2:
```
Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 < nums[i], target < 10^4`
- All integers in `nums` are **unique**
- `nums` is sorted in ascending order

## Approach

**Pattern Recognition**: Classic binary search:
- ✅ Sorted array
- ✅ Search for specific element
- ✅ Need O(log n) time

**Algorithm**:
1. Initialize `left = 0`, `right = len(nums) - 1`
2. While `left <= right`:
   - Calculate `mid = left + (right - left) // 2`
   - If `nums[mid] == target`: return `mid`
   - If `nums[mid] < target`: search right half (`left = mid + 1`)
   - If `nums[mid] > target`: search left half (`right = mid - 1`)
3. Return `-1` if not found

## Complexity Analysis

- **Time Complexity**: O(log n) - Divide search space by 2 each iteration
- **Space Complexity**: O(1) - Only variables used

## Solution Location

[src/dsa/core_patterns/binary_search.py](../../../src/dsa/core_patterns/binary_search.py) - `binary_search()` method

## Related Problems

- **First Bad Version** (LeetCode #278) - Easy
- **Search Insert Position** (LeetCode #35) - Easy
- **Find Smallest Letter Greater Than Target** (LeetCode #744) - Easy

## Tags

`Array` `Binary Search`
