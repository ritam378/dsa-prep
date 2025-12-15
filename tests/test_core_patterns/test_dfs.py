"""
Comprehensive tests for DFS and Tree problems.
"""

import pytest
from dsa.core_patterns.dfs import DFSSolutions
from dsa.data_structures.tree import TreeNode
from dsa.data_structures.graph import Graph


class TestMaxDepth:
    """Tests for Maximum Depth of Binary Tree."""

    def test_basic_example(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert DFSSolutions.max_depth_binary_tree(root) == 3

    def test_single_node(self):
        assert DFSSolutions.max_depth_binary_tree(TreeNode(1)) == 1

    def test_empty_tree(self):
        assert DFSSolutions.max_depth_binary_tree(None) == 0

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert DFSSolutions.max_depth_binary_tree(root) == 3

    def test_right_skewed(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        assert DFSSolutions.max_depth_binary_tree(root) == 3


class TestValidBST:
    """Tests for Validate Binary Search Tree."""

    def test_valid_bst(self):
        root = TreeNode(2, TreeNode(1), TreeNode(3))
        assert DFSSolutions.is_valid_bst(root) == True

    def test_invalid_bst(self):
        root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
        assert DFSSolutions.is_valid_bst(root) == False

    def test_single_node(self):
        assert DFSSolutions.is_valid_bst(TreeNode(1)) == True

    def test_empty_tree(self):
        assert DFSSolutions.is_valid_bst(None) == True


class TestPathSum:
    """Tests for Path Sum problems."""

    def test_path_sum_exists(self):
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8))
        assert DFSSolutions.path_sum(root, 22) == True

    def test_path_sum_not_exists(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert DFSSolutions.path_sum(root, 5) == False

    def test_all_paths_sum(self):
        root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))), TreeNode(8))
        paths = DFSSolutions.all_paths_sum(root, 22)
        assert [5, 4, 11, 2] in paths


class TestNumberOfIslands:
    """Tests for Number of Islands."""

    def test_basic_example(self):
        grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
        ]
        assert DFSSolutions.number_of_islands(grid) == 3

    def test_single_island(self):
        grid = [["1","1"],["1","1"]]
        assert DFSSolutions.number_of_islands(grid) == 1

    def test_no_islands(self):
        grid = [["0","0"],["0","0"]]
        assert DFSSolutions.number_of_islands(grid) == 0

    def test_empty_grid(self):
        assert DFSSolutions.number_of_islands([]) == 0


class TestLowestCommonAncestor:
    """Tests for Lowest Common Ancestor."""

    def test_basic_example(self):
        root = TreeNode(3, TreeNode(5), TreeNode(1))
        p = root.left
        q = root.right
        assert DFSSolutions.lowest_common_ancestor(root, p, q).val == 3

    def test_one_is_ancestor(self):
        root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2)), TreeNode(1))
        p = root.left
        q = root.left.right
        lca = DFSSolutions.lowest_common_ancestor(root, p, q)
        assert lca.val == 5

    def test_same_node(self):
        root = TreeNode(3, TreeNode(5), TreeNode(1))
        p = root.left
        lca = DFSSolutions.lowest_common_ancestor(root, p, p)
        assert lca.val == 5


