# encoding: utf-8
# a = input("please input a number:")
# print("hello world")


class ListNode():
    def __init__(self, val, _next=None) -> None:
        self.val = val
        self.next = _next


def rotate_listnode(root, k=0):
    if root is None:
        if k != 0:
            raise ValueError("Invalid empty input.")
        else:
            return root
        
    dummy = ListNode(-1)
    dummy.next = root  # record old head
    
    size = 0
    pivot = dummy.next
    tail_node = None
    while True:
        if pivot.next is None:
            tail_node = pivot  # record tail node, alias
            size += 1
            break
        pivot = pivot.next
        size += 1
    k = k % size
    
    pivot = dummy.next
    # 1->2->3-x->4->5  k=5-2-1=2
    # 4->5->1->2->3 / 1 step to get the "pre" node
    for _ in range(size-k-1):  
        pivot = pivot.next
    pre = pivot  # pre-node of the cutting position
    new_head = pre.next
    pre.next = None  # 
    tail_node.next = dummy.next  # tail -> old_head
    del dummy
    return new_head


if __name__ == "__main__":
    test_root = ListNode(1)
