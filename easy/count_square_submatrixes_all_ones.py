"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.
"""


class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        c = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    c += 1
        return c

if __name__ == '__main__':
    matrix = [
        [0, 1, 1, 1],
        [1, 1, 1, 1],
        [0, 1, 1, 1]
    ]
    res = Solution().countSquares(matrix)

    print(res)

