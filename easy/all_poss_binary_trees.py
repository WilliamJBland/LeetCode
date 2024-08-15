"""
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer
must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    dp = {}
    def backtrack(self, n: int):
        if n in {0, 2}:
            return []
        if n == 1:
            return [TreeNode()]

        if n in self.dp:
            return self.dp[n]

        res = []
        for l in range(n - 1):
            r = n - 1 - l
            left_trees = self.allPossibleFBT(l)
            right_trees = self.allPossibleFBT(r)
            for j in left_trees:
                for k in right_trees:
                    res.append(TreeNode(0, j, k))
        self.dp[n] = res
        return res

    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        return self.backtrack(n)



if __name__ == '__main__':
    res = Solution().allPossibleFBT(5)
    print(res)

