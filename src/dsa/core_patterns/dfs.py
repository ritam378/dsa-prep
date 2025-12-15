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
from dsa.data_structures.tree import TreeNode
from dsa.data_structures.graph import Graph


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

    @staticmethod
    def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        """
        Find lowest common ancestor (LCA) of two nodes in binary tree.

        Difficulty: Medium
        Frequency: VERY HIGH - Amazon, Google, Facebook, Microsoft

        Time Complexity: O(n)
        Space Complexity: O(h)

        Interview Tips:
        - LCA is the deepest node that is ancestor of both p and q
        - If root is one of p or q, root is the LCA
        - If p and q are on different sides, root is LCA
        - For BST, use BST property for O(h) solution

        Example:
            >>> root = TreeNode(3, TreeNode(5), TreeNode(1))
            >>> p = root.left
            >>> q = root.right
            >>> DFSSolutions.lowest_common_ancestor(root, p, q).val
            3
        """
        if not root or root == p or root == q:
            return root

        left = DFSSolutions.lowest_common_ancestor(root.left, p, q)
        right = DFSSolutions.lowest_common_ancestor(root.right, p, q)

        # If both sides return non-null, root is LCA
        if left and right:
            return root

        # Return non-null side (if any)
        return left if left else right

    @staticmethod
    def diameter_binary_tree(root: Optional[TreeNode]) -> int:
        """
        Find diameter of binary tree (longest path between any two nodes).

        Difficulty: Easy
        Frequency: HIGH - Amazon, Google, Microsoft

        Time Complexity: O(n)
        Space Complexity: O(h)

        Interview Tips:
        - Diameter may or may not pass through root
        - For each node, diameter = left_height + right_height
        - Track maximum during traversal

        Example:
            >>> root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
            >>> DFSSolutions.diameter_binary_tree(root)
            3
        """
        max_diameter = [0]

        def height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_height = height(node.left)
            right_height = height(node.right)

            # Update diameter at this node
            max_diameter[0] = max(max_diameter[0], left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)
        return max_diameter[0]

    @staticmethod
    def serialize_tree(root: Optional[TreeNode]) -> str:
        """
        Serialize binary tree to string.

        Difficulty: Hard
        Frequency: VERY HIGH - Amazon, Google, Facebook

        Time Complexity: O(n)
        Space Complexity: O(n)

        Interview Tips:
        - Use pre-order traversal for easy reconstruction
        - Use null markers for empty nodes
        - Alternative: level-order traversal

        Example:
            >>> root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
            >>> s = DFSSolutions.serialize_tree(root)
            >>> s
            '1,2,None,None,3,4,None,None,5,None,None'
        """
        def serialize_helper(node: Optional[TreeNode]) -> List[str]:
            if not node:
                return ["None"]

            return ([str(node.val)] +
                    serialize_helper(node.left) +
                    serialize_helper(node.right))

        return ",".join(serialize_helper(root))

    @staticmethod
    def deserialize_tree(data: str) -> Optional[TreeNode]:
        """
        Deserialize string to binary tree.

        Difficulty: Hard
        Frequency: VERY HIGH - Amazon, Google, Facebook

        Time Complexity: O(n)
        Space Complexity: O(n)

        Interview Tips:
        - Use iterator/index to track position
        - Must match serialization order (pre-order)
        - Handle null markers properly

        Example:
            >>> data = '1,2,None,None,3,4,None,None,5,None,None'
            >>> root = DFSSolutions.deserialize_tree(data)
            >>> root.val
            1
        """
        def deserialize_helper(values: List[str]) -> Optional[TreeNode]:
            val = values.pop(0)
            if val == "None":
                return None

            node = TreeNode(int(val))
            node.left = deserialize_helper(values)
            node.right = deserialize_helper(values)
            return node

        values = data.split(",")
        return deserialize_helper(values)

    @staticmethod
    def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Invert (mirror) a binary tree.

        Difficulty: Easy
        Frequency: HIGH - Google, Amazon

        Time Complexity: O(n)
        Space Complexity: O(h)

        Interview Tips:
        - Swap left and right subtrees recursively
        - Can also use BFS (level-order)
        - Base case: null node returns null

        Example:
            >>> root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7))
            >>> inverted = DFSSolutions.invert_tree(root)
            >>> inverted.right.val
            2
        """
        if not root:
            return None

        # Swap children
        root.left, root.right = root.right, root.left

        # Recursively invert subtrees
        DFSSolutions.invert_tree(root.left)
        DFSSolutions.invert_tree(root.right)

        return root

    @staticmethod
    def is_symmetric(root: Optional[TreeNode]) -> bool:
        """
        Check if binary tree is symmetric (mirror of itself).

        Difficulty: Easy
        Frequency: HIGH - Amazon, Microsoft

        Time Complexity: O(n)
        Space Complexity: O(h)

        Interview Tips:
        - Compare left and right subtrees
        - left.left should equal right.right
        - left.right should equal right.left

        Example:
            >>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
            >>> DFSSolutions.is_symmetric(root)
            True
        """
        def is_mirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            if not left and not right:
                return True
            if not left or not right:
                return False

            return (left.val == right.val and
                    is_mirror(left.left, right.right) and
                    is_mirror(left.right, right.left))

        if not root:
            return True
        return is_mirror(root.left, root.right)

    @staticmethod
    def flatten_tree(root: Optional[TreeNode]) -> None:
        """
        Flatten binary tree to linked list in-place (pre-order).

        Difficulty: Medium
        Frequency: HIGH - Amazon, Microsoft

        Time Complexity: O(n)
        Space Complexity: O(h)

        Interview Tips:
        - Flatten in pre-order: root -> left -> right
        - Use right pointer as 'next', set left to None
        - Can use Morris traversal for O(1) space

        Example:
            >>> root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
            >>> DFSSolutions.flatten_tree(root)
            >>> root.left is None
            True
        """
        def flatten_helper(node: Optional[TreeNode]) -> Optional[TreeNode]:
            """Returns the tail of flattened subtree."""
            if not node:
                return None

            left_tail = flatten_helper(node.left)
            right_tail = flatten_helper(node.right)

            # If there was a left subtree, shuffle connections
            if node.left:
                left_tail.right = node.right
                node.right = node.left
                node.left = None

            # Return the rightmost node
            return right_tail or left_tail or node

        flatten_helper(root)

    @staticmethod
    def kth_smallest_bst(root: Optional[TreeNode], k: int) -> int:
        """
        Find kth smallest element in BST.

        Difficulty: Medium
        Frequency: VERY HIGH - Amazon, Google, Facebook

        Time Complexity: O(h + k) where h is height
        Space Complexity: O(h)

        Interview Tips:
        - In-order traversal of BST gives sorted order
        - Can optimize with iterative + early stop
        - Follow-up: handle frequent queries (augment tree with count)

        Example:
            >>> root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
            >>> DFSSolutions.kth_smallest_bst(root, 1)
            1
        """
        count = [0]
        result = [None]

        def inorder(node: Optional[TreeNode]) -> None:
            if not node or result[0] is not None:
                return

            inorder(node.left)

            count[0] += 1
            if count[0] == k:
                result[0] = node.val
                return

            inorder(node.right)

        inorder(root)
        return result[0]

    @staticmethod
    def count_good_nodes(root: Optional[TreeNode]) -> int:
        """
        Count good nodes (node >= all ancestors on path from root).

        Difficulty: Medium
        Frequency: Medium - Amazon, Google

        Time Complexity: O(n)
        Space Complexity: O(h)

        Interview Tips:
        - Track maximum value on path from root
        - Node is good if val >= max_so_far
        - Root is always good

        Example:
            >>> root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
            >>> DFSSolutions.count_good_nodes(root)
            4
        """
        def dfs(node: Optional[TreeNode], max_so_far: int) -> int:
            if not node:
                return 0

            count = 1 if node.val >= max_so_far else 0
            max_so_far = max(max_so_far, node.val)

            count += dfs(node.left, max_so_far)
            count += dfs(node.right, max_so_far)

            return count

        return dfs(root, float('-inf'))

    @staticmethod
    def max_path_sum(root: Optional[TreeNode]) -> int:
        """
        Find maximum path sum in binary tree (any node to any node).

        Difficulty: Hard
        Frequency: VERY HIGH - Amazon, Google, Facebook

        Time Complexity: O(n)
        Space Complexity: O(h)

        Interview Tips:
        - Path can start and end at any node
        - For each node, max path through it = node + left_max + right_max
        - Return value: max contribution to parent (node + max(left, right))

        Example:
            >>> root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            >>> DFSSolutions.max_path_sum(root)
            42
        """
        max_sum = [float('-inf')]

        def max_gain(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            # Only take positive gains
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # Path through current node
            current_path = node.val + left_gain + right_gain
            max_sum[0] = max(max_sum[0], current_path)

            # Return max contribution to parent
            return node.val + max(left_gain, right_gain)

        max_gain(root)
        return max_sum[0]

    @staticmethod
    def is_subtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Check if subRoot is a subtree of root.

        Difficulty: Easy
        Frequency: HIGH - Amazon, Facebook

        Time Complexity: O(m * n) where m, n are tree sizes
        Space Complexity: O(h)

        Interview Tips:
        - Subtree must match exactly (not just values)
        - Check if trees are same, else recurse on children
        - Alternative: serialize both and check substring

        Example:
            >>> root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
            >>> subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
            >>> DFSSolutions.is_subtree(root, subRoot)
            True
        """
        def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if not p or not q:
                return False
            return (p.val == q.val and
                    is_same_tree(p.left, q.left) and
                    is_same_tree(p.right, q.right))

        if not root:
            return False

        if is_same_tree(root, subRoot):
            return True

        return (DFSSolutions.is_subtree(root.left, subRoot) or
                DFSSolutions.is_subtree(root.right, subRoot))

    @staticmethod
    def construct_tree_inorder_preorder(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        Construct binary tree from preorder and inorder traversals.

        Difficulty: Medium
        Frequency: HIGH - Amazon, Microsoft, Google

        Time Complexity: O(n)
        Space Complexity: O(n)

        Interview Tips:
        - Preorder: root is first element
        - Inorder: elements before root are left subtree
        - Use hashmap for O(1) index lookup in inorder
        - Similar: construct from inorder and postorder

        Example:
            >>> preorder = [3,9,20,15,7]
            >>> inorder = [9,3,15,20,7]
            >>> root = DFSSolutions.construct_tree_inorder_preorder(preorder, inorder)
            >>> root.val
            3
        """
        if not preorder or not inorder:
            return None

        # Build index map for inorder
        inorder_map = {val: i for i, val in enumerate(inorder)}

        def build(pre_start: int, pre_end: int, in_start: int, in_end: int) -> Optional[TreeNode]:
            if pre_start > pre_end:
                return None

            root_val = preorder[pre_start]
            root = TreeNode(root_val)

            # Find root in inorder
            root_idx = inorder_map[root_val]
            left_size = root_idx - in_start

            # Recursively build left and right subtrees
            root.left = build(pre_start + 1, pre_start + left_size,
                            in_start, root_idx - 1)
            root.right = build(pre_start + left_size + 1, pre_end,
                             root_idx + 1, in_end)

            return root

        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

    @staticmethod
    def path_sum_iii(root: Optional[TreeNode], targetSum: int) -> int:
        """
        Count paths (not necessarily root-to-leaf) that sum to target.

        Difficulty: Medium
        Frequency: HIGH - Amazon, Facebook

        Time Complexity: O(n)
        Space Complexity: O(n)

        Interview Tips:
        - Use prefix sum + hashmap (similar to subarray sum)
        - Track cumulative sum from root
        - Count how many times (curr_sum - target) appears
        - Don't forget to remove from map on backtrack

        Example:
            >>> root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(2)), TreeNode(-3))
            >>> DFSSolutions.path_sum_iii(root, 8)
            3
        """
        prefix_sums = {0: 1}  # sum -> count

        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0

            curr_sum += node.val

            # Count paths ending at current node
            count = prefix_sums.get(curr_sum - targetSum, 0)

            # Add current sum to map
            prefix_sums[curr_sum] = prefix_sums.get(curr_sum, 0) + 1

            # Recurse
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)

            # Backtrack: remove current sum
            prefix_sums[curr_sum] -= 1

            return count

        return dfs(root, 0)

    @staticmethod
    def min_depth_binary_tree(root: Optional[TreeNode]) -> int:
        """
        Find minimum depth of binary tree (root to nearest leaf).

        Difficulty: Easy
        Frequency: Medium - Amazon, Microsoft

        Time Complexity: O(n)
        Space Complexity: O(h)

        Interview Tips:
        - Different from max depth: need to find LEAF
        - If only one child exists, must go down that path
        - BFS is more efficient (stops at first leaf)

        Example:
            >>> root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
            >>> DFSSolutions.min_depth_binary_tree(root)
            2
        """
        if not root:
            return 0

        # If one child is missing, go down the other path
        if not root.left:
            return 1 + DFSSolutions.min_depth_binary_tree(root.right)
        if not root.right:
            return 1 + DFSSolutions.min_depth_binary_tree(root.left)

        # Both children exist
        return 1 + min(DFSSolutions.min_depth_binary_tree(root.left),
                      DFSSolutions.min_depth_binary_tree(root.right))
