"""
https://www.acwing.com/problem/content/4/

有 N 种物品和一个容量是 V 的背包。
第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。
求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0 < N,V ≤ 100
0 < vi,wi,si ≤ 100
"""


def flatten(_list):
    """
    将列表中的列表拍平
    """
    return [item for sublist in _list for item in sublist]


def backpack_multi(n, m, v, w, s):
    """
    n: 物品个数
    m: maximum volumn 背包最大容积
    v: volumn 体积
    w: worth 价值
    s: 某种物品最多可以选几个
    """
    f = [0 for _ in range(m+1)]  # f[i] 为体积小于等于 i 的最大价值
    # f = [0] + [-inf for _ in range(m)]  # f[i] 为体积等于 i 的最大价值，结果需要遍历 f 找最大值
    
    nn, vv, ww = 0, [0], [0]  # 第1个物品: vv[1] and ww[1]
    for _v, _w, _s in zip(v, w, s):
        k = 1
        while k <= _s:
            vv.append(_v * k)
            ww.append(_w * k)
            _s -= k
            nn += 1
            k <<= 1
        if _s > 0:
            vv.append(_v * _s)
            ww.append(_w * _s)
            nn += 1
    n, v, w = nn, vv, ww

    for i in range(1, n+1):
        for j in range(m, v[i]-1, -1):  # 反着来是为了让每个物品只能用一次
            f[j] = max(f[j - v[i]] + w[i], f[j])

    print(f[m])


def backpack_multi_naive(n, m, v, w, s):
    """
    n: 物品个数
    m: maximum volumn 背包最大容积
    v: volumn 体积
    w: worth 价值
    s: 某种物品最多可以选几个
    """
    f = [0 for _ in range(m+1)]  # f[i] 为体积小于等于 i 的最大价值
    # f = [0] + [-inf for _ in range(m)]  # f[i] 为体积等于 i 的最大价值，结果需要遍历 f 找最大值

    v, w, s = [0] + v, [0] + w, [0] + s  # 第1个物品: v[1] and w[1]

    for i in range(1, n+1):
        for j in range(m, v[i]-1, -1):  # 反着来是为了让每个物品只能用一次
            f[j] = max([f[j - k * v[i]] + k * w[i] 
                        for k in range(s[i] + 1)
                        if k * v[i] <= j])

    print(f[m])
            

if __name__ == "__main__":
    n, m = list(map(int, input().strip().split()))
    v, w, s = [], [], []
    for _ in range(n):
        _v, _w, _s = list(map(int, input().strip().split()))
        v.append(_v)
        w.append(_w)
        s.append(_s)
    # backpack_multi(4, 5, [1,2,3,4], [2,4,4,5], [3,1,3,2])    
    backpack_multi(n, m, v, w, s)    
