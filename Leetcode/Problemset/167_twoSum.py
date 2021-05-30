class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        rec = {}
        for idx in xrange(len(numbers)):
            rest = target - numbers[idx]
            if rest in rec:
                return [rec[rest]+1, idx+1]
            rec[numbers[idx]] = idx
        return None