/*
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
朴素：https://www.acwing.com/problem/content/4/
0 < N,V ≤ 100
0 < vi,wi,si ≤ 100

二进制：https://www.acwing.com/problem/content/5/
0 < N ≤ 1000
0 < V ≤ 2000
0 < vi,wi,si ≤ 2000

单调栈：https://www.acwing.com/problem/content/6/
0 < N ≤ 1000
0 < V ≤ 20000
0 < vi,wi,si ≤ 20000
*/

#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 2022;

int n, m;
int v[N], w[N], s[N]; // v[i] = 体积, w[i] = 价值, s[i] = 数量

int main()
{
    // 二进制优化方法 https://www.acwing.com/problem/content/5/
    cin >> n >> m;
    vector<int> vv, ww; // 体积, 价值
    vv.push_back(0);
    ww.push_back(0);
    int f[N];                // f[i][j] = 从前i件物品中选择，体积等于j时物品的最大价值
    memset(f, 0, sizeof(f)); // 所有体积小于等于 f[i] 的最大价值是多少

    int nn = 0;
    int _v, _w, _s;
    for (int i = 1; i <= n; i++)
    {
        cin >> _v >> _w >> _s;
        for (int k = 1; k <= _s; k <<= 1)
        {
            vv.push_back(_v * k);
            ww.push_back(_w * k);
            nn++;
            _s -= k;
        }
        if (_s > 0)
        {
            vv.push_back(_v * _s);
            ww.push_back(_w * _s);
            nn++;
        }
    }

    for (int i = 1; i <= nn; i++)
    {
        for (int j = m; j >= vv[i]; j--)
        {
            f[j] = max(f[j], f[j - vv[i]] + ww[i]);
        }
    }

    cout << f[m] << endl;
    return 0;
}

int main_stack()
{
    int dp[N], pre[N], q[N];

    cin >> n >> m;
    for (int i = 0; i < n; ++i)
    {
        memcpy(pre, dp, sizeof(dp));
        int v, w, s;
        cin >> v >> w >> s;
        for (int j = 0; j < v; ++j)
        {
            int head = 0, tail = -1;
            for (int k = j; k <= m; k += v)
            {

                if (head <= tail && k - s * v > q[head])
                    ++head;

                while (head <= tail && pre[q[tail]] - (q[tail] - j) / v * w <= pre[k] - (k - j) / v * w)
                    --tail;

                if (head <= tail)
                    dp[k] = max(dp[k], pre[q[head]] + (k - q[head]) / v * w);

                q[++tail] = k;
            }
        }
    }
    cout << dp[m] << endl;
    return 0;
}

int main_naive()
{
    cin >> n >> m;
    int f[N];                // f[i][j] = 从前i件物品中选择，体积等于j时物品的最大价值
    memset(f, 0, sizeof(f)); // 所有体积小于等于 f[i] 的最大价值是多少

    for (int i = 1; i <= n; i++)
    {
        cin >> v[i] >> w[i] >> s[i];
    }

    for (int i = 1; i <= n; i++)
    {
        for (int j = m; j >= 1; j--)
        {
            for (int k = 1; k <= s[i] && k * v[i] <= j; k++)
            {
                f[j] = max(f[j], f[j - k * v[i]] + k * w[i]);
            }
        }
    }

    cout << f[m] << endl;
    return 0;
}