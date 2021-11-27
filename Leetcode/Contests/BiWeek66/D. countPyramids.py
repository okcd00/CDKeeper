class Solution:
    def countPyramids(self, grid: List[List[int]]) -> int:
        ret = 0
        level = 1
        
        # upper-left
        ul = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r in range(1, len(grid)):
            for c in range(1, len(grid[0])-1):
                if grid[r][c] != 1:
                    continue
                if grid[r-1][c] == grid[r][c-1]:
                    if grid[r][c-1] == 0:
                        continue
                    ul[r][c] = min(ul[r-1][c], ul[r][c-1]) + 1
                    # if ul[r-1][c] == ul[r][c-1]:
                    #     ul[r][c] = ul[r][c-1] + 1
        print(ul)
        
        # upper-right
        ur = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r in range(1, len(grid)):
            for c in range(len(grid[0])-2, 0, -1):
                if grid[r][c] != 1:
                    continue
                if grid[r-1][c] == grid[r][c+1]:
                    if grid[r][c+1] == 0:
                        continue
                    ur[r][c] = min(ur[r-1][c], ur[r][c+1]) + 1
        print(ur)
        
        # lower-left
        ll = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r in range(len(grid)-2, -1, -1):
            for c in range(1, len(grid[0])-1):
                if grid[r][c] != 1:
                    continue
                if grid[r+1][c] == grid[r][c-1]:
                    if grid[r][c-1] == 0:
                        continue
                    ll[r][c] = min(ll[r+1][c], ll[r][c-1]) + 1
        print(ll)
        
        # lower-right
        lr = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for r in range(len(grid)-2, -1, -1):
            for c in range(len(grid[0])-2, 0, -1):
                if grid[r][c] != 1:
                    continue
                if grid[r+1][c] == grid[r][c+1]:
                    if grid[r][c+1] == 0:
                        continue
                    lr[r][c] = min(lr[r+1][c], lr[r][c+1]) + 1
        print(lr)
        
        # total
        for r in range(len(grid)):
            for c in range(1, len(grid[0])-1):
                ret += min(ul[r][c], ur[r][c]) 
                ret += min(ll[r][c], lr[r][c]) 
                # print(r, c, min(ul[r][c], ur[r][c]), min(ll[r][c], lr[r][c]))
        return ret
        
        