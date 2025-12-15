"""
Breadth-First Search (BFS) Pattern

Pattern: Explore all neighbors before going deeper.
When to use:
- Level-order traversal
- Shortest path in unweighted graphs
- Finding minimum depth
- Finding all nodes at distance k

Time Complexity: O(V + E) for graphs, O(n) for trees
Space Complexity: O(w) where w is maximum width
"""

from typing import List, Optional, Set
from collections import deque
from dsa.data_structures.tree import TreeNode
from dsa.data_structures.graph import Graph


class BFSSolutions:
    """Solutions using the breadth-first search pattern."""

    @staticmethod
    def level_order_traversal(root: Optional[TreeNode]) -> List[List[int]]:
        """
        Level order traversal of binary tree.

        Time Complexity: O(n)
        Space Complexity: O(w) where w is maximum width

        Example:
            >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            >>> BFSSolutions.level_order_traversal(root)
            [[3], [9, 20], [15, 7]]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return result

    @staticmethod
    def min_depth(root: Optional[TreeNode]) -> int:
        """
        Find minimum depth of binary tree.

        Time Complexity: O(n)
        Space Complexity: O(w)

        Example:
            >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            >>> BFSSolutions.min_depth(root)
            2
        """
        if not root:
            return 0

        queue = deque([(root, 1)])

        while queue:
            node, depth = queue.popleft()

            # If it's a leaf node
            if not node.left and not node.right:
                return depth

            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        return 0

    @staticmethod
    def zigzag_level_order(root: Optional[TreeNode]) -> List[List[int]]:
        """
        Zigzag level order traversal.

        Time Complexity: O(n)
        Space Complexity: O(w)

        Example:
            >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            >>> BFSSolutions.zigzag_level_order(root)
            [[3], [20, 9], [15, 7]]
        """
        if not root:
            return []

        result = []
        queue = deque([root])
        left_to_right = True

        while queue:
            level_size = len(queue)
            current_level = deque()

            for _ in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    current_level.append(node.val)
                else:
                    current_level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(current_level))
            left_to_right = not left_to_right

        return result

    @staticmethod
    def right_side_view(root: Optional[TreeNode]) -> List[int]:
        """
        Return values of nodes visible from right side.

        Time Complexity: O(n)
        Space Complexity: O(w)

        Example:
            >>> root = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, None, TreeNode(4)))
            >>> BFSSolutions.right_side_view(root)
            [1, 3, 4]
        """
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                # Add the rightmost node of each level
                if i == level_size - 1:
                    result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result

    @staticmethod
    def shortest_path_binary_matrix(grid: List[List[int]]) -> int:
        """
        Find shortest path in binary matrix (8-directional).

        Time Complexity: O(n²)
        Space Complexity: O(n²)

        Example:
            >>> grid = [[0,0,0],[1,1,0],[1,1,0]]
            >>> BFSSolutions.shortest_path_binary_matrix(grid)
            4
        """
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        # 8 directions
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        queue = deque([(0, 0, 1)])  # (row, col, distance)
        grid[0][0] = 1  # Mark as visited

        while queue:
            row, col, dist = queue.popleft()

            if row == n - 1 and col == n - 1:
                return dist

            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc

                if (0 <= new_row < n and 0 <= new_col < n and
                        grid[new_row][new_col] == 0):
                    grid[new_row][new_col] = 1  # Mark as visited
                    queue.append((new_row, new_col, dist + 1))

        return -1

    @staticmethod
    def word_ladder(begin_word: str, end_word: str, word_list: List[str]) -> int:
        """
        Find shortest transformation sequence length.

        Time Complexity: O(M² * N) where M is word length, N is word list size
        Space Complexity: O(M * N)

        Example:
            >>> BFSSolutions.word_ladder("hit", "cog", ["hot","dot","dog","lot","log","cog"])
            5
        """
        word_set = set(word_list)

        if end_word not in word_set:
            return 0

        queue = deque([(begin_word, 1)])

        while queue:
            current_word, length = queue.popleft()

            if current_word == end_word:
                return length

            # Try all possible one-letter changes
            for i in range(len(current_word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = current_word[:i] + c + current_word[i+1:]

                    if next_word in word_set:
                        word_set.remove(next_word)
                        queue.append((next_word, length + 1))

        return 0
