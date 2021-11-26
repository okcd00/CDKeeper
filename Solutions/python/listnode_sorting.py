# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeSort:
    def merge(self, lef_head, rig_head):
        # merge two sorted listnodes
        dummy_node = ListNode(-1)
        pivot = dummy_node
        
        while lef_head and rig_head:
            if lef_head.val <= rig_head.val:
                pivot.next = lef_head
                lef_head = lef_head.next
                pivot = pivot.next
            else:
                pivot.next = rig_head
                rig_head = rig_head.next
                pivot = pivot.next
        if lef_head:
            pivot.next = lef_head
        elif rig_head:
            pivot.next = rig_head
        return dummy_node.next
    
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # merge k sorted listnodes
        if len(lists) == 0:
            return None
        
        list_size = len(lists)
        if list_size == 1:
            return lists[0]
        elif list_size == 2:
            return self.merge(lists[0], lists[1])
        lef_list, rig_list = lists[:list_size//2], lists[list_size//2:]
        return self.merge(self.mergeKLists(lef_list), 
                          self.mergeKLists(rig_list))

    def mergeKLists_pq(self, lists: List[ListNode]) -> ListNode:
        # merge k sorted listnodes with priority queue
        if len(lists) == 0:
            return None
        dummy_node = ListNode(-1) 
        pivot = dummy_node
        
        from queue import PriorityQueue
        pq = PriorityQueue()
        for idx, ln in enumerate(lists):
            if ln:
                pq.put((ln.val, idx))
        
        while not pq.empty():
            val, idx = pq.get()
            pivot.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx]:
                pq.put((lists[idx].val, idx))
            pivot = pivot.next

        return dummy_node.next


if __name__ == "__main__":
    lns = ListNodeSort()
