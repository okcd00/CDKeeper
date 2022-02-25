# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        acc = int((l1.val + l2.val) / 10)
        dig = (l1.val + l2.val) % 10
        ret = ListNode(dig)
        cur = ListNode(0)
        cur = ret
        while l1.next or l2.next or acc>0:
            dig = 0
            cur.next = ListNode(0)
            cur = cur.next
            if l1.next:
                l1 = l1.next
                dig += l1.val
            if l2.next:
                l2 = l2.next
                dig += l2.val
            dig += acc
            acc = int(dig / 10)
            dig = dig % 10
            cur.val = dig
        return ret