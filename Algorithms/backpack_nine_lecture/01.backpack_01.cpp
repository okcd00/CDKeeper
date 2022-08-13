/*
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
*/

#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 1010;

int n, m;
int v[N], w[N];  // v[i] = 体积, w[i] = 价值


int main() {
    cin >> n >> m;
    int f[N][N];  // f[i][j] = 从前i件物品中选择，体积等于j时物品的最大价值

    for (int i = 1; i <= n; i++) {
        cin >> v[i] >> w[i];
    }

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
            if (j < v[i]) {
                f[i][j] = f[i - 1][j];
            } else {
                f[i][j] = max(f[i - 1][j], f[i - 1][j - v[i]] + w[i]);
            }
        }
    }

    int res = 0;
    for (int i = 0; i <= m; i++) {
        res = max(res, f[n][i]);
    }

    cout << res << endl;
    return 0;
}


int optimized_main() {
    cin >> n >> m;
    int f[N];  // 滚动数组
    memset(f, 0, sizeof(f));  // 所有体积小于等于 f[i] 的最大价值是多少
    // for (int i=1; i<=n; i++) f[i] = -INF;  // 所有体积恰好等于 f[i] 的最大价值是多少

    for (int i = 1; i <= n; i++) {
        cin >> v[i] >> w[i];
    }

    for (int i = 1; i <= n; i++) {
        for (int j = m; j >= v[i]; j--) {
            f[j] = max(f[j], f[j - v[i]] + w[i]);
        }
    }

    cout << f[m] << endl;
    return 0;
}
