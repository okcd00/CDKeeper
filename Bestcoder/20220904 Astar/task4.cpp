#include <bits/stdc++.h>
using namespace std;
using ll = long long;
using pii = array<int, 2>;
constexpr int N = 1010;
constexpr int inf = 1E9;
constexpr int p = 998244353;

int qpow(int x, int n = p - 2)
{
    int y = 1;
    for (; n; n >>= 1, x = 1LL * x * x % p)
        if (n & 1)
            y = 1LL * y * x % p;
    return y;
}

template <typename T = int>
T read()
{
    T x;
    cin >> x;
    return x;
}

int q[4][2] = {0, -1, 0, 1, -1, 0, 1, 0};
char a[N][N];
bool b[N][N];
int f[3], s;
void dfs(int i, int j, int u, int v)
{
    b[i][j] = 1;
    for (auto [x, y] : q)
    {
        x += i;
        y += j;
        if (a[x][y] ^ '#' || x == u && y == v)
            continue;
        if (b[x][y])
            ++s;
        else
            dfs(x, y, i, j);
    }
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    cout << fixed << setprecision(6);
    int n = read(), m = read();
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            cin >> a[i][j];
    for (int i = 1; i <= n; ++i)
        for (int j = 1; j <= m; ++j)
            if (a[i][j] ^ '.' && !b[i][j])
            {
                s = 0;
                dfs(i, j, 0, 0);
                ++f[s >> 1];
            }
    cout << f[0] << ' ' << f[1] << ' ' << f[2] << '\n';
    exit(0);
}