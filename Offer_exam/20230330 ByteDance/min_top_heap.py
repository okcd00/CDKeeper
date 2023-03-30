# stream of ints

class MTHeap(object):
    def __init__(self, k):
        inf = -999
        self.k = k
        self.mt_heap = [inf for _ in range(k)]

    def insert(self, v):
        # change the top node as v, then adjust the heap.
        pivot = 0
        h = self.mt_heap
        h[pivot] = v
        while pivot < k:
            lef_pivot = pivot * 2 + 1
            rig_pivot = pivot * 2 + 2
            if lef_pivot >= k:
                 break
            if lef_pivot == k-1:  # has left, but has no right
                min_pivot = lef_pivot
            else:                
                min_pivot = lef_pivot if h[lef_pivot] < h[rig_pivot] else rig_pivot
            if h[pivot] > h[min_pivot]:
                h[min_pivot], h[pivot] = h[pivot], h[min_pivot]
                pivot = min_pivot
            else:
                break

    def __call__(self, iterator):    
        for v in iterator:
            if len(self.mt_heap) <= self.k:
                self.insert(v)
                continue
            else:
                if v > self.mt_heap[0]:
                    self.insert(v)


if __name__ == "__main__":
    k = 7
    it = iter([2,3,5,1,1,6,26,6,17,7,34,51,56])
    mt = MTHeap(k)
    mt(it)
    print(mt.mt_heap)

