# 3Sum

## Difficulty: 🟡 Medium

## Pattern: Two Pointer

## LeetCode: [#15](https://leetcode.com/problems/3sum/)

## Description

Given an integer array `nums`, return all the triplets `[nums[i], nums[j], nums[k]]` such that `i != j`, `i != k`, and `j != k`, and `nums[i] + nums[j] + nums[k] == 0`.

Notice that the solution set must not contain duplicate triplets.

## Examples

### Example 1:
```
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation:
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
```

### Example 2:
```
Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
```

### Example 3:
```
Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
```

## Constraints

- `3 <= nums.length <= 3000`
- `-10^5 <= nums[i] <= 10^5`

## Approach

**Pattern Recognition**: Extension of Two Sum with sorting:
- ✅ Fix one number, use two pointers for remaining two
- ✅ Sort first to enable two pointer technique
- ✅ Skip duplicates to avoid duplicate triplets

**Algorithm**:
1. Sort the array
2. For each number `nums[i]`:
   - Skip if duplicate of previous
   - Use two pointers (`left = i+1`, `right = n-1`)
   - Find pairs that sum to `-nums[i]`
   - Skip duplicates for all three positions
3. Return all unique triplets

## Complexity Analysis

- **Time Complexity**: O(n²)
  - O(n log n) for sorting
  - O(n²) for nested loops with two pointers
- **Space Complexity**: O(1) excluding output array

## Solution Location

[src/dsa/core_patterns/two_pointer.py](../../../src/dsa/core_patterns/two_pointer.py) - `three_sum()` method

## Related Problems

- **Two Sum** (LeetCode #1) - Easy
- **3Sum Closest** (LeetCode #16) - Medium
- **4Sum** (LeetCode #18) - Medium
- **3Sum Smaller** (LeetCode #259) - Medium

## Tags

`Array` `Two Pointers` `Sorting`
