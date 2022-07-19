# Definition for singly-linked list.
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class CDListNode(ListNode):
    def __init__(self, val=-1, next=None):
        if isinstance(val, list):
            if len(val) > 0:
                self.init_with_list(val)
            else:
                self.is_empty = True
        elif isinstance(val, ListNode):
            super().__init__(val.val, val.next)
        else:
            super().__init__(val, next)
    
    def init_with_list(self, val_list):
        head = ListNode(-1)
        cur = head
        for v in val_list:
            cur.next = ListNode(v)
            cur = cur.next
        if head.next:
            self.val = head.next.val
            self.next = head.next.next
        return self

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

    def to_listnode(self, head=None):
        if head is None:
            head = self
        if head.val is None:
            return None
        return ListNode(head.val, head.next)

    def to_list(self, head=None):
        if head is None:
            head = self
        val_list = []
        cur = head
        while cur:
            if cur.val is None:
                break
            val_list.append(cur.val)
            cur = cur.next
        return val_list

    def to_string(self, head=None, delim='-'):
        if head is None:
            head = self
        return delim.join(map(str, self.to_list()))

    def __repr__(self):
        # print(self) does not change it
        # => 1-2-2-3-4-4-6
        return self.to_string()


class ListNodeSort:

    @staticmethod
    def sortList(head: ListNode) -> ListNode:
        # sort a listnode
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
            _, idx = pq.get()
            pivot.next = lists[idx]
            lists[idx] = lists[idx].next
            if lists[idx]:
                pq.put((lists[idx].val, idx))
            pivot = pivot.next

        return head.next


if __name__ == "__main__":
    l1 = CDListNode([1,2,3,4])
    l2 = CDListNode([2,4,6])
    print(l1, l2)
    print(l1, l2)
    print(l1.to_list(l1.reverse()))

    lns = ListNodeSort()
    l1 = CDListNode([1,2,3,4])
    print(lns.merge(l1, l2))
