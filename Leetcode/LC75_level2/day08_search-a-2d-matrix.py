"""
https://leetcode.cn/problems/search-a-2d-matrix/submissions/

编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
"""


from bisect import bisect_right


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = bisect_right([r[0] for r in matrix], target)
        col = bisect_right(matrix[row-1], target)
        # print(row, col)
        return matrix[row-1][col-1] == target
    
    def searchMatrix_v2(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        x,y = 0, n - 1
        while x < m and y >= 0:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False