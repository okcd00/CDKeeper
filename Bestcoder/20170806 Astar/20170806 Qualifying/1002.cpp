/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : 1002.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2017-08-06
#   desc     : cut strong-connect-graph
#   bestcoder.hdu.edu.cn/contests/contest_showproblem.php?cid=774&pid=1002
# ==========================================================================*/

#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;  
#define __int64 long long  

const int N = 1e5 + 10, INF = 0x3f3f3f3f, MOD = 1e9 + 7;

int n, m;
int sum[N];

int main(){
#ifdef LOCAL
    freopen("/Users/didi/ACM/in.txt", "r", stdin);
//  freopen("/Users/didi/ACM/out.txt", "w", stdout);
#endif
    
    while(scanf("%d%d", &n, &m) == 2) {
        memset(sum, 0, sizeof sum);
        for(int i = 1; i <= n; ++i) sum[i] = 0;
        for(int i = 1; i <= m; ++i) {
            int u, v, c; scanf("%d%d%d", &u, &v, &c);
            if(u != v) {
                sum[u] += c;
                sum[v] += c;
            }
        }
        printf("%d\n", *min_element(sum + 1, sum + 1 + n));
    }    
    return 0;
}
