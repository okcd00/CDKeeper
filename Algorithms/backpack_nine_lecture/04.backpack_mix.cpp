/*
https://www.acwing.com/problem/content/7/
有 N 种物品和一个容量是 V 的背包。

物品一共有三类：

第一类物品只能用1次（01背包）；
第二类物品可以用无限次（完全背包）；
第三类物品最多只能用 si 次（多重背包）；
每种体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。
接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

si=−1 表示第 i 种物品只能用 1 次；
si=0 表示第 i 种物品可以用无限次；
si>0 表示第 i 种物品可以使用 si 次；

输出格式
输出一个整数，表示最大价值。

数据范围
0 < N,V ≤ 1000
0 < vi,wi ≤ 1000
−1 ≤ si ≤ 1000
*/

#include <iostream>
using namespace std;

int n, v, tc, tw, s, cnt = 1;
int c[11000], w[11000], dp[50000];

int main()
{
    scanf("%d%d", &n, &v);
    for (int i = 1; i <= n; i++)
    {
        scanf("%d%d%d", &tc, &tw, &s);
        if (s == 0)
            s = v / tc; // 完全背包
        if (s == -1)
            s = 1; // 01背包

        // 二进制优化
        int k = 1;
        while (k <= s)
        {
            cnt++;
            c[cnt] = k * tc;
            w[cnt] = k * tw;
            s -= k;
            k *= 2;
        }
        if (s > 0)
        {
            cnt++;
            c[cnt] = s * tc;
            w[cnt] = s * tw;
        }
    }

    // 将01背包 完全背包 多重背包全部打包成cnt件
    n = cnt; // 接下来就是普通的 01 背包
    for (int i = 1; i <= n; i++)
    {
        for (int j = v; j >= c[i]; j--)
        {
            dp[j] = max(dp[j], dp[j - c[i]] + w[i]);
        }
    }
    printf("%d", dp[v]);
}
