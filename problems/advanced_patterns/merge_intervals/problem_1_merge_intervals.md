# Merge Intervals

## Difficulty: Medium

## Pattern: Merge Intervals

## Description

Given an array of intervals where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Examples

### Example 1:
```
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Intervals [1,3] and [2,6] overlap, so merge them into [1,6]
```

### Example 2:
```
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping
```

## Constraints

- `1 <= intervals.length <= 10^4`
- `intervals[i].length == 2`
- `0 <= start_i <= end_i <= 10^4`

## Approach

**Pattern Recognition**: This is a merge intervals problem because:
- We're dealing with ranges/intervals
- Need to identify and merge overlapping intervals
- Sorting helps identify overlaps

**Algorithm**:
1. Sort intervals by start time
2. Initialize result with first interval
3. For each interval:
   - If it overlaps with last merged interval, merge them
   - Otherwise, add it to result

**Key Insight**: Two intervals [a,b] and [c,d] overlap if a <= d and c <= b. After sorting, we only need to check if current start <= last end.

## Complexity Analysis

- **Time Complexity**: O(n log n) - Dominated by sorting
- **Space Complexity**: O(n) - For result array

## Solution Location

[src/dsa/advanced_patterns/merge_intervals.py](../../../src/dsa/advanced_patterns/merge_intervals.py#L18)

## Related Problems

- Insert Interval
- Meeting Rooms
- Meeting Rooms II
- Non-overlapping Intervals
