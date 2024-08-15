"""
Given the head of a singly linked list, reverse the list, and return the reversed list.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        res = []
        node = head
        while node:
            res.append(node)
            node = node.next
        for i in range(len(res)-1, -1, -1):
            res[i].next = res[i-1]
        res[0].next = None
        return res[-1]

if __name__ == '__main__':
    last = ListNode(2, None)
    mid = ListNode(1, last)
    first = ListNode(0, mid)
    res = Solution().reverseList(first)
    print(res)
