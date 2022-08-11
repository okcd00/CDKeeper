def partition(nums, l, r):
    pivot = nums[l] + 0
    while l < r:
        while l < r and nums[r] >= pivot:
            r -= 1
        nums[l] = nums[r]
        while l < r and nums[l] <= pivot:
            l += 1
        nums[r] = nums[l]
    nums[l] = pivot
    return l


def kth_smallest(nums, l, r, k):
    pivot = partition(nums, l, r)
    if pivot < k:
        return kth_smallest(nums, pivot+1, r, k)
    elif pivot > k:
        return kth_smallest(nums, l, pivot-1, k)
    else:
        return nums[pivot]


if __name__ == "__main__":
    # AIDU - 1st interview
    arr = [5123,6162,671734,3115,3]
    print(kth_smallest(arr, 0, len(arr)-1, 3))
    print(arr)
