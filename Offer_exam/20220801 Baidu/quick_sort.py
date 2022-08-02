def partition(nums, l, r):
    # this pivot is a value
    # print(l, r)
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

def quick_sort(nums, l, r):
    if r - l < 1:
        return 
    # this pivot is an index
    pivot = partition(nums, l, r)
    quick_sort(nums, l, pivot-1)
    quick_sort(nums, pivot+1, r)    


nums = [234,15,6116,12465,7174]
quick_sort(nums, 0, len(nums)-1)
print(nums)