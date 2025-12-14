"""
Modified Binary Search Pattern

Pattern: Binary search on answer space or modified arrays.
When to use:
- Search in rotated array
- Finding minimum in rotated array
- Search in 2D matrix
- Binary search on answer

Time Complexity: O(log n)
Space Complexity: O(1)
"""

from typing import List


class ModifiedBinarySearchSolutions:
    """Solutions using modified binary search pattern."""

    @staticmethod
    def search_2d_matrix(matrix: List[List[int]], target: int) -> bool:
        """
        Search in 2D sorted matrix.

        Time Complexity: O(log(m*n))
        Space Complexity: O(1)
        """
        if not matrix or not matrix[0]:
            return False

        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = matrix[mid // cols][mid % cols]

            if mid_val == target:
                return True
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
