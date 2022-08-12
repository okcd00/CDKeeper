"""

给定一个长度为 n 的数组 nums 和滑动窗口的大小 size ，找出所有滑动窗口里数值的最大值。
输入：
[1,2,3,4], 3
返回值：
[3,4]
"""


import collections

class Solution:
    def maxSlidingWindow(self, nums, k):
        if not nums or k == 0: 
            return []
        deque = collections.deque()

        # 未形成窗口
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]

        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res     
    

if __name__ == "__main__":
    nums = [5,4,3,2,3,4,5]
    size = 3
    sol = Solution()
    print(sol.maxSlidingWindow(nums=nums, k=size))
    # 5,4,3,4,5
