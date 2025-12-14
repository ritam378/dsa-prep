"""
Tree Data Structure

Binary tree, BST, and related tree structures.
"""

from typing import Optional, Any, List
from collections import deque


class TreeNode:
    """Binary tree node."""

    def __init__(
        self,
        val: int = 0,
        left: Optional['TreeNode'] = None,
        right: Optional['TreeNode'] = None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"TreeNode({self.val})"


class BinaryTree:
    """Binary tree with common operations."""

    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root

    def inorder_traversal(self) -> List[int]:
        """Inorder traversal: left -> root -> right."""
        result = []

        def inorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)

        inorder(self.root)
        return result

    def preorder_traversal(self) -> List[int]:
        """Preorder traversal: root -> left -> right."""
        result = []

        def preorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)

        preorder(self.root)
        return result

    def postorder_traversal(self) -> List[int]:
        """Postorder traversal: left -> right -> root."""
        result = []

        def postorder(node: Optional[TreeNode]) -> None:
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)

        postorder(self.root)
        return result

    def level_order_traversal(self) -> List[List[int]]:
        """Level order traversal (BFS)."""
        if not self.root:
            return []

        result = []
        queue = deque([self.root])

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

    def height(self) -> int:
        """Calculate the height of the tree."""
        def get_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        return get_height(self.root)


class BST:
    """Binary Search Tree implementation."""

    def __init__(self):
        self.root: Optional[TreeNode] = None

    def insert(self, val: int) -> None:
        """Insert a value into the BST."""
        def insert_helper(node: Optional[TreeNode], val: int) -> TreeNode:
            if not node:
                return TreeNode(val)

            if val < node.val:
                node.left = insert_helper(node.left, val)
            elif val > node.val:
                node.right = insert_helper(node.right, val)

            return node

        self.root = insert_helper(self.root, val)

    def search(self, val: int) -> bool:
        """Search for a value in the BST."""
        def search_helper(node: Optional[TreeNode], val: int) -> bool:
            if not node:
                return False
            if node.val == val:
                return True
            if val < node.val:
                return search_helper(node.left, val)
            return search_helper(node.right, val)

        return search_helper(self.root, val)

    def delete(self, val: int) -> None:
        """Delete a value from the BST."""
        def delete_helper(node: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            if not node:
                return None

            if val < node.val:
                node.left = delete_helper(node.left, val)
            elif val > node.val:
                node.right = delete_helper(node.right, val)
            else:
                # Node to delete found
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left

                # Node has two children
                min_node = self._find_min(node.right)
                node.val = min_node.val
                node.right = delete_helper(node.right, min_node.val)

            return node

        self.root = delete_helper(self.root, val)

    def _find_min(self, node: TreeNode) -> TreeNode:
        """Find the minimum value node in a subtree."""
        while node.left:
            node = node.left
        return node
