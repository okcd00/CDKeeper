"""
https://leetcode.cn/problems/sort-list/

给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def merge(self, lef_head, rig_head):
        # merge two sorted listnodes
        head = ListNode(-1)
        pivot = head
        
        while lef_head and rig_head:
            if lef_head.val <= rig_head.val:
                temp = lef_head.next
                lef_head.next = None
                pivot.next = lef_head
                lef_head = temp
                # update pivot
                pivot = pivot.next
            else:
                temp = rig_head.next
                rig_head.next = None
                pivot.next = rig_head
                rig_head = temp
                # update pivot
                pivot = pivot.next
        if lef_head:
            pivot.next = lef_head
        elif rig_head:
            pivot.next = rig_head
        return head.next

    def sortList(self, head: ListNode) -> ListNode:
        h, length, intv = head, 0, 1
        while h: h, length = h.next, length + 1
        res = ListNode(0)
        res.next = head
        # merge the list in different intv.
        while intv < length:
            pre, h = res, res.next
            while h:
                # get the two merge head `h1`, `h2`
                h1, i = h, intv
                while i and h: 
                    h, i = h.next, i - 1
                if i: 
                    # no need to merge because the `h2` is None.
                    break  
                h2, i = h, intv
                while i and h: 
                    h, i = h.next, i - 1
                # the `c2`: length of `h2` can be small than the `intv`.
                c1, c2 = intv, intv - i  
                # merge the `h1` and `h2`.
                while c1 and c2:
                    if h1.val < h2.val: 
                        pre.next, h1, c1 = h1, h1.next, c1 - 1
                    else: 
                        pre.next, h2, c2 = h2, h2.next, c2 - 1
                    pre = pre.next
                pre.next = h1 if c1 else h2
                while c1 > 0 or c2 > 0: 
                    pre, c1, c2 = pre.next, c1 - 1, c2 - 1
                pre.next = h 
            intv *= 2
        return res.next
