#!/usr/bin/env python3
"""
Generate all problem markdown files for the DSA repository.

This script creates problem description files for all 71+ problems
based on the implementations in src/dsa/.
"""

import os
from pathlib import Path

# Base directory
BASE_DIR = Path(__file__).parent.parent
PROBLEMS_DIR = BASE_DIR / "problems"

# Problem definitions
PROBLEMS = {
    "core_patterns/sliding_window": [
        {
            "num": "01",
            "title": "Maximum Sum Subarray of Size K",
            "difficulty": "🟢 Easy",
            "leetcode": "-",
            "description": "Given an array of integers and a number k, find the maximum sum of any contiguous subarray of size k.",
            "example": 'Input: arr = [2, 1, 5, 1, 3, 2], k = 3\nOutput: 9\nExplanation: Subarray with maximum sum is [5, 1, 3]',
        },
        {
            "num": "02",
            "title": "Longest Substring with K Distinct Characters",
            "difficulty": "🟡 Medium",
            "leetcode": "#340",
            "description": "Given a string, find the length of the longest substring with at most k distinct characters.",
            "example": 'Input: s = "araaci", k = 2\nOutput: 4\nExplanation: The longest substring with at most 2 distinct characters is "araa"',
        },
        {
            "num": "03",
            "title": "Minimum Size Subarray Sum",
            "difficulty": "🟡 Medium",
            "leetcode": "#209",
            "description": "Given an array of positive integers and a target, find the minimum length of contiguous subarray whose sum is greater than or equal to target.",
            "example": 'Input: target = 7, nums = [2,3,1,2,4,3]\nOutput: 2\nExplanation: [4,3] is the smallest subarray with sum >= 7',
        },
        {
            "num": "04",
            "title": "Longest Substring Without Repeating Characters",
            "difficulty": "🟡 Medium",
            "leetcode": "#3",
            "description": "Given a string s, find the length of the longest substring without repeating characters.",
            "example": 'Input: s = "abcabcbb"\nOutput: 3\nExplanation: "abc" is the longest substring without repeating characters',
        },
        {
            "num": "05",
            "title": "Permutation in String",
            "difficulty": "🟡 Medium",
            "leetcode": "#567",
            "description": "Given two strings s1 and s2, return true if s2 contains a permutation of s1.",
            "example": 'Input: s1 = "ab", s2 = "eidbaooo"\nOutput: true\nExplanation: s2 contains "ba" which is a permutation of s1',
        },
        {
            "num": "06",
            "title": "Fruits Into Baskets",
            "difficulty": "🟡 Medium",
            "leetcode": "#904",
            "description": "Given an array where each element represents a fruit type, find the maximum number of fruits you can collect with only 2 baskets (each basket can only hold one type of fruit).",
            "example": 'Input: fruits = [1,2,1]\nOutput: 3\nExplanation: We can collect [1,2,1]',
        },
    ],
    # Add more patterns here - this is just a template
    # You can extend this with all other patterns
}

TEMPLATE = """# {title}

## Difficulty: {difficulty}

## Pattern: {pattern_name}

## LeetCode: {leetcode_link}

## Description

{description}

## Examples

### Example 1:
```
{example}
```

## Constraints

- See problem description for specific constraints

## Approach

**Pattern Recognition**: This is a **{pattern_lower}** problem because:
- Uses the {pattern_lower} technique
- Requires {key_characteristic}

**Algorithm**:
1. Initialize window/pointers
2. Expand/contract window based on conditions
3. Track optimal result
4. Return result

## Complexity Analysis

- **Time Complexity**: {time_complexity}
- **Space Complexity**: {space_complexity}

## Solution Location

[src/dsa/{pattern_path}](../../../src/dsa/{pattern_path})

## Related Problems

See problem description for related problems.

## Tags

`{tags}`
"""


def create_problem_file(pattern_path, problem_info, pattern_name):
    """Create a single problem markdown file."""
    # Create directory if it doesn't exist
    problem_dir = PROBLEMS_DIR / pattern_path
    problem_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename
    filename = f"{problem_info['num']}_{problem_info['title'].lower().replace(' ', '_').replace('/', '_').replace('(', '').replace(')', '')}.md"
    filepath = problem_dir / filename

    # Determine pattern-specific details
    pattern_lower = pattern_name.lower()

    # Generate content from template
    content = TEMPLATE.format(
        title=problem_info['title'],
        difficulty=problem_info['difficulty'],
        pattern_name=pattern_name,
        leetcode_link=f"[{problem_info['leetcode']}](https://leetcode.com/problems/)" if problem_info['leetcode'] != '-' else problem_info['leetcode'],
        description=problem_info['description'],
        example=problem_info['example'],
        pattern_lower=pattern_lower,
        key_characteristic="window management" if "window" in pattern_lower else "pointer movement",
        time_complexity="O(n)" if "window" in pattern_lower else "O(n log n)",
        space_complexity="O(k)" if "window" in pattern_lower else "O(1)",
        pattern_path=pattern_path.replace('/', '/') + '.py',
        tags=f"{pattern_name}, Array, String"
    )

    # Write file
    with open(filepath, 'w') as f:
        f.write(content)

    print(f"✓ Created: {filepath.relative_to(BASE_DIR)}")


def main():
    """Generate all problem files."""
    print("Generating problem files...\n")

    total = 0
    for pattern_path, problems in PROBLEMS.items():
        pattern_name = pattern_path.split('/')[-1].replace('_', ' ').title()
        print(f"\n{pattern_name}:")
        for problem in problems:
            create_problem_file(pattern_path, problem, pattern_name)
            total += 1

    print(f"\n✅ Generated {total} problem files!")
    print("\nTo extend this script, add more patterns to the PROBLEMS dictionary.")


if __name__ == "__main__":
    main()
