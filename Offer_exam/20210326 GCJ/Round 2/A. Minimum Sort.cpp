#include <iostream>
#include <cstdio>
#include <stack>
#include <cstring>
#include <queue>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <set>
#include <map>
#include <unordered_map>
#define lson x<<1
#define rson x<<1|1
#define mid ((lt[x].l+lt[x].r)/2)
#define mkpr make_pair
//#define ID(x, y) ((x)*m+(y))
//#define CHECK(x, y) ((x)>=0 && (x)<n && (y)>=0 && (y)<m)
using namespace std;
typedef long long LL;
typedef pair<LL,LL> PII;
const int mod = 998244353;
const int INF=0x3f3f3f3f;
const int N = 50010;

int query(char t, int i, int j)
{
    if(t == 'D') printf("D\n");
    else printf("%c %d %d\n", t, i, j);
    fflush(stdout);
    int res;
    scanf("%d", &res);
    return res;
}


int main()
{
    // std::ios::sync_with_stdio(false);
    // std::cin.tie(0);
    // int T;
    // cin >> T;
    // for(; T--;)
    int T, cas=1;
    int n;
    for(scanf("%d%d", &T, &n); T--;)
    {
        // int n;
        // scanf("%d", &n);
        for(int i = 0; i < n-1; i++)
        {
            int res = query('M', i+1, n);
            if(res != i+1) query('S', i+1, res);
        }
        int res = query('D', 1, 2);
        // printf("Case #%d: %d\n", cas++);
    }
    // scanf("%d", &T);
    // cout << T << endl;
}