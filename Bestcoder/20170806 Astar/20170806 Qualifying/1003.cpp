/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : 1003.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2017-08-06
#   desc     : Skill and monster type.
#   bestcoder.hdu.edu.cn/contests/contest_showproblem.php?cid=774&pid=1003
# ==========================================================================*/

#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;  
const int N = 1e5 + 10, INF = 0x3f3f3f3f, MOD = 1e9 + 7;

int n, m;
int cnt[1010][20], cost[1010][20];

int main(){
#ifdef LOCAL
//  freopen("/Users/didi/ACM/in.txt", "r", stdin);
//  freopen("/Users/didi/ACM/out.txt", "w", stdout);
#endif
    ios::sync_with_stdio(0); cin.tie(0);
    
    while(scanf("%d%d", &n, &m) == 2) {
        memset(cnt, 0, sizeof cnt);
        memset(cost, 0x3f, sizeof cost);
        for(int i = 0; i <= 10; ++i) cost[0][i] = 0;
        for(int i = 1; i <= n; ++i) {
            int a, b; scanf("%d%d", &a, &b);
            ++cnt[a][b];
        }
        for(int i = 1; i <= m; ++i) {
            int c, p; scanf("%d%d", &c, &p);
            for(int j = 1; j <= 1000; ++j) {
                for(int k = 0; k <= 10; ++k) {
                    int atk = p - k;
                    cost[j][k] = min(cost[j][k], cost[max(0, j - atk)][k] + c);
                }
            } 
        }
        long long ans = 0;
        bool ok = true;
        for(int i = 1; i <= 1000; ++i) {
            for(int k = 0; k <= 10; ++k) {
                if(cnt[i][k] && cost[i][k] == INF) ok = false;
                ans += cnt[i][k] * cost[i][k];
            } 
        }
        if(!ok) ans = -1;
        printf("%I64d\n", ans);
    } 
    return 0;
}