class TestDiameterBinaryTree:
    """Tests for Diameter of Binary Tree."""

    def test_basic_example(self):
        root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
        assert DFSSolutions.diameter_binary_tree(root) == 3

    def test_single_node(self):
        assert DFSSolutions.diameter_binary_tree(TreeNode(1)) == 0

    def test_two_nodes(self):
        root = TreeNode(1, TreeNode(2))
        assert DFSSolutions.diameter_binary_tree(root) == 1

    def test_skewed_tree(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
        assert DFSSolutions.diameter_binary_tree(root) == 3


class TestSerializeDeserialize:
    """Tests for Tree Serialization and Deserialization."""

    def test_basic_tree(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        serialized = DFSSolutions.serialize_tree(root)
        deserialized = DFSSolutions.deserialize_tree(serialized)
        assert deserialized.val == 1
        assert deserialized.left.val == 2
        assert deserialized.right.val == 3

    def test_empty_tree(self):
        serialized = DFSSolutions.serialize_tree(None)
        assert DFSSolutions.deserialize_tree(serialized) is None

    def test_single_node(self):
        root = TreeNode(42)
        serialized = DFSSolutions.serialize_tree(root)
        deserialized = DFSSolutions.deserialize_tree(serialized)
        assert deserialized.val == 42


class TestInvertTree:
    """Tests for Invert Binary Tree."""

    def test_basic_example(self):
        root = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9)))
        inverted = DFSSolutions.invert_tree(root)
        assert inverted.right.val == 2
        assert inverted.left.val == 7

    def test_single_node(self):
        root = TreeNode(1)
        inverted = DFSSolutions.invert_tree(root)
        assert inverted.val == 1

    def test_empty_tree(self):
        assert DFSSolutions.invert_tree(None) is None


class TestSymmetricTree:
    """Tests for Symmetric Tree."""

    def test_symmetric(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(4), TreeNode(3)))
        assert DFSSolutions.is_symmetric(root) == True

    def test_not_symmetric(self):
        root = TreeNode(1, TreeNode(2, None, TreeNode(3)), TreeNode(2, None, TreeNode(3)))
        assert DFSSolutions.is_symmetric(root) == False

    def test_single_node(self):
        assert DFSSolutions.is_symmetric(TreeNode(1)) == True

    def test_empty_tree(self):
        assert DFSSolutions.is_symmetric(None) == True


class TestFlattenTree:
    """Tests for Flatten Binary Tree to Linked List."""

    def test_basic_example(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(5, None, TreeNode(6)))
        DFSSolutions.flatten_tree(root)
        assert root.left is None
        assert root.right.val == 2

    def test_single_node(self):
        root = TreeNode(1)
        DFSSolutions.flatten_tree(root)
        assert root.val == 1
        assert root.left is None

    def test_already_flat(self):
        root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
        DFSSolutions.flatten_tree(root)
        assert root.right.val == 2


class TestKthSmallestBST:
    """Tests for Kth Smallest Element in BST."""

    def test_basic_example(self):
        root = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
        assert DFSSolutions.kth_smallest_bst(root, 1) == 1

    def test_kth_is_root(self):
        root = TreeNode(5, TreeNode(3, TreeNode(2), TreeNode(4)), TreeNode(6))
        assert DFSSolutions.kth_smallest_bst(root, 3) == 4

    def test_single_node(self):
        assert DFSSolutions.kth_smallest_bst(TreeNode(1), 1) == 1


