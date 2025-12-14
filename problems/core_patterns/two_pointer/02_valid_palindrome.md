# Valid Palindrome

## Difficulty: 🟢 Easy

## Pattern: Two Pointer

## LeetCode: [#125](https://leetcode.com/problems/valid-palindrome/)

## Description

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a **palindrome**, or `false` otherwise.

## Examples

### Example 1:
```
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
```

### Example 2:
```
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
```

### Example 3:
```
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

## Constraints

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters

## Approach

**Pattern Recognition**: Two pointer pattern because:
- ✅ Need to compare characters from both ends
- ✅ Move inward simultaneously
- ✅ Can skip non-alphanumeric characters efficiently

**Algorithm**:
1. Initialize `left = 0`, `right = len(s) - 1`
2. While `left < right`:
   - Skip non-alphanumeric characters from left
   - Skip non-alphanumeric characters from right
   - Compare characters (case-insensitive)
   - If not equal, return `false`
   - Move both pointers inward
3. Return `true` if all comparisons passed

## Complexity Analysis

- **Time Complexity**: O(n) - Single pass with two pointers
- **Space Complexity**: O(1) - Only pointer variables

## Solution Location

[src/dsa/core_patterns/two_pointer.py](../../../src/dsa/core_patterns/two_pointer.py) - `is_palindrome()` method

## Related Problems

- **Valid Palindrome II** (LeetCode #680) - Medium
- **Palindrome Linked List** (LeetCode #234) - Easy
- **Longest Palindromic Substring** (LeetCode #5) - Medium

## Tags

`Two Pointers` `String`
