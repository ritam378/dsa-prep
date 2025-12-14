# Search Insert Position

## Difficulty: 🟢 Easy

## Pattern: Binary Search

## LeetCode: [#35](https://leetcode.com/problems/search-insert-position/)

## Description

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with `O(log n)` runtime complexity.

## Examples

### Example 1:
```
Input: nums = [1,3,5,6], target = 5
Output: 2
```

### Example 2:
```
Input: nums = [1,3,5,6], target = 2
Output: 1
```

### Example 3:
```
Input: nums = [1,3,5,6], target = 7
Output: 4
```

## Constraints

- `1 <= nums.length <= 10^4`
- `-10^4 <= nums[i] <= 10^4`
- `nums` contains **distinct** values sorted in **ascending** order
- `-10^4 <= target <= 10^4`

## Approach

**Pattern Recognition**: Binary search with insertion point:
- ✅ Find exact match or insertion position
- ✅ Standard binary search with slight modification
- ✅ Return left pointer if not found (insertion point)

**Algorithm**:
1. Binary search for target
2. If found, return index
3. If not found, return left pointer (insertion position)

## Complexity Analysis

- **Time Complexity**: O(log n)
- **Space Complexity**: O(1)

## Solution Location

[src/dsa/core_patterns/binary_search.py](../../../src/dsa/core_patterns/binary_search.py)

## Related Problems

- **First Bad Version** (LeetCode #278) - Easy
- **Binary Search** (LeetCode #704) - Easy

## Tags

`Array` `Binary Search`
