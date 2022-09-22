/*
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
*/

#include <bits/stdc++.h>
using namespace std;

int n, V, M;
const int N = 1e3 + 5;
int v[N], m[N], w[N], f[N][N];

signed main () {
    cin >> n >> V >> M;
    for (int i = 1; i <= n; i ++) {
        cin >> v[i] >> m[i] >> w[i];//体积，重量，价值
    }
    for (int i = 1; i <= n; i ++)
        for (int j = V; j >= v[i]; j --)
            for (int k = M; k >= m[i]; k --)
                f[j][k] = max (f[j - v[i]][k - m[i]] + w[i], f[j][k]);//动态转移方程，01 背包的思路
    cout << f[V][M];
} 