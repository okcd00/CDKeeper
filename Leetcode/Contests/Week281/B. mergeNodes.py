# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        dummy.next = head
        cur = dummy
        pivot = None
        
        while cur.next:
            # sum_value = 0
            pivot = cur
            while cur.next and cur.next.val != 0:
                cur = cur.next
                pivot.val += cur.val
            pivot.next = cur.next
            cur = cur.next
        pivot.next = None
        return dummy.next
                
            
            