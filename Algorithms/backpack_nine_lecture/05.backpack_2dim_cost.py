"""
https://www.acwing.com/problem/content/8/
有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。

每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi。

求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量不超过背包可承受的最大重量，且价值总和最大。
输出最大价值。

输入格式
第一行三个整数，N,V,M，用空格隔开，分别表示物品件数、背包容积和背包可承受的最大重量。
接下来有 N 行，每行三个整数 vi,mi,wi，用空格隔开，分别表示第 i 件物品的体积、重量和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0 < N ≤ 1000
0 < V, M ≤ 100
0 < vi, mi ≤ 100
0 < wi ≤ 1000
"""


def backpack_2dim(n, V, M, v, m, w):
    """
    n: 物品个数
    V: maximum volumn 背包最大容积
    M: maximum mess 背包最大质量
    v: volumn 体积
    m: mess 质量
    w: worth 价值
    """
    f = [[0 for _ in range(M+1)] for _ in range(V+1)]  # f[i] 为体积小于等于 i 的最大价值
    # f = [0] + [-inf for _ in range(m)]  # f[i] 为体积等于 i 的最大价值

    v, m, w = [0] + v, [0] + m, [0] + w  # 第1个物品: v[1] and w[1]

    for i in range(1, n+1):
        for j in range(V, v[i]-1, -1):  # 反着来是为了让每个物品只能用一次
            for k in range(M, m[i]-1, -1):  # 反着来是为了让每个物品只能用一次
                f[j][k] = max(f[j][k], f[j - v[i]][k - m[i]] + w[i])

    print(f[V][M])


if __name__ == "__main__":
    n, V, M = list(map(int, input().strip().split()))
    v, w, m = [], [], []
    for _ in range(n):
        _v, _w, _m = list(map(int, input().strip().split()))
        v.append(_v)
        w.append(_w)
        m.append(_m)
    # backpack_multi(4, 5, [1,2,3,4], [2,4,4,5], [3,-1,0,2])    
    backpack_2dim(n, V, M, v, w, m)
