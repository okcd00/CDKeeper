class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowCosts: List[int], colCosts: List[int]) -> int:
        ret = 0
        r_step = 1 if startPos[0] > homePos[0] else -1
        for r_offset in range(homePos[0], startPos[0], r_step):
            ret += rowCosts[r_offset]
        c_step = 1 if startPos[1] > homePos[1] else -1
        for c_offset in range(homePos[1], startPos[1], c_step):
            ret += colCosts[c_offset]
        return ret
        
        
if __name__ == "__main__":
    s = Solution()
    s.minCost()