"""
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

"""


class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        s = 0
        r_in = -1
        for i in range(len(grid) -1, -1, -1):
            if r_in == len(grid[0]):
                return s
            for j in range(len(grid[0])-1, r_in, -1):
                if grid[i][j] < 0:
                    s += 1
                else:
                    r_in = j
        return s

if __name__ == '__main__':
    grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    res = Solution().countNegatives(grid)
    print(res)