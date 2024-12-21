import math
from functools import cache


class Solution:
    def countPathsWithXorValue(self, grid, k: int) -> int:
        m, n = len(grid), len(grid[0])
        v_mod = int(1e9) + 7

        max_xor = 16  # 最大异或值为 16
        dp = [[[0] * (max_xor + 1) for _ in range(n)] for _ in range(m)]
        dp[0][0][grid[0][0]] = 1
        
        for i in range(m):
            for j in range(n):
                for x in range(max_xor + 1):
                    if dp[i][j][x] > 0:
                        if i + 1 < m:  # 向下走
                            dp[i + 1][j][x ^ grid[i + 1][j]] = (dp[i + 1][j][x ^ grid[i + 1][j]] + dp[i][j][x]) % v_mod
                        if j + 1 < n:  # 向右走
                            dp[i][j + 1][x ^ grid[i][j + 1]] = (dp[i][j + 1][x ^ grid[i][j + 1]] + dp[i][j][x]) % v_mod
                
        return dp[m-1][n-1][k]


if __name__ == '__main__':
    s = Solution()
    grid = [[2,1,5], [7,10,0], [12,6,4]]
    k = 11
    ret = s.countPathsWithXorValue(grid,k)
    print(ret)