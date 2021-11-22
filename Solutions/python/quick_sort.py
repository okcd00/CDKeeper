def quick_sort_simple(data):
    # sort the list
    if len(data) >= 2:
        pivot = data[0]  # any number is fine 
        left, right = [], []
        for num in data[1:]:
            if num >= pivot:
                right.append(num)
            else:
                left.append(num)
        return quick_sort(left) + [pivot] + quick_sort(right)
    else:
        return data


def quick_find_simple(data, k):
    # find the k-th smallest number
    if len(data) >= 2:
        # any number is fine
        mid = data[0]
        left, right = [], []
        for num in data[1:]:
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
        return data[0]


def quick_sort(data_list, l=None, r=None):
    # from Weimin Yan's "Data Structure"
    if l is None and r is None:
        l, r = 0, len(data_list) - 1

    def paritition(data, low, high):
        pivot = data[low] + 0
        while low < high:
            while low < high and data[high] >= pivot:
                high -= 1
            # set data[low] as the right-most num < data[pivot]
            # print(f"data[{low}]: {data[low]} -> {data[high]}")
            data[low] = data[high]  
            while low < high and data[low] <= pivot:
                low += 1
            # set data[high] as the left-most num > pivot
            # print(f"data[{high}]: {data[high]} -> {data[low]}")
            data[high] = data[low]  
        # print(f"data[{low}]: {data[low]} -> {pivot}")
        data[low] = pivot          
        return low

    if l < r:
        p = paritition(data_list, l, r)
        quick_sort(data_list, l, p-1)
        quick_sort(data_list, p+1, r)
    
    return data_list


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


if __name__ == "__main__":
    dat = [2,3,4,51,1,1,53,26,3,4,16]
    print(quick_sort(dat))
    print(quick_find_simple(dat, k=3))
