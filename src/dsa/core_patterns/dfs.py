"""
Depth-First Search (DFS) Pattern

Pattern: Explore as far as possible along each branch before backtracking.
When to use:
- Tree/graph traversal
- Path finding
- Detecting cycles
- Topological sorting

Time Complexity: O(V + E) for graphs, O(n) for trees
Space Complexity: O(h) where h is height (recursion stack)
"""

from typing import List, Optional, Set
import sys
sys.path.append('..')
from data_structures.tree import TreeNode
from data_structures.graph import Graph


class DFSSolutions:
    """Solutions using the depth-first search pattern."""

    @staticmethod
    def max_depth_binary_tree(root: Optional[TreeNode]) -> int:
        """
        Find maximum depth of binary tree.

        Time Complexity: O(n)
        Space Complexity: O(h) where h is height

        Example:
            >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            >>> DFSSolutions.max_depth_binary_tree(root)
            3
        """
        if not root:
            return 0

        left_depth = DFSSolutions.max_depth_binary_tree(root.left)
        right_depth = DFSSolutions.max_depth_binary_tree(root.right)

        return 1 + max(left_depth, right_depth)

    @staticmethod
    def is_valid_bst(root: Optional[TreeNode]) -> bool:
        """
        Check if tree is a valid binary search tree.

        Time Complexity: O(n)
        Space Complexity: O(h)

        Example:
            >>> root = TreeNode(2, TreeNode(1), TreeNode(3))
            >>> DFSSolutions.is_valid_bst(root)
            True
        """
        def validate(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            if not node:
                return True

            if not (min_val < node.val < max_val):
                return False

            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))

        return validate(root, float('-inf'), float('inf'))

    @staticmethod
    def path_sum(root: Optional[TreeNode], target_sum: int) -> bool:
        """
        Check if tree has root-to-leaf path with given sum.

        Time Complexity: O(n)
        Space Complexity: O(h)

        Example:
            >>> root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8))
            >>> DFSSolutions.path_sum(root, 22)
            True
        """
        if not root:
            return False

        # Check if it's a leaf node
        if not root.left and not root.right:
            return root.val == target_sum

        remaining_sum = target_sum - root.val

        return (DFSSolutions.path_sum(root.left, remaining_sum) or
                DFSSolutions.path_sum(root.right, remaining_sum))

    @staticmethod
    def all_paths_sum(root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
        """
        Find all root-to-leaf paths with given sum.

        Time Complexity: O(n²) in worst case (skewed tree)
        Space Complexity: O(n)

        Example:
            >>> root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8))
            >>> DFSSolutions.all_paths_sum(root, 22)
            [[5, 4, 11, 2]]
        """
        all_paths = []

        def find_paths(node: Optional[TreeNode], remaining: int, path: List[int]) -> None:
            if not node:
                return

            path.append(node.val)

            # Check if it's a leaf and sum matches
            if not node.left and not node.right and node.val == remaining:
                all_paths.append(list(path))
            else:
                find_paths(node.left, remaining - node.val, path)
                find_paths(node.right, remaining - node.val, path)

            path.pop()  # Backtrack

        find_paths(root, target_sum, [])
        return all_paths

    @staticmethod
    def number_of_islands(grid: List[List[str]]) -> int:
        """
        Count number of islands in 2D grid.

        Time Complexity: O(m * n)
        Space Complexity: O(m * n) in worst case

        Example:
            >>> grid = [
            ...     ["1","1","0","0","0"],
            ...     ["1","1","0","0","0"],
            ...     ["0","0","1","0","0"],
            ...     ["0","0","0","1","1"]
            ... ]
            >>> DFSSolutions.number_of_islands(grid)
            3
        """
        if not grid or not grid[0]:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> None:
            if (r < 0 or r >= rows or c < 0 or c >= cols or
                    grid[r][c] != "1"):
                return

            grid[r][c] = "0"  # Mark as visited

            # Explore all 4 directions
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count

    @staticmethod
    def has_cycle_directed(graph: Graph) -> bool:
        """
        Detect cycle in directed graph using DFS.

        Time Complexity: O(V + E)
        Space Complexity: O(V)

        Example:
            >>> g = Graph(directed=True)
            >>> g.add_edge(0, 1)
            >>> g.add_edge(1, 2)
            >>> g.add_edge(2, 0)
            >>> DFSSolutions.has_cycle_directed(g)
            True
        """
        visited = set()
        rec_stack = set()

        def has_cycle_util(v: int) -> bool:
            visited.add(v)
            rec_stack.add(v)

            for neighbor in graph.get_neighbors(v):
                if neighbor not in visited:
                    if has_cycle_util(neighbor):
                        return True
                elif neighbor in rec_stack:
                    return True

            rec_stack.remove(v)
            return False

        for vertex in graph.get_vertices():
            if vertex not in visited:
                if has_cycle_util(vertex):
                    return True

        return False
