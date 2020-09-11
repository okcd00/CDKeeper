#include<bits/stdc++.h>
using namespace std;

int main()
{
    int T; scanf("%d", &T);
    while (T--)
    {
        int n, m, p; scanf("%d%d%d", &n, &m, &p);
        int d = m - m * (100 - p) / 100;
        if (n < m) printf("%d\n", 0);
        else printf("%d\n", (n - m + d) / d);
    }
    return 0;
}
