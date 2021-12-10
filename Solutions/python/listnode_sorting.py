# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next
        if isinstance(val, list):
            self.init_with_list(val)
    
    def init_with_list(self, val_list):
        head = ListNode()
        cur = head
        for v in val_list:
            cur.next = ListNode(v)
            cur = cur.next
        self.val = head.next.val
        self.next = head.next.next

    def reverse(self, head=None):
        # inplace operation
        if head is None:
            head = self
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

    def __repr__(self):
        # print(self) does not change it
        # => 1-2-2-3-4-4-6
        val_list = []
        cur = self
        while cur:
            val_list.append(str(cur.val))
            cur = cur.next
        return '-'.join(val_list)


class ListNodeSort:
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
    
    def mergeKLists(self, lists) -> ListNode:
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

    def mergeKLists_pq(self, lists) -> ListNode:
        # merge k sorted listnodes with priority queue
        if len(lists) == 0:
            return None
        head = ListNode(-1) 
        pivot = head
        
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

        return head.next


if __name__ == "__main__":
    l1 = ListNode([1,2,3,4])
    l2 = ListNode([2,4,6])
    print(l1, l2)
    print(l1, l2)
    print(l1.reverse(l1))

    lns = ListNodeSort()
    l1 = ListNode([1,2,3,4])
    print(lns.merge(l1, l2))
