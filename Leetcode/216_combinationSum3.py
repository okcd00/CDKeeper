class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        candidates = list(itertools.combinations(range(1, 10),k))
        return [ans for ans in candidates if sum(ans)==n]