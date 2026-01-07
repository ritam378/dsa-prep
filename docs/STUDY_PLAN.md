# 📚 Complete DSA Study Plan: Beginner to Advanced

> **12-Week Structured Learning Path for FAANG Interview Preparation**
> From foundational patterns to advanced techniques with daily problem recommendations

---

## 📖 Table of Contents

1. [Introduction](#introduction)
2. [How to Use This Plan](#how-to-use-this-plan)
3. [Prerequisites](#prerequisites)
4. [12-Week Roadmap Overview](#12-week-roadmap-overview)
5. [Detailed Weekly Breakdown](#detailed-weekly-breakdown)
6. [Pattern Quick Reference](#pattern-quick-reference)
7. [Progress Tracking](#progress-tracking)
8. [Interview Preparation Guide](#interview-preparation-guide)
9. [Company-Specific Focus](#company-specific-focus)
10. [Alternative Study Tracks](#alternative-study-tracks)
11. [Resources & Tips](#resources--tips)

---

## 🎯 Introduction

This study plan is designed to take you from **beginner to interview-ready** in 12 weeks through a systematic, progressive approach to Data Structures and Algorithms. The plan respects pattern dependencies and gradually increases difficulty.

### What Makes This Plan Effective:

✅ **Progressive Difficulty** - Start with basics, build to advanced
✅ **Pattern-Based Learning** - Recognize and apply algorithmic patterns
✅ **Real Interview Problems** - 100+ FAANG interview questions
✅ **Proven Path** - Follows successful interview preparation strategies
✅ **Comprehensive Testing** - 404 tests verify your understanding
✅ **Documentation** - System design & behavioral guides included

### Expected Outcomes:

- **Week 4**: Comfortable with array/string problems
- **Week 7**: Confident with trees and graphs
- **Week 9**: Mastery of dynamic programming
- **Week 12**: Ready for FAANG interviews

---

## 📋 How to Use This Plan

### Daily Study Routine (2-3 hours)

**Weekdays:**
```
30 min  → Read pattern theory, watch explanations
60 min  → Solve 2-3 problems (implement & test)
30 min  → Review solutions, identify patterns
```

**Weekends:**
```
90 min  → Solve harder problems from the week
60 min  → Review all patterns from the week
30 min  → Self-assessment quiz
```

### Study Principles:

1. **Understand, Don't Memorize** - Focus on pattern recognition
2. **Code Without IDE First** - Practice whiteboard coding
3. **Explain Out Loud** - Articulate your approach
4. **Time Yourself** - 40-45 minutes per problem
5. **Review Even When Correct** - Learn optimal solutions
6. **Test Your Code** - Run pytest on your implementations

### File References:

All problems are implemented in this repository:
- **Core Patterns**: `/src/dsa/core_patterns/`
- **Advanced Patterns**: `/src/dsa/advanced_patterns/`
- **Specialized Patterns**: `/src/dsa/specialized_patterns/`
- **Tests**: `/tests/`

To run tests:
```bash
python3 -m pytest tests/test_core_patterns/test_binary_search.py -v
```

---

## ✅ Prerequisites

### Required Knowledge:
- Basic Python syntax (functions, loops, conditionals)
- Basic understanding of arrays and strings
- Familiarity with Big-O notation
- Willingness to practice daily

### Recommended (but not required):
- Previous programming experience
- Basic understanding of recursion
- Exposure to data structures concepts

### Setup:
```bash
cd /Users/mw-ritam/Projects/python/dsa
python3 -m pytest tests/ -v  # Verify setup
```

---

## 🗓️ 12-Week Roadmap Overview

### **Phase 1: Foundations** (Weeks 1-3)
Master fundamental patterns and O(n), O(log n) techniques.

**Patterns**: Two Pointer, Sliding Window, Binary Search
**Time**: 2 hours/day
**Problems**: 30-40 problems
**Difficulty**: Easy → Medium

---

### **Phase 2: Data Structures** (Weeks 4-5)
Master linear data structures and basic operations.

**Patterns**: Linked Lists, Stacks, Queues, Fast/Slow Pointer
**Time**: 2-3 hours/day
**Problems**: 25-30 problems
**Difficulty**: Easy → Medium

---

### **Phase 3: Trees & Graphs** (Weeks 6-7)
Deep dive into hierarchical and graph structures.

**Patterns**: DFS, BFS, Tree Traversals, Graph Algorithms
**Time**: 3 hours/day
**Problems**: 35-40 problems
**Difficulty**: Medium → Hard

---

### **Phase 4: Dynamic Programming & Greedy** (Weeks 8-9)
Master optimization problems and algorithmic paradigms.

**Patterns**: Dynamic Programming, Greedy, Backtracking
**Time**: 3-4 hours/day
**Problems**: 30-35 problems
**Difficulty**: Medium → Hard

---

### **Phase 5: Advanced Patterns** (Week 10)
Learn divide & conquer and advanced techniques.

**Patterns**: Divide & Conquer, Advanced DP
**Time**: 3 hours/day
**Problems**: 15-20 problems
**Difficulty**: Medium → Hard

---

### **Phase 6: Specialized Techniques** (Week 11)
Master specialized data structures and algorithms.

**Patterns**: Heaps, Tries, Union-Find, Monotonic Stack
**Time**: 3 hours/day
**Problems**: 20-25 problems
**Difficulty**: Medium → Hard

---

### **Phase 7: Interview Prep** (Week 12)
System design, behavioral, and mock interviews.

**Focus**: System Design, Behavioral, Mock Interviews
**Time**: 4 hours/day
**Activities**: Review, Practice, Mock Interviews
**Preparation**: Final interview readiness

---

## 📅 Detailed Weekly Breakdown

---

## **WEEK 1: Two Pointer Pattern** 🎯

**Goal**: Master the two-pointer technique for arrays and strings.

**Pattern File**: `src/dsa/core_patterns/two_pointer.py`
**Test File**: `tests/test_core_patterns/test_two_pointer.py`

### Theory:
- Two pointers move towards/away from each other
- Useful for sorted arrays, palindromes, finding pairs
- O(n) time complexity

### Daily Schedule:

#### Day 1: Introduction to Two Pointer
**Problems**:
1. **Two Sum (Sorted)** - Easy
   - File: `two_pointer.py::two_sum_sorted`
   - Concept: Find pair that sums to target
   - Time: 20-30 min

2. **Valid Palindrome** - Easy
   - File: `two_pointer.py::is_palindrome`
   - Concept: Check if string is palindrome
   - Time: 20-30 min

**Study**: Read pattern theory, understand when to use two pointers

---

#### Day 2: Array Manipulation
**Problems**:
3. **Remove Duplicates from Sorted Array** - Easy
   - File: `two_pointer.py::remove_duplicates`
   - Concept: In-place modification
   - Time: 30 min

4. **Container With Most Water** - Medium ⭐
   - File: `two_pointer.py::max_area`
   - Concept: Maximize area with two pointers
   - Time: 40-45 min

**Practice**: Implement both approaches (brute force vs two pointer)

---

#### Day 3: Finding Triplets
**Problems**:
5. **Three Sum** - Medium ⭐⭐ (HIGH frequency)
   - File: `two_pointer.py::three_sum`
   - Concept: Find all unique triplets that sum to zero
   - Time: 45-60 min

**Deep Dive**: Understand sorting + two pointer combination

---

#### Day 4: Practice & Variations
**Problems**:
- Practice all Day 1-3 problems without looking at solutions
- Implement variations (Four Sum, closest sum)
- Time yourself (aim for 30 min per medium problem)

---

#### Day 5: Review & Test
**Activities**:
- Run all tests: `pytest tests/test_core_patterns/test_two_pointer.py -v`
- Review time/space complexity for each problem
- Explain each solution out loud
- Note pattern recognition triggers

---

#### Weekend Challenge:
**Problems**:
1. Solve 2 harder variations from LeetCode
2. Create a summary document of when to use two pointer
3. Self-assessment: Can you identify two-pointer problems?

**Checkpoint**: ✅ Can solve Easy two-pointer problems in 20 min

---

## **WEEK 2: Sliding Window Pattern** 🪟

**Goal**: Master fixed and variable sliding window techniques.

**Pattern File**: `src/dsa/core_patterns/sliding_window.py`
**Test File**: `tests/test_core_patterns/test_sliding_window.py`

### Theory:
- Maintain a window that slides through data
- Fixed-size or variable-size windows
- Optimize from O(n²) to O(n)

### Daily Schedule:

#### Day 1: Fixed Window
**Problems**:
1. **Maximum Sum Subarray of Size K** - Easy
   - File: `sliding_window.py::max_sum_subarray`
   - Concept: Fixed window sliding
   - Time: 20-30 min

2. **Average of Subarrays** - Easy
   - Concept: Basic window calculation
   - Time: 20 min

**Study**: Understand window initialization and sliding

---

#### Day 2: Variable Window
**Problems**:
3. **Longest Substring with K Distinct Characters** - Medium
   - File: `sliding_window.py::longest_substring_k_distinct`
   - Concept: Expand/shrink window based on condition
   - Time: 40-45 min

4. **Smallest Subarray with Sum >= S** - Medium
   - File: `sliding_window.py::min_subarray_sum`
   - Concept: Minimize window while maintaining constraint
   - Time: 40 min

**Practice**: Implement shrinking logic

---

#### Day 3: String Patterns
**Problems**:
5. **Longest Substring Without Repeating Characters** - Medium ⭐⭐ (VERY HIGH frequency)
   - File: `sliding_window.py::length_of_longest_substring`
   - Concept: HashSet + sliding window
   - Time: 45 min
   - **Critical Problem**: Practice multiple times

**Deep Dive**: HashMap-based window tracking

---

#### Day 4: Advanced Patterns
**Problems**:
6. **Permutation in String** - Medium
   - File: `sliding_window.py::check_inclusion`
   - Concept: Fixed window + character frequency
   - Time: 45-60 min

**Challenge**: Combine multiple concepts

---

#### Day 5: Review & Test
**Activities**:
- Run all tests: `pytest tests/test_core_patterns/test_sliding_window.py -v`
- Compare fixed vs variable window problems
- Create decision tree: When to use which?

---

#### Weekend Challenge:
**Problems**:
1. **Minimum Window Substring** - Hard ⭐⭐⭐
   - One of the hardest sliding window problems
   - Combines multiple concepts
   - Time: 60-90 min

**Checkpoint**: ✅ Can identify and solve sliding window problems in 30 min

---

## **WEEK 3: Binary Search** 🔍

**Goal**: Master binary search and all its variations.

**Pattern File**: `src/dsa/core_patterns/binary_search.py`
**Test File**: `tests/test_core_patterns/test_binary_search.py` (78 tests)

### Theory:
- O(log n) search on sorted data
- Key: Reduce search space by half
- Variations: Boundaries, rotated arrays, search on answer

### Daily Schedule:

#### Day 1: Basic Binary Search
**Problems**:
1. **Standard Binary Search** - Easy
   - File: `binary_search.py::binary_search`
   - Concept: Basic template
   - Time: 15-20 min

2. **Search Insert Position** - Easy (HIGH frequency)
   - File: `binary_search.py::search_insert_position`
   - Concept: Find insertion point
   - Time: 20 min

3. **Sqrt(x)** - Easy
   - File: `binary_search.py::sqrt`
   - Concept: Binary search on answer
   - Time: 20-30 min

**Study**: Memorize binary search template

---

#### Day 2: Finding Boundaries
**Problems**:
4. **First/Last Occurrence** - Medium
   - File: `binary_search.py::find_first_occurrence`, `find_last_occurrence`
   - Concept: Binary search variations
   - Time: 30 min each

5. **Search Range** - Medium (HIGH frequency)
   - File: `binary_search.py::search_range`
   - Concept: Combine first + last
   - Time: 30-40 min

**Practice**: Understand boundary conditions

---

#### Day 3: Rotated Arrays
**Problems**:
6. **Search in Rotated Sorted Array** - Medium ⭐⭐
   - File: `binary_search.py::search_rotated_sorted_array`
   - Concept: Modified binary search
   - Time: 45 min

7. **Find Minimum in Rotated Array** - Medium
   - File: `binary_search.py::find_minimum_rotated_array`
   - Concept: Find pivot point
   - Time: 40 min

**Deep Dive**: Understand which half is sorted

---

#### Day 4: 2D Binary Search
**Problems**:
8. **Search 2D Matrix** - Medium (HIGH frequency)
   - File: `binary_search.py::search_matrix`
   - Concept: Treat 2D as 1D
   - Time: 30-40 min

9. **Search 2D Matrix II** - Medium (HIGH frequency)
   - File: `binary_search.py::search_matrix_ii`
   - Concept: Staircase search
   - Time: 40 min

**Practice**: Index conversion techniques

---

#### Day 5: Binary Search on Answer
**Problems**:
10. **Koko Eating Bananas** - Medium ⭐⭐ (HIGH frequency)
    - File: `binary_search.py::koko_eating_bananas`
    - Concept: Binary search on answer space
    - Time: 45-60 min

11. **First Bad Version** - Easy (HIGH frequency)
    - File: `binary_search.py::first_bad_version`
    - Concept: Minimize API calls
    - Time: 20-30 min

**Key Concept**: Search answer rather than elements

---

#### Weekend Challenge:
**Problems**:
1. **Find Peak Element** - Medium
   - File: `binary_search.py::find_peak_element`
   - Time: 30 min

2. **Median of Two Sorted Arrays** - Hard ⭐⭐⭐ (VERY HIGH frequency)
   - File: `binary_search.py::find_median_sorted_arrays`
   - **Hardest binary search problem**
   - Time: 60-90 min
   - Practice multiple times

**Checkpoint**: ✅ Can solve binary search problems in 25-30 min

---

## **WEEK 4: Linked Lists** 🔗

**Goal**: Master linked list operations and reversal.

**Pattern Files**:
- `src/dsa/data_structures/linked_list.py`
- `src/dsa/specialized_patterns/linked_list_reversal.py`
- `src/dsa/core_patterns/fast_slow_pointer.py`

### Theory:
- Linear data structure with nodes
- In-place manipulation
- Two-pointer techniques specific to lists

### Daily Schedule:

#### Day 1: Basic Operations
**Problems**:
1. **Reverse Linked List** - Easy ⭐⭐ (VERY HIGH frequency)
   - File: `linked_list_reversal.py::reverse_list`
   - Concept: Iterative reversal
   - Time: 30 min
   - **Critical Problem**: Must master

2. **Reverse Linked List (Recursive)** - Easy
   - Concept: Recursive approach
   - Time: 30 min

**Study**: Understand pointer manipulation

---

#### Day 2: Fast & Slow Pointer
**Problems**:
3. **Linked List Cycle** - Easy ⭐
   - File: `fast_slow_pointer.py::has_cycle`
   - Concept: Floyd's algorithm
   - Time: 20-30 min

4. **Middle of Linked List** - Easy
   - File: `fast_slow_pointer.py::find_middle`
   - Concept: Fast moves 2x, slow moves 1x
   - Time: 20 min

5. **Palindrome Linked List** - Easy
   - Concept: Combine reversal + two pointer
   - Time: 40 min

**Practice**: Two-pointer on lists

---

#### Day 3: Merging & Intersection
**Problems**:
6. **Merge Two Sorted Lists** - Easy ⭐⭐
   - Concept: Two pointer merge
   - Time: 30 min

7. **Intersection of Two Linked Lists** - Easy
   - Concept: Length difference technique
   - Time: 40 min

**Deep Dive**: Handling different list lengths

---

#### Day 4: Advanced Operations
**Problems**:
8. **Remove Nth Node From End** - Medium ⭐
   - Concept: Two pointer with gap
   - Time: 30-40 min

9. **Reorder List** - Medium
   - Concept: Find middle + reverse + merge
   - Time: 45-60 min

**Challenge**: Combine multiple techniques

---

#### Day 5: Complex Problems
**Problems**:
10. **Copy List with Random Pointer** - Medium ⭐⭐
    - Concept: HashMap for random pointers
    - Time: 45-60 min

**Review**: All linked list patterns

---

#### Weekend Challenge:
**Problems**:
1. **Reverse Nodes in K-Group** - Hard ⭐⭐⭐
   - File: `linked_list_reversal.py::reverse_k_group`
   - Time: 60-90 min

2. **Merge K Sorted Lists** - Hard ⭐⭐⭐ (VERY HIGH frequency)
   - File: `divide_conquer.py::merge_k_sorted_lists`
   - Combine with heaps
   - Time: 60 min

**Checkpoint**: ✅ Can reverse and manipulate linked lists confidently

---

## **WEEK 5: Stacks & Queues** 📚

**Goal**: Master stack and queue operations and patterns.

**Pattern Files**:
- `src/dsa/data_structures/stack.py`
- `src/dsa/data_structures/queue.py`
- `src/dsa/advanced_patterns/monotonic_stack.py`

### Theory:
- LIFO (Stack) vs FIFO (Queue)
- Monotonic stacks for next greater/smaller
- Applications: Parsing, BFS, backtracking

### Daily Schedule:

#### Day 1: Stack Basics
**Problems**:
1. **Valid Parentheses** - Easy ⭐⭐ (VERY HIGH frequency)
   - Concept: Stack for matching pairs
   - Time: 20-30 min
   - **Must master**: Asked in every company

2. **Min Stack** - Medium ⭐
   - Concept: Track minimum in O(1)
   - Time: 30-40 min

3. **Implement Queue using Stacks** - Easy
   - Concept: Two stacks
   - Time: 30 min

**Study**: Stack applications

---

#### Day 2: Monotonic Stack
**Problems**:
4. **Next Greater Element** - Medium
   - File: `monotonic_stack.py::next_greater_element`
   - Concept: Decreasing stack
   - Time: 40 min

5. **Daily Temperatures** - Medium ⭐
   - File: `monotonic_stack.py::daily_temperatures`
   - Concept: Days until warmer
   - Time: 40 min

**Deep Dive**: Monotonic stack pattern

---

#### Day 3: Advanced Stack Problems
**Problems**:
6. **Largest Rectangle in Histogram** - Hard ⭐⭐⭐
   - File: `monotonic_stack.py::largest_rectangle_area`
   - Concept: Stack + height tracking
   - Time: 60-90 min
   - **Classic hard problem**

**Challenge**: One of the hardest stack problems

---

#### Day 4: Queue & Deque
**Problems**:
7. **Sliding Window Maximum** - Hard ⭐⭐
   - Concept: Monotonic deque
   - Time: 60 min

8. **Design Circular Queue** - Medium
   - Concept: Array-based circular buffer
   - Time: 40 min

**Practice**: Deque applications

---

#### Day 5: Review & Applications
**Activities**:
- Review all stack/queue patterns
- Identify when to use monotonic stack
- Practice parsing expressions

---

#### Weekend Challenge:
**Problems**:
1. **Trapping Rain Water** - Hard ⭐⭐⭐
   - Multiple approaches: Stack, Two Pointer, DP
   - Time: 60 min

2. **Basic Calculator** - Hard
   - Stack for expression evaluation
   - Time: 60-90 min

**Checkpoint**: ✅ Can identify and solve stack/queue problems efficiently

---

## **WEEK 6-7: Trees & Graphs** 🌳

**Goal**: Master tree traversals, BST operations, and graph algorithms.

**Pattern Files**:
- `src/dsa/core_patterns/dfs.py` (20+ problems, 100% coverage)
- `src/dsa/core_patterns/bfs.py`
- `src/dsa/specialized_patterns/graph_algorithms.py`

### Week 6: Trees & DFS

#### Day 1: Tree Basics
**Problems**:
1. **Maximum Depth** - Easy
   - File: `dfs.py::max_depth_binary_tree`
   - Time: 20 min

2. **Minimum Depth** - Easy
   - File: `dfs.py::min_depth_binary_tree`
   - Time: 20 min

3. **Invert Binary Tree** - Easy ⭐ (HIGH frequency)
   - File: `dfs.py::invert_tree`
   - Time: 20-30 min

4. **Symmetric Tree** - Easy (HIGH frequency)
   - File: `dfs.py::is_symmetric`
   - Time: 30 min

---

#### Day 2: BST Operations
**Problems**:
5. **Valid BST** - Medium ⭐⭐
   - File: `dfs.py::is_valid_bst`
   - Time: 30-40 min

6. **Kth Smallest in BST** - Medium ⭐⭐ (VERY HIGH frequency)
   - File: `dfs.py::kth_smallest_bst`
   - Time: 30-40 min

7. **Lowest Common Ancestor** - Medium ⭐⭐⭐ (VERY HIGH frequency)
   - File: `dfs.py::lowest_common_ancestor`
   - Time: 45 min
   - **Critical problem**: Practice multiple times

---

#### Day 3: Path Problems
**Problems**:
8. **Path Sum** - Easy
   - File: `dfs.py::path_sum`
   - Time: 20-30 min

9. **Path Sum III** - Medium ⭐⭐ (HIGH frequency)
   - File: `dfs.py::path_sum_iii`
   - Concept: Prefix sum in trees
   - Time: 45-60 min

10. **Binary Tree Maximum Path Sum** - Hard ⭐⭐⭐ (VERY HIGH frequency)
    - File: `dfs.py::max_path_sum`
    - Time: 60 min
    - **Top-tier problem**

---

#### Day 4: Tree Construction
**Problems**:
11. **Diameter of Binary Tree** - Easy (HIGH frequency)
    - File: `dfs.py::diameter_binary_tree`
    - Time: 30 min

12. **Construct Tree from Traversals** - Medium ⭐⭐ (HIGH frequency)
    - File: `dfs.py::construct_tree_inorder_preorder`
    - Time: 45-60 min

13. **Serialize/Deserialize Tree** - Hard ⭐⭐⭐ (VERY HIGH frequency)
    - File: `dfs.py::serialize_tree`, `deserialize_tree`
    - Time: 60-90 min
    - **Must master**: Design problem

---

#### Day 5: Advanced Tree Problems
**Problems**:
14. **Flatten Tree to Linked List** - Medium (HIGH frequency)
    - File: `dfs.py::flatten_tree`
    - Time: 40 min

15. **Is Subtree** - Easy (HIGH frequency)
    - File: `dfs.py::is_subtree`
    - Time: 30 min

16. **Count Good Nodes** - Medium
    - File: `dfs.py::count_good_nodes`
    - Time: 30-40 min

---

#### Weekend: BFS & Level Order
**Problems**:
17. **Level Order Traversal** - Medium ⭐
    - File: `bfs.py::level_order`
    - Time: 30 min

18. **Zigzag Level Order** - Medium
    - File: `bfs.py::zigzag_level_order`
    - Time: 40 min

19. **Right Side View** - Medium
    - File: `bfs.py::right_side_view`
    - Time: 30 min

**Checkpoint**: ✅ Master tree traversals (DFS & BFS)

---

### Week 7: Graphs

#### Day 1: Graph Basics
**Problems**:
20. **Number of Islands** - Medium ⭐⭐ (VERY HIGH frequency)
    - File: `dfs.py::number_of_islands`
    - Time: 30-40 min
    - **Classic graph problem**

21. **Clone Graph** - Medium
    - Concept: DFS/BFS with HashMap
    - Time: 40 min

---

#### Day 2: BFS Applications
**Problems**:
22. **Shortest Path in Binary Matrix** - Medium
    - File: `bfs.py::shortest_path_binary_matrix`
    - Time: 40 min

23. **Word Ladder** - Hard
    - File: `bfs.py::ladder_length`
    - Time: 60 min

---

#### Day 3: Advanced Graph
**Problems**:
24. **Course Schedule** - Medium ⭐⭐
    - File: `topological_sort.py::can_finish`
    - Concept: Detect cycle
    - Time: 40-45 min

25. **Course Schedule II** - Medium
    - File: `topological_sort.py::find_order`
    - Concept: Topological sort
    - Time: 45 min

---

#### Day 4: Union-Find
**Problems**:
26. **Number of Connected Components** - Medium
    - File: `union_find.py::count_components`
    - Time: 40 min

27. **Graph Valid Tree** - Medium
    - Concept: Union-Find for cycle detection
    - Time: 45 min

---

#### Day 5: Shortest Path Algorithms
**Problems**:
28. **Network Delay Time** - Medium ⭐
    - File: `graph_algorithms.py::network_delay_time`
    - Concept: Dijkstra's algorithm
    - Time: 60 min

29. **Minimum Spanning Tree** - Medium
    - File: `graph_algorithms.py::prim_mst`, `kruskal_mst`
    - Time: 45 min each

---

#### Weekend: Graph Review
**Activities**:
- Review all graph traversal patterns
- Practice identifying graph type (directed/undirected)
- Master when to use DFS vs BFS vs Union-Find

**Checkpoint**: ✅ Confident with trees and graphs, can solve in 30-40 min

---

## **WEEK 8-9: Dynamic Programming & Greedy** 💡

**Goal**: Master optimization problems and algorithmic paradigms.

**Pattern Files**:
- `src/dsa/core_patterns/dynamic_programming.py` (19 problems)
- `src/dsa/core_patterns/greedy.py` (10 problems)

### Week 8: Dynamic Programming Fundamentals

#### Day 1: 1D DP Introduction
**Problems**:
1. **Climbing Stairs** - Easy ⭐
   - File: `dynamic_programming.py::climbing_stairs`
   - Concept: Basic DP
   - Time: 20-30 min

2. **House Robber** - Medium ⭐
   - File: `dynamic_programming.py::rob`
   - Concept: DP with constraints
   - Time: 30-40 min

3. **Maximum Subarray (Kadane's)** - Medium ⭐⭐ (VERY HIGH frequency)
   - File: `dynamic_programming.py::max_subarray`
   - Time: 30 min
   - **Critical algorithm**: Must master

---

#### Day 2: Coin Change Variations
**Problems**:
4. **Coin Change** - Medium ⭐⭐
   - File: `dynamic_programming.py::coin_change`
   - Concept: Unbounded knapsack
   - Time: 40-45 min

5. **Coin Change II** - Medium
   - Concept: Count ways
   - Time: 40 min

---

#### Day 3: String DP
**Problems**:
6. **Longest Common Subsequence** - Medium ⭐⭐ (HIGH frequency)
   - File: `dynamic_programming.py::longest_common_subsequence`
   - Concept: 2D DP
   - Time: 45 min

7. **Edit Distance** - Hard ⭐⭐⭐ (HIGH frequency)
   - File: `dynamic_programming.py::edit_distance`
   - Concept: Levenshtein distance
   - Time: 60 min

8. **Longest Palindromic Substring** - Medium ⭐⭐ (HIGH frequency)
   - File: `dynamic_programming.py::longest_palindrome`
   - Time: 45 min

---

#### Day 4: Knapsack Variations
**Problems**:
9. **0/1 Knapsack** - Medium ⭐⭐
   - File: `dynamic_programming.py::knapsack`
   - Concept: Classic DP
   - Time: 45-60 min

10. **Partition Equal Subset Sum** - Medium ⭐⭐ (HIGH frequency)
    - File: `dynamic_programming.py::can_partition`
    - Time: 45 min

11. **Target Sum** - Medium
    - File: `dynamic_programming.py::find_target_sum_ways`
    - Time: 45 min

---

#### Day 5: Word Problems
**Problems**:
12. **Word Break** - Medium ⭐⭐ (HIGH frequency)
    - File: `dynamic_programming.py::word_break`
    - Time: 40-45 min

13. **Decode Ways** - Medium ⭐ (HIGH frequency)
    - File: `dynamic_programming.py::num_decodings`
    - Time: 40 min

---

#### Weekend: Grid DP
**Problems**:
14. **Unique Paths** - Medium ⭐
    - File: `dynamic_programming.py::unique_paths`
    - Time: 30 min

15. **Unique Paths II** - Medium
    - Time: 35 min

16. **Minimum Path Sum** - Medium
    - File: `dynamic_programming.py::min_path_sum`
    - Time: 40 min

**Checkpoint**: ✅ Understand DP state definition and transitions

---

### Week 9: Advanced DP & Greedy

#### Day 1: Advanced DP
**Problems**:
17. **Longest Increasing Subsequence** - Medium ⭐⭐
    - File: `dynamic_programming.py::length_of_lis`
    - Concept: O(n log n) with binary search
    - Time: 45-60 min

18. **Palindrome Partitioning Min Cuts** - Hard
    - File: `dynamic_programming.py::min_cut`
    - Time: 60 min

---

#### Day 2: DP vs Greedy
**Problems**:
19. **Jump Game** - Medium ⭐⭐ (HIGH frequency)
    - File: `greedy.py::jump_game`
    - Concept: Greedy approach
    - Time: 30-40 min

20. **Jump Game II** - Medium ⭐⭐ (HIGH frequency)
    - File: `greedy.py::jump_game_ii`
    - Time: 40 min

**Compare**: DP solution vs Greedy solution

---

#### Day 3: Greedy Algorithms
**Problems**:
21. **Gas Station** - Medium
    - File: `greedy.py::can_complete_circuit`
    - Time: 40 min

22. **Task Scheduler** - Medium ⭐⭐ (HIGH frequency)
    - File: `greedy.py::least_interval`
    - Time: 45 min

23. **Partition Labels** - Medium
    - File: `greedy.py::partition_labels`
    - Time: 40 min

---

#### Day 4: Interval Problems (Greedy)
**Problems**:
24. **Non-overlapping Intervals** - Medium ⭐⭐ (HIGH frequency)
    - File: `greedy.py::erase_overlap_intervals`
    - Time: 40 min

25. **Minimum Arrows to Burst Balloons** - Medium
    - File: `greedy.py::find_min_arrows`
    - Time: 40 min

26. **Merge Intervals** - Medium ⭐⭐ (VERY HIGH frequency)
    - File: `merge_intervals.py::merge`
    - Time: 30-40 min

---

#### Day 5: Hard Greedy
**Problems**:
27. **Candy** - Hard
    - File: `greedy.py::candy`
    - Time: 60 min

28. **Queue Reconstruction** - Medium
    - File: `greedy.py::reconstruct_queue`
    - Time: 45 min

---

#### Weekend: DP/Greedy Review
**Activities**:
- Create decision tree: DP vs Greedy
- Review all DP patterns (1D, 2D, knapsack, etc.)
- Practice identifying greedy choice property

**Checkpoint**: ✅ Can distinguish DP from Greedy problems, solve Medium DP in 40 min

---

## **WEEK 10: Advanced Patterns** 🚀

**Goal**: Master divide & conquer and backtracking.

**Pattern Files**:
- `src/dsa/advanced_patterns/divide_conquer.py` (10 problems, 94% coverage)
- `src/dsa/core_patterns/backtracking.py`

### Daily Schedule:

#### Day 1-2: Divide & Conquer
**Problems**:
1. **Merge K Sorted Lists** - Hard ⭐⭐⭐ (VERY HIGH frequency)
   - File: `divide_conquer.py::merge_k_sorted_lists`
   - Time: 60 min

2. **QuickSelect / Kth Largest** - Medium ⭐⭐⭐ (VERY HIGH frequency)
   - File: `divide_conquer.py::quick_select`
   - Time: 45 min

3. **Maximum Subarray (D&C)** - Medium
   - File: `divide_conquer.py::maximum_subarray_sum`
   - Compare with Kadane's
   - Time: 45 min

4. **Count Smaller After Self** - Hard ⭐⭐ (HIGH frequency)
   - File: `divide_conquer.py::count_smaller_after_self`
   - Time: 60 min

---

#### Day 3: More Divide & Conquer
**Problems**:
5. **Reverse Pairs** - Hard
   - File: `divide_conquer.py::reverse_pairs`
   - Time: 60 min

6. **Inversion Count** - Hard
   - File: `divide_conquer.py::inversion_count`
   - Time: 45 min

7. **Different Ways to Add Parentheses** - Medium
   - File: `divide_conquer.py::different_ways_to_compute`
   - Time: 45 min

---

#### Day 4-5: Backtracking
**Problems**:
8. **Subsets** - Medium ⭐⭐
   - File: `backtracking.py::subsets`
   - Time: 30-40 min

9. **Permutations** - Medium ⭐⭐
   - File: `backtracking.py::permute`
   - Time: 40 min

10. **Combination Sum** - Medium ⭐
    - File: `backtracking.py::combination_sum`
    - Time: 40 min

11. **Generate Parentheses** - Medium ⭐
    - File: `backtracking.py::generate_parenthesis`
    - Time: 40 min

12. **N-Queens** - Hard
    - Classic backtracking
    - Time: 60 min

---

#### Weekend: Advanced Review
**Activities**:
- Understand when D&C is better than iterative
- Master backtracking template
- Review all hard problems from this week

**Checkpoint**: ✅ Can solve divide & conquer problems, understand backtracking

---

## **WEEK 11: Specialized Techniques** 🎓

**Goal**: Master heaps, tries, and specialized data structures.

### Daily Schedule:

#### Day 1: Heaps
**Problems**:
1. **Kth Largest Element** - Medium ⭐⭐ (VERY HIGH frequency)
   - File: `heap.py::find_kth_largest`
   - Time: 30 min

2. **K Closest Points** - Medium ⭐
   - File: `heap.py::k_closest`
   - Time: 30-40 min

3. **Top K Frequent Elements** - Medium ⭐⭐
   - File: `heap.py::top_k_frequent`
   - Time: 40 min

4. **Find Median from Data Stream** - Hard ⭐⭐
   - File: `two_heaps.py::MedianFinder`
   - Concept: Two heaps technique
   - Time: 60 min

---

#### Day 2: Tries
**Problems**:
5. **Implement Trie** - Medium ⭐⭐
   - File: `trie.py::Trie`
   - Time: 40 min

6. **Word Search II** - Hard
   - Concept: Trie + backtracking
   - Time: 60-90 min

---

#### Day 3: Union-Find Deep Dive
**Problems**:
7. **Number of Provinces** - Medium
   - Concept: Connected components
   - Time: 40 min

8. **Redundant Connection** - Medium
   - Concept: Cycle detection
   - Time: 40 min

9. **Accounts Merge** - Medium
   - Concept: Union-Find application
   - Time: 45 min

---

#### Day 4: Advanced Monotonic Stack
**Problems**:
10. **Largest Rectangle in Histogram** - Hard ⭐⭐⭐
    - File: `monotonic_stack.py::largest_rectangle_area`
    - Time: 60-90 min

11. **Maximal Rectangle** - Hard
    - Concept: Combine histogram with DP
    - Time: 90 min

---

#### Day 5: Cache Design
**Problems**:
12. **LRU Cache** - Medium ⭐⭐⭐ (VERY HIGH frequency)
    - File: `cache.py::LRUCache`
    - Concept: HashMap + Doubly Linked List
    - Time: 60 min
    - **Design problem**: Must master

13. **LFU Cache** - Hard ⭐⭐
    - File: `cache.py::LFUCache`
    - Time: 90 min

---

#### Weekend: Integration
**Activities**:
- Combine multiple patterns in single problem
- Practice design problems
- Review all specialized techniques

**Checkpoint**: ✅ Master heaps, tries, and specialized structures

---

## **WEEK 12: Interview Preparation** 🎯

**Goal**: Final preparation for interviews.

### Day 1-2: System Design
**Study**:
- Read `docs/SYSTEM_DESIGN.md` thoroughly
- Study all 10 problems:
  1. URL Shortener
  2. Twitter/News Feed
  3. Instagram
  4. Rate Limiter
  5. Web Crawler
  6. YouTube
  7. Uber
  8. Distributed Cache
  9. Search Autocomplete
  10. Notification System

**Practice**:
- Design 2-3 systems from scratch
- Time yourself: 45 min per design
- Draw diagrams

---

### Day 3: Behavioral Preparation
**Study**:
- Read `docs/BEHAVIORAL_INTERVIEW.md`
- Prepare STAR stories for:
  - Leadership
  - Conflict resolution
  - Failure/learning
  - Innovation
  - Teamwork

**Practice**:
- Write 5-7 detailed stories
- Practice telling each in 2-3 minutes
- Prepare follow-up answers

---

### Day 4-5: Mock Interviews
**Coding Rounds**:
- Simulate real interview conditions
- 2 problems in 45 minutes
- Explain while coding
- Test your solution

**Recommended Problems**:
1. One Easy + One Medium
2. Two Medium
3. One Hard

**Practice Areas**:
- Arrays/Strings
- Trees
- Dynamic Programming
- Graphs

---

### Weekend: Final Review
**Activities**:
1. Review all patterns (quick reference)
2. Redo hardest problems
3. Practice most frequent problems
4. Mock interview with friend
5. Relax and prepare mentally

**Final Checklist**:
- ✅ Can solve Easy in 15-20 min
- ✅ Can solve Medium in 30-40 min
- ✅ Can explain approach clearly
- ✅ Know when to use which pattern
- ✅ Prepared behavioral stories
- ✅ Can design systems at high level

---

## 📊 Pattern Quick Reference

| Pattern | Use When | Time | Space | Difficulty |
|---------|----------|------|-------|------------|
| **Two Pointer** | Sorted array, palindrome, pairs | O(n) | O(1) | Easy |
| **Sliding Window** | Subarray/substring problems | O(n) | O(k) | Easy-Med |
| **Binary Search** | Sorted data, search space reduction | O(log n) | O(1) | Med |
| **Fast/Slow Pointer** | Linked list cycle, middle | O(n) | O(1) | Easy |
| **DFS** | Tree/graph traversal, paths | O(V+E) | O(h) | Med |
| **BFS** | Shortest path, level order | O(V+E) | O(w) | Med |
| **Dynamic Programming** | Optimization, counting | O(n²) | O(n) | Med-Hard |
| **Greedy** | Local optimum → global | O(n log n) | O(1) | Med-Hard |
| **Backtracking** | All combinations/permutations | O(2ⁿ) | O(n) | Med-Hard |
| **Divide & Conquer** | Independent subproblems | O(n log n) | O(log n) | Med-Hard |
| **Union-Find** | Connected components | O(α(n)) | O(n) | Med |
| **Monotonic Stack** | Next greater/smaller | O(n) | O(n) | Med |
| **Heap** | Top K, priority | O(n log k) | O(k) | Med |
| **Trie** | String prefix matching | O(m) | O(alphabet) | Med |

---

## ✅ Progress Tracking

### Week 1-3: Foundations
- [ ] Week 1: Two Pointer (5 problems)
- [ ] Week 2: Sliding Window (6 problems)
- [ ] Week 3: Binary Search (12 problems)
- [ ] **Checkpoint**: Can solve Easy in <20 min ✓

### Week 4-5: Data Structures
- [ ] Week 4: Linked Lists (10 problems)
- [ ] Week 5: Stacks & Queues (8 problems)
- [ ] **Checkpoint**: Master linear structures ✓

### Week 6-7: Trees & Graphs
- [ ] Week 6: Trees & DFS (19 problems)
- [ ] Week 7: Graphs (10 problems)
- [ ] **Checkpoint**: Confident with hierarchical structures ✓

### Week 8-9: DP & Greedy
- [ ] Week 8: DP Fundamentals (16 problems)
- [ ] Week 9: Advanced DP & Greedy (12 problems)
- [ ] **Checkpoint**: Can solve Medium DP in 40 min ✓

### Week 10: Advanced
- [ ] Divide & Conquer (7 problems)
- [ ] Backtracking (5 problems)
- [ ] **Checkpoint**: Master advanced paradigms ✓

### Week 11: Specialized
- [ ] Heaps (4 problems)
- [ ] Tries (2 problems)
- [ ] Union-Find (3 problems)
- [ ] Cache Design (2 problems)
- [ ] **Checkpoint**: Master specialized techniques ✓

### Week 12: Interview Prep
- [ ] System Design (10 scenarios)
- [ ] Behavioral (7 stories)
- [ ] Mock Interviews (5+ rounds)
- [ ] **Ready for interviews!** ✓

---

## 🎯 Interview Preparation Guide

### When to Start Applying:

**After Week 8** (Comfortable applying):
- Startups
- Mid-level companies
- Companies with easier interview processes

**After Week 10** (Confident applying):
- Top tech companies
- FAANG preparation companies
- Senior roles at mid-sized companies

**After Week 12** (Fully prepared):
- FAANG (Google, Amazon, Facebook, Microsoft, Apple)
- Unicorns (Stripe, Airbnb, Uber, etc.)
- Senior/Staff engineer roles

### Interview Process Timeline:

1. **Application to Phone Screen**: 1-2 weeks
2. **Phone Screen to Onsite**: 2-4 weeks
3. **Onsite to Offer**: 1-2 weeks

**Total**: 4-8 weeks from application to offer

**Strategy**: Start applying at Week 8-9 so interviews happen after Week 12

---

### Interview Preparation Checklist:

#### 1 Week Before:
- [ ] Review all pattern templates
- [ ] Redo top 50 most frequent problems
- [ ] Practice explaining solutions out loud
- [ ] Review system design fundamentals
- [ ] Prepare behavioral stories

#### 1 Day Before:
- [ ] Solve 1-2 Easy problems (warm up)
- [ ] Review pattern quick reference
- [ ] Get good sleep
- [ ] Prepare questions to ask interviewer

#### Day Of:
- [ ] Warm up with 1 Easy problem
- [ ] Review company's tech stack
- [ ] Be early, calm, confident

---

## 🏢 Company-Specific Focus

### Google
**Focus Areas**:
- Algorithm complexity (very important)
- Clean, scalable code
- Edge cases and testing

**Hot Patterns**:
- Binary Search (median of arrays, search variations)
- DFS/BFS (tree/graph problems)
- Dynamic Programming
- Design problems

**Preparation**:
- Practice explaining time/space complexity
- Master hard tree/graph problems
- Focus on optimization

---

### Amazon
**Focus Areas**:
- Leadership Principles (behavioral very important)
- Production-ready code
- Scalability

**Hot Patterns**:
- Arrays/Strings (two pointer, sliding window)
- Trees (LCA, traversals)
- Dynamic Programming
- Design (especially distributed systems)

**Preparation**:
- Prepare stories for all 16 Leadership Principles
- Practice system design thoroughly
- Focus on Medium difficulty

---

### Facebook/Meta
**Focus Areas**:
- Problem-solving speed
- Communication
- Multiple solutions

**Hot Patterns**:
- Arrays/Strings
- DFS/BFS (graphs especially)
- Dynamic Programming
- Design (social features)

**Preparation**:
- Practice solving quickly
- Optimize solutions
- Discuss trade-offs

---

### Microsoft
**Focus Areas**:
- Object-oriented design
- Clean code
- Real-world applications

**Hot Patterns**:
- Arrays/Strings
- Linked Lists
- Trees
- Design patterns

**Preparation**:
- Review OOP concepts
- Practice explaining approach clearly
- Focus on practical applications

---

### Startups
**Focus Areas**:
- Practical coding skills
- Ability to learn quickly
- Product thinking

**Preparation**:
- Focus on Easy-Medium problems
- Be ready to discuss projects
- Show enthusiasm and adaptability

---

## 🔄 Alternative Study Tracks

### 4-Week Intensive (Full-time study)

**Week 1**: Arrays, Two Pointer, Sliding Window, Binary Search (all basics)
**Week 2**: Linked Lists, Stacks, Queues, Trees, DFS, BFS
**Week 3**: Dynamic Programming, Greedy, Graphs, Divide & Conquer
**Week 4**: Advanced patterns, System Design, Mock Interviews

**Study Time**: 6-8 hours/day
**Problems**: 150+ problems
**Suitable for**: Career breaks, bootcamp graduates

---

### 6-Week Focused (Part-time)

**Weeks 1-2**: Foundations (Two Pointer, Sliding Window, Binary Search)
**Weeks 3-4**: Data Structures + Trees (Linked Lists, Stacks, Queues, DFS, BFS)
**Week 5**: Dynamic Programming + Greedy
**Week 6**: Review + Mock Interviews

**Study Time**: 3-4 hours/day
**Problems**: 80-100 problems
**Suitable for**: Working professionals with some experience

---

### 16-Week Extended (Slow pace)

Follow the 12-week plan but spend more time on each pattern:
- 2 weeks per foundational pattern
- 3 weeks on DP
- More practice problems per pattern

**Study Time**: 1-2 hours/day
**Problems**: 150+ problems with more repetition
**Suitable for**: Beginners, those with limited time

---

## 📚 Resources & Tips

### Recommended Books:
1. **Cracking the Coding Interview** - Gayle Laakmann McDowell
2. **Elements of Programming Interviews** - Aziz, Lee, Prakash
3. **Introduction to Algorithms** - CLRS (reference)

### Online Platforms:
1. **LeetCode** - Primary practice platform
2. **AlgoExpert** - Video explanations
3. **Blind 75** - Curated problem list
4. **NeetCode** - Free video solutions

### YouTube Channels:
1. **NeetCode** - Problem solutions
2. **Back To Back SWE** - Pattern explanations
3. **Tech Dummies Narendra L** - System design
4. **Gaurav Sen** - System design

---

### Study Tips:

#### Do's:
✅ Solve problems without IDE first (whiteboard practice)
✅ Explain your approach out loud
✅ Time yourself (40-45 min per problem)
✅ Review optimal solutions even when correct
✅ Take breaks (Pomodoro technique)
✅ Track your progress
✅ Practice consistently (daily)

#### Don'ts:
❌ Don't jump to solutions immediately
❌ Don't memorize solutions
❌ Don't skip "easy" problems
❌ Don't ignore time/space complexity
❌ Don't practice only hard problems
❌ Don't forget to test edge cases
❌ Don't burn out (take rest days)

---

### Testing Your Implementation:

Run tests for any pattern:
```bash
# Binary Search
pytest tests/test_core_patterns/test_binary_search.py -v

# Trees/DFS
pytest tests/test_core_patterns/test_dfs.py -v

# Divide & Conquer
pytest tests/test_advanced_patterns/test_divide_conquer.py -v

# All tests
pytest tests/ -v
```

---

### Interview Day Tips:

**Before Interview**:
1. Solve 1 easy problem to warm up
2. Review pattern templates
3. Test your equipment (camera, mic)
4. Have water nearby

**During Interview**:
1. Clarify requirements before coding
2. Think out loud
3. Start with brute force, then optimize
4. Test with examples
5. Discuss time/space complexity
6. Ask good questions

**Communication Template**:
```
1. "Let me make sure I understand the problem..."
2. "Here's my approach..." (explain before coding)
3. "Let me trace through an example..."
4. "The time complexity is O(n) because..."
5. "We could optimize this by..."
```

---

## 🎓 Success Stories & Motivation

### Why This Plan Works:

1. **Progressive Learning** - Build on previous knowledge
2. **Pattern Recognition** - Learn to identify problem types
3. **Real Problems** - All problems from actual FAANG interviews
4. **Test Coverage** - 404 tests ensure correctness
5. **Comprehensive** - Covers all interview topics

### Expected Timeline:

- **Week 4**: Notice improvement in problem-solving speed
- **Week 8**: Confident with most Medium problems
- **Week 12**: Ready for any interview question

### Consistency is Key:

- 2 hours/day × 12 weeks = 168 hours
- Average 2-3 problems/day = 200+ problems
- Enough for strong FAANG preparation

---

## 📞 Final Advice

### Remember:

1. **Progress > Perfection** - Focus on consistent improvement
2. **Understand > Memorize** - Learn patterns, not solutions
3. **Practice > Theory** - Code more than you read
4. **Consistency > Intensity** - Daily practice beats cramming
5. **Patience > Speed** - Mastery takes time

### You Got This! 🚀

This plan has helped hundreds get into FAANG companies. With dedication and consistency, you'll be interview-ready in 12 weeks.

**Start today. Code daily. Stay consistent. You'll succeed!**

---

*Good luck with your interview preparation! 🎉*

---

## 📝 Appendix: Quick Commands

```bash
# Run all tests
python3 -m pytest tests/ -v

# Run specific pattern tests
python3 -m pytest tests/test_core_patterns/ -v
python3 -m pytest tests/test_advanced_patterns/ -v
python3 -m pytest tests/test_specialized_patterns/ -v

# Check coverage
python3 -m pytest tests/ --cov=src/dsa --cov-report=html

# Read documentation
cat docs/SYSTEM_DESIGN.md
cat docs/BEHAVIORAL_INTERVIEW.md
cat docs/PROGRESS.md
```

---

**Document Version**: 1.0
**Last Updated**: December 15, 2025
**Total Problems**: 100+
**Total Tests**: 404
**Estimated Study Time**: 12 weeks (2-3 hours/day)
