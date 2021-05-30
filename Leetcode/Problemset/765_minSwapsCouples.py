class Solution:
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        res = 0
        for i in range(0, len(row), 2):
            p = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
            j = row.index(p)
            if j-i > 1:
                row[i+1], row[j] = row[j], row[i+1]
                res += 1
        return res