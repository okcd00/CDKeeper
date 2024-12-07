# coding: utf-8
# ==========================================================================
#   Copyright (C) since 2024 All rights reserved.
#
#   filename : ufs.py
#   author   : chendian / okcd00@qq.com
#   date     : 2024/12/08 00:18:01
#   desc     : 
#              
# ==========================================================================

import os, sys, time


class UnionFind:
    def __init__(self, n):
        """初始化并查集，n 是节点的数量"""
        self.parent = list(range(n))  # 每个节点的父节点
        self.rank = [0] * n           # 每个节点的秩，用于优化合并
    
    def find(self, x):
        """查找节点 x 的根，并进行路径压缩"""
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # 路径压缩
        return self.parent[x]
    
    def union(self, x, y):
        """将两个节点 x 和 y 所在的集合合并"""
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x != root_y:
            # 按秩合并：将秩低的集合合并到秩高的集合中
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1

    def connected(self, x, y):
        """判断两个节点 x 和 y 是否在同一个集合中"""
        return self.find(x) == self.find(y)
    
    def count_components(self):
        """计算连通块的数量"""
        return sum(1 for i in range(len(self.parent)) if self.parent[i] == i)

