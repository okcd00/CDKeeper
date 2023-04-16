class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ret = 0
        count = sum(mat[0])
        for i in range(1, len(mat)):
            _count = sum(mat[i])
            if _count > count:
                ret = i
                count = _count
        return [ret, count]
        