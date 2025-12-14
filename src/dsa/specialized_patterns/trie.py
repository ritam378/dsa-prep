"""
Trie Pattern (Prefix Tree)

Pattern: Tree structure for efficient string operations.
When to use:
- Autocomplete
- Spell checker
- Longest common prefix
- Word search problems

Time Complexity: O(m) where m is string length
Space Complexity: O(ALPHABET_SIZE * m * n)
"""

from typing import Optional, List


class TrieNode:
    """Node in Trie data structure."""

    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    """Trie (Prefix Tree) implementation."""

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Insert a word into trie.

        Time Complexity: O(m)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        """
        Search for exact word in trie.

        Time Complexity: O(m)
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        """
        Check if any word starts with prefix.

        Time Complexity: O(m)
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
