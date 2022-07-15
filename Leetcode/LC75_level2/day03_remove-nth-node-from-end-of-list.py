"""
https://leetcode.cn/problems/remove-nth-node-from-end-of-list/
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(val=-1, next=head)
        fast = dummy
        while n > 0:
            fast = fast.next
            n -= 1
        slow = dummy
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next