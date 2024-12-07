from collections import Counter

class Solution:
    def minOperations(self, nums, k: int) -> int:
        v_min = min(nums)
        if v_min < k:
            return -1
        hash = Counter(nums)
        if v_min == k:
            return len(hash.keys()) - 1
        else:
            return len(hash.keys())
        

if __name__ == '__main__':
    inp = [2,3,5,10]
    s = Solution()
    ret = s.getLargestOutlier(inp)
    print(ret)