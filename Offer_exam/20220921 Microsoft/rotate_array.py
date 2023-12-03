class Solution:
    def _gcd(self, a, b):
        if a == b:
            return a
        if a > b:
            a, b = b, a
        return self._gcd(a, b-a)

    def rotate(self, nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums = list(map(int, input().strip().split()))
        n = len(nums)
        k = k % n
        if k == 0:
            return nums
        for start_position in range(self._gcd(n, k)):
            pivot = start_position
            tmp = nums[start_position]
            for _ in range(n//self._gcd(n, k)-1):
                pre_index = (pivot - k + n) % n
                nums[pivot] = nums[pre_index]
                pivot = pre_index
            nums[pivot] = tmp
        return nums



if __name__ == "__main__":
    s = Solution()
    print(s.rotate_array([1,2,3,4,5,6,7], k=3))
