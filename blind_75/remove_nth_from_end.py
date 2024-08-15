"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.

"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get length of list
        if head.next is None:
            return None
        node = head
        i = 0
        while node:
            node = node.next
            i += 1

        n_from_end = i - n
        node = head
        j = 0
        prev = None
        while j < n_from_end:
            prev = node
            print(node.val)
            node = node.next
            j += 1
        if not prev:
            return node.next
        prev.next = node.next
        return head
