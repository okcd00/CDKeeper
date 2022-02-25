def quick_sort_simple(nums):
    # sort the list
    if len(nums) >= 2:
        pivot = nums[0]  # any number is fine 
        left, right = [], []
        for num in nums[1:]:
            if num >= pivot:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [pivot] + quick_sort(right)
    else:
        return nums


def quick_find_simple(nums, k):
    # find the k-th smallest number
    if len(nums) >= 2:
        # any number is fine
        mid = nums[0]
        left, right = [], []
        for num in nums[1:]:
            if num >= mid:
                right.append(num)
            else:
                left.append(num)
        if len(left) == k - 1:
            return mid
        elif len(left) < k - 1:
            return quick_find_simple(right, k=k-len(left)-1)
        else:  # len(left) > k - 1
            return quick_find_simple(left, k=k)
    else:
        return nums[0]
        

class QuickSort:
    def __init__(self):
        self.partition = self.partition_oneway

    def find_kth_largest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums)-1, len(nums)-k)

    def find_kth_smallest(self, nums: List[int], k: int) -> int:
        return self.quick_select(nums, 0, len(nums)-1, k-1)

    def quick_select(self, nums, l, r, index):
        pivot = self.partition(nums, l, r)

        if pivot < index:
            return self.quick_select(nums, pivot+1, r, index)
        elif pivot > index:
            return self.quick_select(nums, l, pivot-1, index)
        else:
            return nums[pivot]

    def quick_sort(self, nums, l, r):
        # self.quick_sort(nums, 0, len(nums)-1)
        if l < r: 
            pivot = self.partition(nums, l, r) 
            self.quick_sort(nums, l, pivot-1) 
            self.quick_sort(nums, pivot+1, r) 

    def partition_oneway(self, nums, l, r):
        # print(nums)
        pivot, v = l, nums[r]  # l can be randomly selected
        for idx in range(l, r):
            if nums[idx] <= v:
                nums[pivot], nums[idx] = nums[idx], nums[pivot]
                pivot += 1
                # print("->", nums)
        nums[pivot], nums[r] = nums[r], nums[pivot]
        return pivot

    def paritition_twoway(self, nums, low, high):
        # from Weimin Yan's "nums Structure"
        pivot = nums[low] + 0
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            # set nums[low] as the right-most num < nums[pivot]
            # print(f"nums[{low}]: {nums[low]} -> {nums[high]}")
            nums[low] = nums[high]  
            while low < high and nums[low] <= pivot:
                low += 1
            # set nums[high] as the left-most num > pivot
            # print(f"nums[{high}]: {nums[high]} -> {nums[low]}")
            nums[high] = nums[low]  
        # print(f"nums[{low}]: {nums[low]} -> {pivot}")
        nums[low] = pivot          
        return low


if __name__ == "__main__":
    dat = [2,3,4,51,1,1,53,26,3,4,16]
    print(quick_sort(dat))
    print(quick_find_simple(dat, k=3))
