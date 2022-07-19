"""
https://leetcode.cn/problems/spiral-matrix/

给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        u, d = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        while True:
            ret.extend(matrix[u][l:r+1])
            u += 1
            if u > d: break
            ret.extend([matrix[k][r] for k in range(u, d+1)])
            r -= 1
            if r < l: break
            ret.extend(matrix[d][l:r+1][::-1])
            d -= 1
            if d < u: break
            ret.extend([matrix[k][l] for k in range(u, d+1)][::-1])
            l += 1
            if l > r: break
        return ret