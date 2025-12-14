#!/usr/bin/env python3
"""
Create all remaining problem markdown files.
Run from project root: python3 scripts/create_remaining_problems.py
"""

import os
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent
PROBLEMS_DIR = BASE_DIR / "problems"

# All remaining problems to create
PROBLEMS = [
    # DFS Problems (6)
    ("core_patterns/dfs", "01", "Maximum Depth of Binary Tree", "🟢 Easy", "#104", "DFS"),
    ("core_patterns/dfs", "02", "Validate Binary Search Tree", "🟡 Medium", "#98", "DFS"),
    ("core_patterns/dfs", "03", "Path Sum", "🟢 Easy", "#112", "DFS"),
    ("core_patterns/dfs", "04", "Path Sum II (All Paths)", "🟡 Medium", "#113", "DFS"),
    ("core_patterns/dfs", "05", "Number of Islands", "🟡 Medium", "#200", "DFS"),
    ("core_patterns/dfs", "06", "Course Schedule (Cycle Detection)", "🟡 Medium", "#207", "DFS"),

    # BFS Problems (6)
    ("core_patterns/bfs", "01", "Binary Tree Level Order Traversal", "🟡 Medium", "#102", "BFS"),
    ("core_patterns/bfs", "02", "Minimum Depth of Binary Tree", "🟢 Easy", "#111", "BFS"),
    ("core_patterns/bfs", "03", "Binary Tree Zigzag Level Order Traversal", "🟡 Medium", "#103", "BFS"),
    ("core_patterns/bfs", "04", "Binary Tree Right Side View", "🟡 Medium", "#199", "BFS"),
    ("core_patterns/bfs", "05", "Shortest Path in Binary Matrix", "🟡 Medium", "#1091", "BFS"),
    ("core_patterns/bfs", "06", "Word Ladder", "🔴 Hard", "#127", "BFS"),

    # Backtracking Problems (4)
    ("core_patterns/backtracking", "01", "Subsets", "🟡 Medium", "#78", "Backtracking"),
    ("core_patterns/backtracking", "02", "Permutations", "🟡 Medium", "#46", "Backtracking"),
    ("core_patterns/backtracking", "03", "Combination Sum", "🟡 Medium", "#39", "Backtracking"),
    ("core_patterns/backtracking", "04", "Generate Parentheses", "🟡 Medium", "#22", "Backtracking"),

    # Dynamic Programming Problems (7)
    ("core_patterns/dynamic_programming", "01", "Fibonacci Number", "🟢 Easy", "#509", "Dynamic Programming"),
    ("core_patterns/dynamic_programming", "02", "Climbing Stairs", "🟢 Easy", "#70", "Dynamic Programming"),
    ("core_patterns/dynamic_programming", "03", "Coin Change", "🟡 Medium", "#322", "Dynamic Programming"),
    ("core_patterns/dynamic_programming", "04", "Longest Increasing Subsequence", "🟡 Medium", "#300", "Dynamic Programming"),
    ("core_patterns/dynamic_programming", "05", "Maximum Subarray (Kadane's Algorithm)", "🟡 Medium", "#53", "Dynamic Programming"),
    ("core_patterns/dynamic_programming", "06", "House Robber", "🟡 Medium", "#198", "Dynamic Programming"),
    ("core_patterns/dynamic_programming", "07", "0/1 Knapsack", "🟡 Medium", "-", "Dynamic Programming"),

    # Fast & Slow Pointer Problems (3)
    ("core_patterns/fast_slow_pointer", "01", "Linked List Cycle", "🟢 Easy", "#141", "Fast & Slow Pointer"),
    ("core_patterns/fast_slow_pointer", "02", "Middle of Linked List", "🟢 Easy", "#876", "Fast & Slow Pointer"),
    ("core_patterns/fast_slow_pointer", "03", "Happy Number", "🟢 Easy", "#202", "Fast & Slow Pointer"),

    # Advanced Patterns - Merge Intervals (3)
    ("advanced_patterns/merge_intervals", "01", "Merge Intervals", "🟡 Medium", "#56", "Merge Intervals"),
    ("advanced_patterns/merge_intervals", "02", "Insert Interval", "🟡 Medium", "#57", "Merge Intervals"),
    ("advanced_patterns/merge_intervals", "03", "Meeting Rooms", "🟢 Easy", "#252", "Merge Intervals"),

    # Advanced Patterns - Heap (3)
    ("advanced_patterns/heap", "01", "Kth Largest Element in an Array", "🟡 Medium", "#215", "Heap"),
    ("advanced_patterns/heap", "02", "K Closest Points to Origin", "🟡 Medium", "#973", "Heap"),
    ("advanced_patterns/heap", "03", "Top K Frequent Elements", "🟡 Medium", "#347", "Heap"),

    # Advanced Patterns - Monotonic Stack (3)
    ("advanced_patterns/monotonic_stack", "01", "Next Greater Element", "🟢 Easy", "#496", "Monotonic Stack"),
    ("advanced_patterns/monotonic_stack", "02", "Daily Temperatures", "🟡 Medium", "#739", "Monotonic Stack"),
    ("advanced_patterns/monotonic_stack", "03", "Largest Rectangle in Histogram", "🔴 Hard", "#84", "Monotonic Stack"),

    # Advanced Patterns - Union Find (2)
    ("advanced_patterns/union_find", "01", "Number of Connected Components", "🟡 Medium", "#323", "Union-Find"),
    ("advanced_patterns/union_find", "02", "Graph Valid Tree (Cycle Detection)", "🟡 Medium", "#261", "Union-Find"),

    # Advanced Patterns - Topological Sort (2)
    ("advanced_patterns/topological_sort", "01", "Course Schedule", "🟡 Medium", "#207", "Topological Sort"),
    ("advanced_patterns/topological_sort", "02", "Course Schedule II", "🟡 Medium", "#210", "Topological Sort"),

    # Advanced Patterns - Matrix Traversal (2)
    ("advanced_patterns/matrix_traversal", "01", "Number of Islands", "🟡 Medium", "#200", "Matrix Traversal"),
    ("advanced_patterns/matrix_traversal", "02", "Max Area of Island", "🟡 Medium", "#695", "Matrix Traversal"),

    # Advanced Patterns - K-way Merge (1)
    ("advanced_patterns/k_way_merge", "01", "Merge K Sorted Arrays", "🟡 Medium", "-", "K-way Merge"),

    # Advanced Patterns - Modified Binary Search (1)
    ("advanced_patterns/modified_binary_search", "01", "Search a 2D Matrix", "🟡 Medium", "#74", "Modified Binary Search"),

    # Specialized Patterns - Cyclic Sort (3)
    ("specialized_patterns/cyclic_sort", "01", "Cyclic Sort", "🟢 Easy", "-", "Cyclic Sort"),
    ("specialized_patterns/cyclic_sort", "02", "Find Missing Number", "🟢 Easy", "#268", "Cyclic Sort"),
    ("specialized_patterns/cyclic_sort", "03", "Find the Duplicate Number", "🟡 Medium", "#287", "Cyclic Sort"),

    # Specialized Patterns - Linked List Reversal (2)
    ("specialized_patterns/linked_list_reversal", "01", "Reverse Linked List", "🟢 Easy", "#206", "Linked List Reversal"),
    ("specialized_patterns/linked_list_reversal", "02", "Reverse Linked List II", "🟡 Medium", "#92", "Linked List Reversal"),

    # Specialized Patterns - Two Heaps (1)
    ("specialized_patterns/two_heaps", "01", "Find Median from Data Stream", "🔴 Hard", "#295", "Two Heaps"),

    # Specialized Patterns - Subsets (2)
    ("specialized_patterns/subsets", "01", "Subsets", "🟡 Medium", "#78", "Subsets"),
    ("specialized_patterns/subsets", "02", "Permutations", "🟡 Medium", "#46", "Subsets"),

    # Specialized Patterns - Bitwise XOR (2)
    ("specialized_patterns/bitwise_xor", "01", "Single Number", "🟢 Easy", "#136", "Bitwise XOR"),
    ("specialized_patterns/bitwise_xor", "02", "Missing Number", "🟢 Easy", "#268", "Bitwise XOR"),

    # Specialized Patterns - Trie (1)
    ("specialized_patterns/trie", "01", "Implement Trie (Prefix Tree)", "🟡 Medium", "#208", "Trie"),
]

