class Solution:
    def countAlternatingSubarrays(self, nums) -> int:
        ans = len(nums)
        l, r = 0, 1
        while l < len(nums) and r < len(nums):
            while r < len(nums) and nums[r] != nums[r-1]:
                r += 1
            ans += (1 + (r-1-l)) * (r-1-l) // 2
            # print(l, r, ans)
            l, r = r, r + 1
        return ans


if __name__ == '__main__':
    s = Solution()
    # inp = [0,1,1,1]
    # inp = [1,0,1,0]
    inp = [1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1]
    ret = s.countAlternatingSubarrays(inp)
    print(ret)