from collections import deque

class Solution:

    def __init__(self):
        self.cost_on_vertices = None
        
    def max_score(self, vertices, edges, scores):
        # 二分图，在相邻点不能同时选择的情况下，输出总价值最大的子点集
        # 该点集即为需要被减半的点集
        ans, collections = 0, []
        return ans, collections
    
    def travel(self, vertices, edges, trips):
        # 记录 trips 全过程需要经过每个节点多少次
        # 为每个节点记录总路径的花费总和
        pass

    def minimumTotalPrice(self, n: int, edges, price, trips) -> int:
        vertices = [i for i in range(n)]
        costs_on_vertices = [1 for _ in range(n)]
        self.cost_on_vertices = [0 for _ in range(n)]
        self.travel(vertices, edges, trips)
        cost, collections = self.max_score(vertices, edges, self.cost_on_vertices)
        return sum(self.cost_on_vertices) - (cost / 2)