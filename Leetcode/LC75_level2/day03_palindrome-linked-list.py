"""
https://leetcode.cn/problems/palindrome-linked-list/
给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true；否则，返回 false 。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverse(self, head=None):
        # inplace operation
        if head is None:
            head = self
        if head.val is None:
            return None
        new_head = ListNode(head.val)  # 1->NULL
        head = head.next  # head: 2->3->4->5->NULL
        while head:
            # temp: 3->4->5->NULL
            temp = head.next  
            # head: 2->1->NULL
            head.next = new_head  
            # new_head: 2->1->NULL
            # cur: 3->4->5->NULL
            new_head, head = head, temp  
        self.val = new_head.val
        self.next = new_head.next
        return new_head

    def isPalindrome(self, head: ListNode) -> bool:
        if head.next is None:
            return True
        dummy = ListNode(val=-1, next=head)
        fast = dummy
        slow = dummy
        while fast is not None and fast.next:
            fast = fast.next.next
            slow = slow.next
        reversed_right_part = self.reverse(slow.next)
        slow.next = None
        left_part = dummy.next
        # print(left_part, reversed_right_part)
        while True:
            if left_part is None or reversed_right_part is None:
                break
            # print(left_part.val, reversed_right_part.val)
            if left_part.val != reversed_right_part.val:
                return False
            left_part = left_part.next
            reversed_right_part = reversed_right_part.next
        return True