class TestCountGoodNodes:
    """Tests for Count Good Nodes."""

    def test_basic_example(self):
        root = TreeNode(3, TreeNode(1, TreeNode(3)), TreeNode(4, TreeNode(1), TreeNode(5)))
        assert DFSSolutions.count_good_nodes(root) == 4

    def test_all_good(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert DFSSolutions.count_good_nodes(root) == 3

    def test_single_node(self):
        assert DFSSolutions.count_good_nodes(TreeNode(1)) == 1


class TestMaxPathSum:
    """Tests for Binary Tree Maximum Path Sum."""

    def test_basic_example(self):
        root = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert DFSSolutions.max_path_sum(root) == 42

    def test_all_negative(self):
        root = TreeNode(-3, TreeNode(-1), TreeNode(-2))
        assert DFSSolutions.max_path_sum(root) == -1

    def test_single_node(self):
        assert DFSSolutions.max_path_sum(TreeNode(5)) == 5

    def test_positive_path(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert DFSSolutions.max_path_sum(root) == 6


class TestIsSubtree:
    """Tests for Subtree of Another Tree."""

    def test_is_subtree(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
        subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
        assert DFSSolutions.is_subtree(root, subRoot) == True

    def test_not_subtree(self):
        root = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2, TreeNode(0))), TreeNode(5))
        subRoot = TreeNode(4, TreeNode(1), TreeNode(2))
        assert DFSSolutions.is_subtree(root, subRoot) == False

    def test_same_tree(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        subRoot = TreeNode(1, TreeNode(2), TreeNode(3))
        assert DFSSolutions.is_subtree(root, subRoot) == True


class TestConstructTree:
    """Tests for Construct Binary Tree from Preorder and Inorder."""

    def test_basic_example(self):
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        root = DFSSolutions.construct_tree_inorder_preorder(preorder, inorder)
        assert root.val == 3
        assert root.left.val == 9
        assert root.right.val == 20

    def test_single_node(self):
        root = DFSSolutions.construct_tree_inorder_preorder([1], [1])
        assert root.val == 1

    def test_empty(self):
        assert DFSSolutions.construct_tree_inorder_preorder([], []) is None

    def test_left_skewed(self):
        preorder = [3,2,1]
        inorder = [1,2,3]
        root = DFSSolutions.construct_tree_inorder_preorder(preorder, inorder)
        assert root.val == 3
        assert root.left.val == 2
        assert root.left.left.val == 1


class TestPathSumIII:
    """Tests for Path Sum III."""

    def test_basic_example(self):
        root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3), TreeNode(-2)), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
        assert DFSSolutions.path_sum_iii(root, 8) == 3

    def test_single_path(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        assert DFSSolutions.path_sum_iii(root, 3) == 2

    def test_negative_numbers(self):
        root = TreeNode(1, None, TreeNode(-2, TreeNode(-3)))
        assert DFSSolutions.path_sum_iii(root, -1) >= 1


class TestMinDepth:
    """Tests for Minimum Depth of Binary Tree."""

    def test_basic_example(self):
        root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
        assert DFSSolutions.min_depth_binary_tree(root) == 2

    def test_single_node(self):
        assert DFSSolutions.min_depth_binary_tree(TreeNode(1)) == 1

    def test_left_skewed(self):
        root = TreeNode(1, TreeNode(2, TreeNode(3)))
        assert DFSSolutions.min_depth_binary_tree(root) == 3

    def test_empty_tree(self):
        assert DFSSolutions.min_depth_binary_tree(None) == 0


class TestHasCycleDirected:
    """Tests for Cycle Detection in Directed Graph."""

    def test_has_cycle(self):
        g = Graph(directed=True)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        g.add_edge(2, 0)
        assert DFSSolutions.has_cycle_directed(g) == True

    def test_no_cycle(self):
        g = Graph(directed=True)
        g.add_edge(0, 1)
        g.add_edge(1, 2)
        assert DFSSolutions.has_cycle_directed(g) == False

    def test_self_loop(self):
        g = Graph(directed=True)
        g.add_edge(0, 0)
        assert DFSSolutions.has_cycle_directed(g) == True


class TestTreeEdgeCases:
    """Test edge cases across tree problems."""

    def test_null_trees(self):
        assert DFSSolutions.max_depth_binary_tree(None) == 0
        assert DFSSolutions.is_valid_bst(None) == True
        assert DFSSolutions.path_sum(None, 0) == False

    def test_single_nodes(self):
        node = TreeNode(5)
        assert DFSSolutions.max_depth_binary_tree(node) == 1
        assert DFSSolutions.diameter_binary_tree(node) == 0
        assert DFSSolutions.count_good_nodes(node) == 1

    def test_large_tree(self):
        # Build a complete binary tree of depth 10
        def build_complete_tree(depth):
            if depth == 0:
                return None
            return TreeNode(1, build_complete_tree(depth-1), build_complete_tree(depth-1))

        root = build_complete_tree(5)
        assert DFSSolutions.max_depth_binary_tree(root) == 5
