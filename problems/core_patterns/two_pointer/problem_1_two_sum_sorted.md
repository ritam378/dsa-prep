# Two Sum II - Input Array Is Sorted

## Difficulty: Easy

## Pattern: Two Pointer

## Description

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Return the indices of the two numbers (1-indexed) as an integer array.

You may assume that each input would have exactly one solution and you may not use the same element twice.

## Examples

### Example 1:
```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

### Example 2:
```
Input: numbers = [2,3,4], target = 6
Output: [1,3]
```

### Example 3:
```
Input: numbers = [-1,0], target = -1
Output: [1,2]
```

## Constraints

- `2 <= numbers.length <= 3 * 10^4`
- `-1000 <= numbers[i] <= 1000`
- `numbers` is sorted in non-decreasing order
- `-1000 <= target <= 1000`
- The tests are generated such that there is exactly one solution

## Approach

**Pattern Recognition**: This is a classic two pointer problem because:
- Array is sorted
- We need to find a pair with specific sum
- Can use two pointers from start and end

**Algorithm**:
1. Initialize two pointers: left at start, right at end
2. Calculate sum of elements at both pointers
3. If sum equals target, return indices
4. If sum is less than target, move left pointer right
5. If sum is greater than target, move right pointer left

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass through array
- **Space Complexity**: O(1) - Only two pointers used

## Solution Location

[src/dsa/core_patterns/two_pointer.py](../../../src/dsa/core_patterns/two_pointer.py#L25)

## Related Problems

- Two Sum (use hash map)
- 3Sum (Medium)
- 4Sum (Medium)
