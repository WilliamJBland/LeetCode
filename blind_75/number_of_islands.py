"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume
all four edges of the grid are all surrounded by water.
"""
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or (r, c) in visited or grid[r][c] == "0":
                return
            visited.add((r, c))
            dfs(r, c + 1)
            dfs(r, c - 1)
            dfs(r + 1, c)
            dfs(r - 1, c)

        for r in range(rows):
            for c in range(cols):
                if (r, c) in visited or grid[r][c] == "0":
                    continue
                else:
                    islands += 1
                    dfs(r, c)
        return islands





if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    res = Solution().search(nums, target)
    print(res)
