"""
https://docs.qq.com/doc/DWkZ6SmJVTHJNeXFm

有 k 个 POD：
每个里面有 k/2 个一级交换机， k/2 个二级交换机，每个一级交换机连接 k/2 个节点
有 k/2 个 SET：
每个里面有 k/2 个三级交换机，每个连接着每个 POD 中对应位置（取模同下标）的二级交换机
问：
N次查询，需要列举出给定编号的节点间的所有通路（仅允许1次上行 + 1次下行）
通过 25%，很奇怪，不理解为啥只通过这么点

"""


if __name__ == "__main__":
    pass