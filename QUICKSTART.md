# Quick Start Guide

Get started with DSA interview preparation in 5 minutes!

## Installation

### 1. Setup Virtual Environment

```bash
# Run the setup script
./scripts/setup.sh
```

Or manually:

```bash
# Create virtual environment
python -m venv venv

# Activate it
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

## Project Structure

```
dsa/
├── src/dsa/                      # Source code
│   ├── core_patterns/            # Essential patterns (80% of interviews)
│   │   ├── two_pointer.py
│   │   ├── sliding_window.py
│   │   ├── binary_search.py
│   │   ├── dfs.py
│   │   ├── bfs.py
│   │   ├── backtracking.py
│   │   └── dynamic_programming.py
│   ├── advanced_patterns/        # Advanced patterns (FAANG)
│   ├── specialized_patterns/     # Specialized patterns
│   └── data_structures/          # Data structure implementations
├── tests/                        # Test suite
├── problems/                     # Problem statements
├── docs/                         # Learning resources
└── scripts/                      # Utility scripts
```

## Running Tests

```bash
# Run all tests
./scripts/run_tests.sh

# Run with coverage
./scripts/run_tests.sh --coverage

# Run specific pattern tests
./scripts/run_tests.sh --pattern two_pointer

# Check coverage threshold
./scripts/check_coverage.sh
```

## Using the Repository

### 1. Learn a Pattern

```bash
# Read the pattern guide
cat docs/PATTERNS.md

# Study a specific pattern (e.g., Two Pointer)
cat src/dsa/core_patterns/two_pointer.py
```

### 2. Solve a Problem

```bash
# Read problem description
cat problems/core_patterns/two_pointer/problem_1_two_sum_sorted.md

# Try solving it yourself first!

# Then check the solution
cat src/dsa/core_patterns/two_pointer.py
```

### 3. Run Tests

```bash
# Test your understanding
pytest tests/test_core_patterns/test_two_pointer.py -v
```

### 4. Practice

```python
# Import and use in Python REPL
python
>>> from dsa.core_patterns.two_pointer import TwoPointerSolutions
>>> TwoPointerSolutions.two_sum_sorted([2, 7, 11, 15], 9)
[0, 1]
```

## Learning Path

### Week 1-2: Core Patterns Basics
- [ ] Two Pointer (5 problems)
- [ ] Sliding Window (5 problems)
- [ ] Binary Search (5 problems)

### Week 3-4: Tree & Graph
- [ ] DFS (5 problems)
- [ ] BFS (5 problems)

### Week 5-6: Recursion & DP
- [ ] Backtracking (5 problems)
- [ ] Dynamic Programming (5 problems)

### Week 7+: Advanced Patterns
- [ ] Merge Intervals
- [ ] Heap
- [ ] Union-Find
- [ ] Topological Sort

## Daily Routine

1. **Morning (1 hour)**
   - Review one pattern
   - Solve 1-2 easy problems

2. **Evening (1-2 hours)**
   - Solve 1-2 medium problems
   - Review and optimize solutions

## Resources

- **Pattern Guide**: [docs/PATTERNS.md](docs/PATTERNS.md)
- **Learning Path**: [docs/LEARNING_GUIDE.md](docs/LEARNING_GUIDE.md)
- **Cheat Sheet**: [docs/CHEATSHEET.md](docs/CHEATSHEET.md)
- **Time Complexity**: [docs/TIME_COMPLEXITY.md](docs/TIME_COMPLEXITY.md)

## Example Workflow

### Solving "Two Sum II"

1. **Read the problem**:
   ```bash
   cat problems/core_patterns/two_pointer/problem_1_two_sum_sorted.md
   ```

2. **Think about approach**:
   - Identify pattern: Two Pointer (sorted array + find pair)
   - Plan solution

3. **Check solution**:
   ```python
   from dsa.core_patterns.two_pointer import TwoPointerSolutions

   # Test it
   result = TwoPointerSolutions.two_sum_sorted([2, 7, 11, 15], 9)
   print(result)  # [0, 1]
   ```

4. **Run tests**:
   ```bash
   pytest tests/test_core_patterns/test_two_pointer.py::TestTwoPointerSolutions::test_two_sum_sorted -v
   ```

5. **Implement yourself**:
   Try coding it from scratch in a separate file

## Tips

1. **Start with Easy**: Begin with core patterns
2. **Understand, Don't Memorize**: Focus on pattern recognition
3. **Code It Yourself**: Don't just read solutions
4. **Time Yourself**: Practice under pressure
5. **Review Regularly**: Revisit problems weekly

## Getting Help

- Check [docs/PATTERNS.md](docs/PATTERNS.md) for pattern explanations
- Review example solutions in `src/dsa/`
- Run tests to verify understanding
- Read problem discussions online (LeetCode, etc.)

## Next Steps

1. Complete setup: `./scripts/setup.sh`
2. Read learning guide: `docs/LEARNING_GUIDE.md`
3. Start with Two Pointer pattern
4. Solve 3-5 problems per pattern
5. Move to next pattern

**You're ready to start! Good luck with your interview preparation!**

## Quick Reference

### Common Commands

```bash
# Setup
./scripts/setup.sh

# Run all tests
./scripts/run_tests.sh

# Coverage report
./scripts/run_tests.sh --coverage

# Activate venv
source venv/bin/activate

# Deactivate venv
deactivate
```

### Import Patterns

```python
# Core patterns
from dsa.core_patterns import two_pointer
from dsa.core_patterns import sliding_window
from dsa.core_patterns import binary_search

# Advanced patterns
from dsa.advanced_patterns import merge_intervals
from dsa.advanced_patterns import heap

# Data structures
from dsa.data_structures import linked_list
from dsa.data_structures import tree
```

---

**Happy Coding! 🚀**
