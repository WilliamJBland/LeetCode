"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""


# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and not list2:
            return list1
        if list2 and not list1:
            return list2
        if not list2 and not list1:
            return None
        if list1.val < list2.val:
            start_node = list1
            list1 = list1.next
        else:
            start_node = list2
            list2 = list2.next
        head = start_node
        while list1 or list2:
            if not list2:
                start_node.next = list1
                start_node = start_node.next
                list1 = list1.next
                continue
            if not list1:
                start_node.next = list2
                start_node = start_node.next
                list2 = list2.next
                continue

            if list1.val < list2.val:
                start_node.next = list1
                start_node = start_node.next
                list1 = list1.next
            else:
                start_node.next = list2
                start_node = start_node.next
                list2 = list2.next
        return head



if __name__ == '__main__':
    last = ListNode(4, None)
    mid = ListNode(2, last)
    first = ListNode(0, mid)
    last_1 = ListNode(5, None)
    mid_1 = ListNode(3, last_1)
    first_1 = ListNode(1, mid_1)
    res = Solution().mergeTwoLists(first, first_1)
    while res:
        print(res.val)
        res = res.next
    print(res)