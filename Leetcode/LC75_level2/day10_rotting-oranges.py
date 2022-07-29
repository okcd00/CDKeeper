"""
https://leetcode.cn/problems/rotting-oranges/

在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。
"""


from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        offset = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n_row = len(grid)
        n_col = len(grid[0])
        # vis = [[0 for _ in range(n_col)] for _ in range(n_row)]
        
        def is_valid(_r, _c):
            if _r < 0 or _r >= n_row:
                return False
            if _c < 0 or _c >= n_col:
                return False
            if grid[_r][_c] != 1:
                return False
            return True

        def bfs(src_case):
            q = deque(src_case)
            n_ticks = 0
            n_rotten = len(src_case)
            while q:
                flag = False
                n_items = len(q)
                for _ in range(n_items):
                    (_r, _c) = q.popleft()
                    for off_r, off_c in offset:
                        if is_valid(_r + off_r, _c + off_c):
                            q.append((_r + off_r, _c + off_c))
                            # print((_r + off_r, _c + off_c))
                            grid[_r + off_r][_c + off_c] = 2
                            flag = True
                            n_rotten += 1
                if flag:
                    n_ticks += 1
                # print(q, n_ticks)
            return n_ticks, n_rotten
        
        n_oranges = 0
        rotten_oranges = []
        for row_id, row in enumerate(grid):
            for col_id, cell in enumerate(row):
                if cell > 0:
                    n_oranges += 1
                if cell == 2:
                    rotten_oranges.append((row_id, col_id))
        n_ticks, n_rotten = bfs(rotten_oranges)
        # print(n_rotten, n_oranges, n_ticks)
        return n_ticks if n_rotten == n_oranges else -1
