"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        res = [[1]]
        for i in range(1, rowIndex + 1):
            row = [1] + [i + j for i, j in zip(res[i-1], res[i-1][1:])] + [1]
            res.append(row)
        return res[rowIndex]

if __name__ == '__main__':
    res = Solution().getRow(1)
    print(res)

