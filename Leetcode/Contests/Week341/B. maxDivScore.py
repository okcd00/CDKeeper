class Solution:
    def maxDivScore(self, nums, divisors) -> int:
        ret = divisors[0]
        count = 0
        for d in divisors:
            # print([v % d == 0 for v in nums])
            _count = sum([v % d == 0 for v in nums])
            if _count > count:
                ret = d
                count = _count
            elif _count == count and d < ret:
                ret = d
                count = _count
            # print(d, ret, _count, count)
        return ret
    

s = Solution()
print(s.maxDivScore([73,13,20,6], [56,75,26,24,61]))