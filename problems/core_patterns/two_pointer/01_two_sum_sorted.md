# Two Sum II - Input Array Is Sorted

## Difficulty: 🟢 Easy

## Pattern: Two Pointer

## LeetCode: [#167](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## Description

Given a **1-indexed** array of integers `numbers` that is already **sorted in non-decreasing order**, find two numbers such that they add up to a specific `target` number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 <= numbers.length`.

Return the indices of the two numbers, `index1` and `index2`, added by one as an integer array `[index1, index2]` of length 2.

The tests are generated such that there is **exactly one solution**. You **may not** use the same element twice.

Your solution must use only constant extra space.

## Examples

### Example 1:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
```

### Example 2:
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
```

### Example 3:
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
```

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in **non-decreasing order**
- `-1000 <= target <= 1000`
- The tests are generated such that there is **exactly one solution**

## Approach

**Pattern Recognition**: This is a classic **two pointer** problem because:
- ✅ Array is sorted
- ✅ We need to find a pair with specific sum
- ✅ Can efficiently use two pointers from start and end

**Algorithm**:
1. Initialize two pointers: `left` at start (0), `right` at end (n-1)
2. While `left < right`:
   - Calculate `current_sum = numbers[left] + numbers[right]`
   - If `current_sum == target`: Found! Return `[left+1, right+1]` (1-indexed)
   - If `current_sum < target`: Move `left` pointer right (need larger sum)
   - If `current_sum > target`: Move `right` pointer left (need smaller sum)

**Why This Works**:
- Since array is sorted, moving `left` right increases sum
- Moving `right` left decreases sum
- We systematically explore all possible pairs in O(n) time

## Complexity Analysis

- **Time Complexity**: O(n)
  - Single pass through array with two pointers
  - Each element visited at most once

- **Space Complexity**: O(1)
  - Only two pointer variables used
  - No extra data structures

## Solution Location

[src/dsa/core_patterns/two_pointer.py](../../../src/dsa/core_patterns/two_pointer.py) - `two_sum_sorted()` method

## Test Location

[tests/test_core_patterns/test_two_pointer.py](../../../tests/test_core_patterns/test_two_pointer.py) - `test_two_sum_sorted()`

## Related Problems

- **Two Sum** (LeetCode #1) - Use hash map for unsorted array
- **3Sum** (LeetCode #15) - Medium - Extend to three numbers
- **4Sum** (LeetCode #18) - Medium - Extend to four numbers
- **3Sum Closest** (LeetCode #16) - Medium - Find closest sum

## Tags

`Array` `Two Pointers` `Binary Search`

## Companies

Amazon, Microsoft, Facebook, Google, Apple

## Hints

<details>
<summary>Hint 1</summary>
Use the fact that the array is sorted. What data structure allows you to efficiently check both ends?
</details>

<details>
<summary>Hint 2</summary>
Try using two pointers - one at the beginning and one at the end. Move them based on whether the sum is too large or too small.
</details>

<details>
<summary>Hint 3</summary>
Since there's exactly one solution, you don't need to handle edge cases where no solution exists.
</details>
