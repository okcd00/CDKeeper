class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        rec = {}
        for idx in xrange(len(nums)):
            rest = target - nums[idx]
            if rest in rec:
                return [rec[rest], idx]
            rec[nums[idx]] = idx
        return None