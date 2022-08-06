#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 通过k-means聚类算法实现对员工居住位置的聚类，返回输入的所有员工坐标位置对应的聚类类别序号（请仔细阅读补充描述中的输入与输出定义）
# @param positions float浮点型二维数组 员工居住地点坐标集合，((x_0,y_0),(x_1,y_1),(x_2,y_2),...,(x_{n-1},y_{n-1}))
# @param k int整型 类别数目
# @return int整型一维数组
#

from collections import defaultdict


class Solution:
    def get_center(self, positions):
        mean_x = sum([x for x, _ in positions]) / len(positions)
        mean_y = sum([y for _, y in positions]) / len(positions)
        return (mean_x, mean_y)

    def get_distance(self, node_a, node_b):
        dist = (node_a[0] - node_b[0])**2 + (node_a[1] - node_b[1])**2
        return dist

    def classify(self, node, centers):
        belong = 0
        min_dist = self.get_distance(node, centers[0])
        for _i in range(1, len(centers)):
            dist = self.get_distance(node, centers[_i])
            if dist < min_dist:
                belong = _i
                min_dist = dist
        return belong

    def k_means(self, positions, k):
        centers = positions[:k]

        for round in range(100):
            belongs = [self.classify(node, centers) for node in positions]
            for center_idx in range(k):
                centers[center_idx] = self.get_center([node for i, node in enumerate(positions) if belongs[i] == center_idx])
        return belongs


if __name__ == "__main__":
    positions = [[1.5,2.1], [0.8,2.1], [1.3,2.1], [110.5,260.6], [21.7, 32.8],[130.9,150.8],[32.6,40.7],[41.5,24.7]]
    k = 3

    sol = Solution()
    ret = sol.k_means(positions=positions, k=k)
    print(ret)
