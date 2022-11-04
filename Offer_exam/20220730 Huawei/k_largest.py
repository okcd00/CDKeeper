class KthLargestSolution:

    def partition(self, nums, l, r):
        # return: the index of pivot value after partition
        pivot = nums[l] + 0  # value
        while l < r:
            # print(l, r)
            while l < r and nums[r] >= pivot:
                r -= 1
            nums[l] = nums[r]
            while l < r and nums[l] <= pivot:
                l += 1
            nums[r] = nums[l]
        nums[l] = pivot
        return l  # index

    def quick_select(self, nums, l, r, k):
        """
        return: the index of k-th largest value
        """
        pivot = self.partition(nums, l, r)  # index
        if pivot < k:  # [l, pivot, k, r]
            return self.quick_select(nums, pivot+1, r, k)
        elif pivot > k:  # [l, k, pivot, r]
            return self.quick_select(nums, l, pivot-1, k)
        return nums[pivot]  # value
 
    def kth_largest(self, nums, k):
        return self.quick_select(nums, 0, len(nums)-1, len(nums)-k)

    def kth_largest_heap(self, nums, k):
        from heapq import heappush, heappop
        if len(nums) < k:
            raise ValueError(f"Invalid k for the {len(nums)}-size array.")
        h = []
        for v in nums:
            heappush(h, v)
            if len(h) > k:
                heappop(h)
        return h[0]


if __name__ == "__main__":
    pass
