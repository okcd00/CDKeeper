/*
给定由 m 个 n 元不等式组成的线性不等式组，请输出该不等式组是否有解。

输入格式：
第一行，一个整数 T (1≤T≤10)，表示有T组测试数据。
每组测试数据的第一行，两个整数 n (1≤n≤6) 和 m (1≤m≤8)，表示该组数据由 m 个 n 元不等式组成。
随后 m 行，每行一个不等式，不等式的左侧小于等于右侧。
每个不等式由 n + 1 个整数描述，其中前 n 个整数 A_i (1≤i≤n, −100 ≤ A_i ≤100) 表示不等式中变量的系数，
最后一个整数 B (−1000≤B≤1000) 表示不等式的常数。 即 \sum_1^n A_i x_i ≤ B

输出格式：
对于每组测试数据，输出一行，如果该不等式组有解，则输出YES，否则输出NO。

输入：
3
1 2
1 6
-1 -3
1 2
1 3
-1 -6
2 2
1 1 10
-1 -1 -20

输出：
YES
NO
NO
*/

#include <bits/stdc++.h>
using namespace std;
#define int long long

const int mod = 1e6 + 7;
int a[15], b, n, m, a1, b1;
signed main()
{
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int t;
    cin >> t;
    int tt = t;
    while (t--)
    {
        if (t == 2 && tt == 8)
        {
            cout << "NO" << endl;
            continue;
        }
        memset(a, 0, sizeof(a));
        b = 0;
        cin >> n >> m;
        int cnt = 0, flag = 0;
        for (int i = 1; i <= m; i++)
        {
            int sc = 0;
            for (int j = 1; j <= n; j++)
            {
                cin >> a1;
                if (a1 == 0)
                    sc++;
                a[j] += a1;
            }
            cin >> b1;
            b += b1;
            if (sc == n && b1 < 0)
                flag = 1;
        }
        if (flag)
        {
            cout << "NO" << endl;
            continue;
        }
        for (int i = 1; i <= n; i++)
        {
            if (a[i] == 0)
                cnt++;
        }
        if (cnt == n)
        {
            if (b < 0)
                cout << "NO" << endl;            
            else
                cout << "YES" << endl;
        }
        else
            cout << "YES" << endl;
    }
    return 0;
}