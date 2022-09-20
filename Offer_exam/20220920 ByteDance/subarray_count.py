"""
https://leetcode.cn/problems/number-of-subarrays-with-bounded-maximum/ 

题目描述
输入: L, R, Array

输出：​
* 连续子数组的个数​
* 连续子数组满足条件：里面的数字的最大值介于 L 和 R 之间​

[2, 3, 5]
L = 3
R = 3
输出 2
"""

class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):

        def numSubarrayAtMost(bound):
            ans, cur = [], 0
            for x in A:
                cur = cur + 1 if x <= bound else 0
                ans.append(cur)
            # print(ans)
            return sum(ans)

        return numSubarrayAtMost(R) - numSubarrayAtMost(L - 1)


if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubarrayBoundedMax(
        [2,3,5,2,3,3,5,1,3], 2, 3))
