# Container With Most Water

## Difficulty: 🟡 Medium

## Pattern: Two Pointer

## LeetCode: [#11](https://leetcode.com/problems/container-with-most-water/)

## Description

You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i`th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

**Notice** that you may not slant the container.

## Examples

### Example 1:
```
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The vertical lines are [1,8,6,2,5,4,8,3,7].
The max area is between index 1 and 8: min(8,7) * (8-1) = 7 * 7 = 49.
```

### Example 2:
```
Input: height = [1,1]
Output: 1
```

## Constraints

- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`

## Approach

**Pattern Recognition**: Two pointer optimization problem:
- ✅ Need to maximize area = min(height[i], height[j]) × (j - i)
- ✅ Start with maximum width, move pointers to potentially increase height
- ✅ Move pointer with smaller height (greedy approach)

**Algorithm**:
1. Initialize `left = 0`, `right = n-1`, `max_area = 0`
2. While `left < right`:
   - Calculate `area = min(height[left], height[right]) × (right - left)`
   - Update `max_area` if current area is larger
   - Move the pointer with smaller height inward
3. Return `max_area`

**Why Move Smaller Height?**
- Width decreases as pointers move inward
- To increase area, we need to potentially increase height
- Moving the smaller height gives possibility of finding taller line

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass with two pointers
- **Space Complexity**: O(1) - Only variables

## Solution Location

[src/dsa/core_patterns/two_pointer.py](../../../src/dsa/core_patterns/two_pointer.py) - `container_with_most_water()` method

## Related Problems

- **Trapping Rain Water** (LeetCode #42) - Hard
- **Largest Rectangle in Histogram** (LeetCode #84) - Hard
- **Maximal Rectangle** (LeetCode #85) - Hard

## Tags

`Array` `Two Pointers` `Greedy`
