"""
https://www.acwing.com/problem/content/2/

有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。
第 i 件物品的体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。
接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

输出格式
输出一个整数，表示最大价值。
"""

from cmath import inf


def backpack_01(n, m, v, w):
    """
    n: 物品个数
    m: maximum volumn 背包最大容积
    v: volumn 体积
    w: worth 价值
    """
    f = [0 for _ in range(m+1)]  # f[i] 为体积小于等于 i 的最大价值
    # f = [0] + [-inf for _ in range(m)]  # f[i] 为体积等于 i 的最大价值

    v, w = [0] + v, [0] + w  # 第1个物品: v[1] and w[1]

    for i in range(1, n+1):
        for j in range(m, v[i]-1, -1):
            f[j] = max(f[j], f[j - v[i]] + w[i])

    print(f[m])
            

if __name__ == "__main__":
    backpack_01(4, 5, [1,2,3,4], [2,4,4,5])    
