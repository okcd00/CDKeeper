class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n_row = obstacleGrid.__len__()
        n_col = obstacleGrid[0].__len__()
        last_row = [0] * n_col
        for r in range(n_row):
            last_col = 0
            for c in range(n_col):
                if obstacleGrid[r][c]:
                    last_row[c] = 0
                    last_col = 0
                    continue
                if c == 0 and r == 0:
                    last_row[c] = 1
                    last_col = 1
                    continue
                # left one
                if obstacleGrid[r][c-1]:
                    lef = 0 
                else:
                    lef = last_col
                # up one
                if obstacleGrid[r-1][c]: 
                    up = 0
                else: 
                    up = last_row[c]
                # current
                last_row[c] = up + lef
                last_col = last_row[c]
        return last_row[-1]