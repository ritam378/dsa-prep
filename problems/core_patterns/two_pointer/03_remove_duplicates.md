# Remove Duplicates from Sorted Array

## Difficulty: 🟢 Easy

## Pattern: Two Pointer

## LeetCode: [#26](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## Description

Given an integer array `nums` sorted in **non-decreasing order**, remove the duplicates **in-place** such that each unique element appears only **once**. The **relative order** of the elements should be kept the **same**. Then return the number of unique elements in `nums`.

Consider the number of unique elements of `nums` to be `k`, to get accepted, you need to do the following things:

- Change the array `nums` such that the first `k` elements of `nums` contain the unique elements in the order they were present in `nums` initially.
- The remaining elements of `nums` are not important as well as the size of `nums`.
- Return `k`.

## Examples

### Example 1:
```
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
```

### Example 2:
```
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
```

## Constraints

- `1 <= nums.length <= 3 * 10^4`
- `-100 <= nums[i] <= 100`
- `nums` is sorted in **non-decreasing order**

## Approach

**Pattern Recognition**: Two pointer (read/write pointer) pattern:
- ✅ In-place modification required (O(1) space)
- ✅ Sorted array (duplicates adjacent)
- ✅ Need to maintain order while removing duplicates

**Algorithm**:
1. Use `write_pointer` starting at index 1
2. Use `read_pointer` to iterate through array
3. When `nums[read] != nums[read-1]`:
   - Copy to `nums[write]`
   - Increment `write_pointer`
4. Return `write_pointer` (number of unique elements)

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass
- **Space Complexity**: O(1) - In-place modification

## Solution Location

[src/dsa/core_patterns/two_pointer.py](../../../src/dsa/core_patterns/two_pointer.py) - `remove_duplicates()` method

## Related Problems

- **Remove Duplicates from Sorted Array II** (LeetCode #80) - Medium
- **Remove Element** (LeetCode #27) - Easy
- **Move Zeroes** (LeetCode #283) - Easy

## Tags

`Array` `Two Pointers`
