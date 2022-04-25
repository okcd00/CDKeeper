#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#define N 300010
using namespace std;
typedef long long LL;
const LL INF = 0x3f3f3f3f3f3f3f3f;

int x[1010][111];
LL dp[1010][111];

int main()
{
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        int n, p;
        scanf("%d%d", &n, &p);
        for (int i = 1; i <= n; i++)
        {
            for (int j = 0; j < p; j++)
            {
                scanf("%d", &x[i][j]);
                dp[i][j] = INF;
            }
            sort(x[i], x[i] + p);
        }

        for (int i = 1; i <= n; i++)
            for (int j = 0; j < p; j++)
                for (int k = 0; k < p; k++)
                {
                    LL sup = abs(x[i][p - 1] - x[i - 1][j]); // to top
                    sup += abs(x[i][p - 1] - x[i][0]);       // to bottom
                    sup += abs(x[i][0] - x[i][k]);
                    LL sdw = abs(x[i - 1][j] - x[i][0]); // to bottom
                    sdw += abs(x[i][0] - x[i][p - 1]);
                    sdw += abs(x[i][p - 1] - x[i][k]);

                    LL tmp = min(sup, sdw);
                    dp[i][k] = min(dp[i][k], dp[i - 1][j] + tmp);
                }
        
        LL ret = INF;
        for (int i = 0; i < p; i++)
            ret = min(ret, dp[n][i]);
        printf("Case #%d: ", cas);
        cout << ret << "\n";
    }
    return 0;
}