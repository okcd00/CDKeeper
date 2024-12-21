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