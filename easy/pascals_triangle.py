"""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it.

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
"""


class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        for i in range(1, numRows):
            result.append([1] + [i + j for i, j in zip(result[i - 1], result[i - 1][1:])] + [1])
        return result




if __name__ == '__main__':
    res = Solution().generate(3)
    for row in res:
        print(row)

