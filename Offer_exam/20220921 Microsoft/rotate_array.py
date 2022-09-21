def rotate_array(nums, k):
    # nums = list(map(int, input().strip().split()))
    n = len(nums)
    k = k % n

    if n % k != 0:
        pivot = k
        tmp = nums[k]  # 0 + k
        for _ in range(n-1):
            pre_index = (pivot - k + n) % n
            nums[pivot] = nums[pre_index]
            pivot = pre_index
        nums[pivot] = tmp
    else:
        for start_position in range(k):
            pivot = start_position + k
            tmp = nums[pivot]
            for _ in range(n-1):
                pre_index = (pivot - k + n) % n
                nums[pivot] = nums[pre_index]
                pivot = pre_index
            nums[pivot] = tmp
    return nums        


if __name__ == "__main__":
    print(rotate_array([1,2,3,4,5,6,7], k=3))
