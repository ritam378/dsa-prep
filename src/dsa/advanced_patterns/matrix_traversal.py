"""
Matrix Traversal Pattern (Island Pattern)

Pattern: Traverse 2D grid using DFS/BFS.
When to use:
- Island counting
- Flood fill
- Matrix region problems
- Surrounded regions

Time Complexity: O(m * n)
Space Complexity: O(m * n)
"""

from typing import List


class MatrixTraversalSolutions:
    """Solutions using the matrix traversal pattern."""

    @staticmethod
    def num_islands(grid: List[List[str]]) -> int:
        """
        Count number of islands.

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        count = 0

        def dfs(r: int, c: int) -> None:
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1'):
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count

    @staticmethod
    def max_area_island(grid: List[List[int]]) -> int:
        """
        Find maximum area of island.

        Time Complexity: O(m * n)
        Space Complexity: O(m * n)
        """
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            if (r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != 1):
                return 0
            grid[r][c] = 0
            return 1 + dfs(r+1, c) + dfs(r-1, c) + dfs(r, c+1) + dfs(r, c-1)

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))

        return max_area
