"""
https://leetcode.cn/problems/odd-even-linked-list/

给定单链表的头节点 head ，将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd = ListNode(-1)
        even = ListNode(-1)
        odd_head = odd
        even_head = even
        index = 0
        while head is not None:
            index += 1
            if index % 2 == 1:
                odd.next = head
                head = head.next
                odd = odd.next
                odd.next = None
            else:
                even.next = head
                head = head.next
                even = even.next
                even.next = None
        odd.next = even_head.next
        return odd_head.next