"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values
of the nodes in the tree."""


# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def __init__(self):
#         self.res = []
#
#     def dfs(self, root, k):
#         if root.left:
#             self.dfs(root.left, k)
#
#         if len(self.res) == k:
#             return self.res[-1]
#
#         self.res.append(root.val)
#         if root.right:
#             self.dfs(root.right, k)
#
#     def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
#         return self.dfs(root, k) or self.res[-1]

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        current_node = root
        n = 0
        while current_node or stack:
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            current_node = stack.pop()
            n += 1
            if n == k:
                return current_node.val
            current_node = current_node.right






if __name__ == '__main__':
    # [4,2,5,null,3]
    three = TreeNode(3, None, None)
    two = TreeNode(2, None, three)
    five = TreeNode(5, None, None)
    four = TreeNode(4, two, five)

    Solution().kthSmallest(five, 1)
