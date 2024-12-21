class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        ans = 0
        for i in range(len(nums) - 2):
            if 2 * (nums[i] + nums[i+2]) == nums[i+1]:
                ans += 1
                # print(nums[i:i+3])
        return ans
