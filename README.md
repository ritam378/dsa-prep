# DSA Interview Preparation - Python

A comprehensive Data Structures and Algorithms repository organized by coding patterns for technical interview preparation.

## Overview

This repository contains 25+ coding patterns with 75-125+ problems commonly asked in technical interviews at FAANG and other top tech companies. Each pattern includes:

- Detailed explanations and when to use the pattern
- Multiple problem implementations with solutions
- Comprehensive test cases
- Time and space complexity analysis
- Problem documentation and examples

## Project Structure

```
dsa/
├── src/dsa/                    # Source code organized by patterns
│   ├── core_patterns/          # Essential patterns (80% of interviews)
│   ├── advanced_patterns/      # Advanced patterns (FAANG level)
│   ├── specialized_patterns/   # Specialized problem-solving patterns
│   └── data_structures/        # Foundation data structures
├── tests/                      # Comprehensive test suite
├── problems/                   # Problem statements and solutions
├── docs/                       # Learning guides and references
└── scripts/                    # Utility scripts
```

## Coding Patterns Covered

### Core Patterns (Essential)
- Two Pointers
- Sliding Window
- Fast & Slow Pointers
- Binary Search
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Backtracking
- Dynamic Programming

### Advanced Patterns
- Merge Intervals
- Matrix Traversal (Island)
- Topological Sort
- Union-Find (DSU)
- Monotonic Stack
- Heap (Top K Elements)
- K-way Merge
- Modified Binary Search

### Specialized Patterns
- Cyclic Sort
- In-place Linked List Reversal
- Two Heaps
- Subsets/Permutations
- Bitwise XOR
- Trie
- Segment Tree
- Graph Algorithms

## Getting Started

### Installation

1. Clone the repository:
```bash
git clone <your-repo-url>
cd dsa
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

### Running Tests

Run all tests:
```bash
pytest
```

Run tests with coverage:
```bash
pytest --cov=src/dsa --cov-report=html
```

Run specific pattern tests:
```bash
pytest tests/test_core_patterns/test_two_pointer.py
```

### Using the Repository

1. **Learn a Pattern**: Start with `docs/PATTERNS.md` to understand each pattern
2. **Study Problems**: Navigate to `problems/<pattern>/` for problem descriptions
3. **Review Solutions**: Check `src/dsa/<pattern>/` for implementations
4. **Practice**: Try solving before looking at solutions
5. **Test**: Run tests to verify your understanding

## Learning Path

### Beginner (Start Here)
1. Two Pointers
2. Sliding Window
3. Binary Search
4. DFS/BFS

### Intermediate
1. Dynamic Programming
2. Backtracking
3. Merge Intervals
4. Monotonic Stack

### Advanced
1. Topological Sort
2. Union-Find
3. Segment Tree
4. Advanced Graph Algorithms

See `docs/LEARNING_GUIDE.md` for detailed learning path.

## Documentation

- **PATTERNS.md**: Detailed explanation of each pattern with examples
- **LEARNING_GUIDE.md**: Recommended learning path and study plan
- **CHEATSHEET.md**: Quick reference for pattern recognition
- **TIME_COMPLEXITY.md**: Big O analysis reference guide
- **RESOURCES.md**: External learning resources and books

## Contributing

Feel free to add more problems, optimize solutions, or improve documentation!

## Time Complexity Quick Reference

| Pattern | Typical Time | Typical Space |
|---------|-------------|---------------|
| Two Pointers | O(n) | O(1) |
| Sliding Window | O(n) | O(k) |
| Binary Search | O(log n) | O(1) |
| DFS/BFS | O(V + E) | O(V) |
| Dynamic Programming | O(n²) or O(n) | O(n) |
| Heap | O(n log k) | O(k) |

## License

MIT License - Feel free to use for learning and interview preparation!

## Acknowledgments

Problems and patterns inspired by common interview questions from LeetCode, HackerRank, and real interview experiences.
