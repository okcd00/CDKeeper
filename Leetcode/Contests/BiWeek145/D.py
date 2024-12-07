from math import gcd
from collections import defaultdict


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


class Solution:
    def countComponents(self, nums, threshold: int) -> int:
        nums = sorted(nums)
        large_num = len([v for v in nums if v > threshold])
        if large_num > 0:
            nums = nums[:-large_num]
        n_parents = self.count_connected_components(nums, threshold)
        # print(large_num, n_parents)
        return large_num + n_parents
    
    def lcm(self, a, b):
        return abs(a * b) // gcd(a, b)

    def sieve_upto(self, k):
        is_multiple = [set() for _ in range(k)]
        for i in range(1, k):
            for j in range(i, k, i):
                is_multiple[j].add(i)
        return is_multiple

    def count_connected_components(self, l, k):
        n = len(l)
        value_to_index = {val: idx for idx, val in enumerate(l)}
        uf = UnionFind(n)
        
        multiples = [list() for _ in range(k+1)]
        for v in l:
            for j in range(v, k+1, v):
                multiples[j].append(v)
        
        for m in range(1, k + 1):
            if len(multiples[m]) >= 2:
                head = value_to_index[multiples[m][0]]
                for a in multiples[m][1:]:
                    uf.union(head, value_to_index[a])
        
        # 统计连通块数量
        return uf.count_components()

    def count_connected_components_tle(self, l, k):
        n = len(l)
        uf = UnionFind(n)
        for i in range(n):
            for j in range(i + 1, n):
                if self.lcm(l[i], l[j]) <= k:
                    uf.union(i, j)

        return uf.count_components()

    def count_connected_components_mle(self, l, k):
        n = len(l)
        graph = defaultdict(list)
        
        for i in range(n):
            for j in range(i + 1, n):
                if self.lcm(l[i], l[j]) <= k:
                    graph[l[i]].append(l[j])
                    graph[l[j]].append(l[i])
        
        visited = set()
        def dfs(node):
            stack = [node]
            while stack:
                current = stack.pop()
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)
        
        connected_components = 0
        for num in l:
            if num not in visited:
                visited.add(num)
                dfs(num)
                connected_components += 1
        
        return connected_components


# 示例测试
l =[2,5,6,8]
k = 6
print(Solution().countComponents(l, k))  # 输出连通块的数量
