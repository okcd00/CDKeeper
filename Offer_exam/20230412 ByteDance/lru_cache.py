# encoding: utf-8

class BiDirectionalNode(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.post = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.head = BiDirectionalNode()
        self.tail = BiDirectionalNode()
        self.head.post = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        self.current_size = 0

    def get(self, key: int) -> int:
        node = self.hashmap.get(key)
        if node is None:
            return -1
        self.insert_to_head(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if self.hashmap.get(key) is not None:
            self.hashmap[key] = value
            return
        new_node = BiDirectionalNode(key, value)
        self.insert_to_head(new_node)
        self.hashmap[key] = new_node
        self.current_size += 1
        while self.current_size > self.capacity:
            self.drop_tail()

    def insert_to_head(self, new_node) -> None:
        prev_to_insert = self.head.post
        post_to_insert = prev_to_insert.prev
        new_node.prev = prev_to_insert
        new_node.post = post_to_insert
        self.head.post = new_node
        post_to_insert.prev = new_node

    def drop_tail(self):
        drop = self.tail.prev
        prev_to_drop = drop.prev
        prev_to_drop.post = self.tail
        self.tail.prev = prev_to_drop
        drop.prev = drop.post = None
        del self.hashmap[drop.key]

if __name__ == "__main__":
    # test cases
    cache = LRUCache(capacity=3)
    nums = [ (1,2), (3,4), (2,6), (1,4), (4,9), (2,5), (7,0), (7,2) ]
    for key, value in nums:
        cache.put(key, value)
        