TEMPLATE = """# {title}

## Difficulty: {difficulty}

## Pattern: {pattern}

## LeetCode: [{leetcode}](https://leetcode.com/problems/)

## Description

This problem uses the **{pattern}** pattern. See the solution implementation for complete details.

## Approach

**Pattern**: {pattern}

For detailed approach and explanation, refer to:
- [Pattern Guide](../../../docs/PATTERNS.md)
- [Solution Implementation](../../../src/dsa/{path}.py)

## Complexity Analysis

- **Time Complexity**: See implementation
- **Space Complexity**: See implementation

## Solution Location

[src/dsa/{path}.py](../../../src/dsa/{path}.py)

## Tags

`{pattern}`
"""

def create_problem_file(dir_path, num, title, difficulty, leetcode, pattern):
    """Create a problem markdown file."""
    # Create directory
    problem_dir = PROBLEMS_DIR / dir_path
    problem_dir.mkdir(parents=True, exist_ok=True)

    # Generate filename
    filename = title.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('/', '_').replace('-', '_')
    filename = filename.replace('__', '_')
    filepath = problem_dir / f"{num}_{filename}.md"

    # Generate content
    leetcode_link = leetcode if leetcode == '-' else leetcode
    content = TEMPLATE.format(
        title=title,
        difficulty=difficulty,
        pattern=pattern,
        leetcode=leetcode_link,
        path=dir_path.replace('/', '/')
    )

    # Write file
    with open(filepath, 'w') as f:
        f.write(content)

    return filepath

def main():
    """Create all problem files."""
    print("Creating all remaining problem files...\n")

    created = 0
    for dir_path, num, title, difficulty, leetcode, pattern in PROBLEMS:
        filepath = create_problem_file(dir_path, num, title, difficulty, leetcode, pattern)
        print(f"✓ Created: {filepath.relative_to(BASE_DIR)}")
        created += 1

    print(f"\n✅ Successfully created {created} problem files!")
    print(f"📊 Total problems now: {created} + 18 existing = {created + 18} files")

if __name__ == "__main__":
    main()
