# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2024 All rights reserved.
#
#   filename : graph_algorithm.py
#   author   : chendian / okcd00@qq.com
#   date     : 2024/12/21 22:13:31
#   desc     : 
#              
# ==========================================================================
import heapq


class TARJAN:
    """
    Tarjan 割点&桥 算法

    # x 是割点
    # 割点 Case 1: 非root && 有儿子 && low[x的child] >= dfn[x]
    # 割点 Case 2: root && 有不少于2个儿子

    # x->y 是桥
    # low[y] > dfn[x]
    """
    def __init__(self, n: int, g):
        # 记录结点的当前时间戳和最早时间戳
        # 从根开始的一条路径上 dfn 严格递增，low 严格非降
        self.dfn = [-1] * n
        self.low = [-1] * n
        self.bridge = []  # 桥
        self.flag = [False] * n  # 是否是割点
        self.g = g

    def tarjan(self, o: int, f: int, t: int) -> None:
        self.dfn[o] = t
        self.low[o] = t
        c = 0
        for child in self.g[o]:
            if child != f:
                if self.dfn[child] == -1:
                    c += 1
                    self.tarjan(child, o, t + 1)
                    self.low[o] = min(self.low[o], self.low[child])

                    # Case 1: 找到割点, 非root, 有儿子
                    if self.dfn[o] <= self.low[child] and f != -1 and not self.flag[o]:
                        self.flag[o] = True

                    # 找到桥
                    if self.dfn[o] < self.low[child]:
                        self.bridge.append([o, child])
                else:
                    self.low[o] = min(self.low[o], self.dfn[child])
                    
        # Case 2: root点 儿子数大于等于2
        if f == -1 and c >= 2 and not self.flag[o]:
            self.flag[o] = True


def dijkstra(graph, start):
    """
    使用 Dijkstra 算法计算从起点到图中所有节点的最短路径

    :param graph: 字典表示的加权图 {节点: [(邻接节点, 权重)]}
    :param start: 起点
    :return: 字典，表示每个节点的最短路径长度 {节点: 最短距离}
    """
    # 初始化距离字典，起点到自己的距离为 0，其他为无穷大
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    # 使用优先队列存储节点和当前最短距离
    priority_queue = [(0, start)]  # (距离, 节点)

    while priority_queue:
        # print(distance)
        current_distance, current_node = heapq.heappop(priority_queue)

        # 如果当前距离比已知最短距离长，跳过
        if current_distance > distances[current_node]:
            continue

        # 更新邻居节点的距离
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # 如果找到更短的路径，更新并加入队列
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances