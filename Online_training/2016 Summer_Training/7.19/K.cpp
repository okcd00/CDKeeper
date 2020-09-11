//
//  Created by TaoSama on 2015-07-26
//  Copyright (c) 2015 TaoSama. All rights reserved.
//
//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <set>
#include <vector>

using namespace std;
#define pr(x) cout << #x << " = " << x << "  "
#define prln(x) cout << #x << " = " << x << endl
const int N = 1e5 + 10, INF = 0x3f3f3f3f, MOD = 1e9 + 7;

int a, b, c, d, dp[205][205];
bool in[205][205];
int ans, vol;

struct P {
    int a, b, c;
    P() {}
    P(int a, int b, int c):
        a(a), b(b), c(c) {}
};

void update(P& cur) {
    if(cur.a <= d && cur.a > ans) {
        ans = cur.a;
        vol = dp[cur.a][cur.b];
    }
    if(cur.b <= d && cur.b > ans) {
        ans = cur.b;
        vol = dp[cur.a][cur.b];
    }
    if(c - cur.a - cur.b <= d && c - cur.a - cur.b > ans) {
        ans = c - cur.a - cur.b;
        vol = dp[cur.a][cur.b];
    }
}

void bfs() {
    deque<P> q;
    memset(dp, 0x3f, sizeof dp);
    memset(in, false, sizeof in);
    q.push_back(P(0, 0, c)); dp[0][0] = 0;
    in[0][0] = true;
    while(q.size()) {
        //a -> b
        P cur = q.front(), nxt; q.pop_front();
        update(cur);  //update the ans
        in[cur.a][cur.b] = false;
        if(cur.a && cur.b < b) {
            nxt = cur;
            int pour = cur.a > b - cur.b ? b - cur.b : cur.a;
            nxt.a -= pour;  nxt.b += pour;
            if(!in[nxt.a][nxt.b] &&
                    dp[nxt.a][nxt.b] > dp[cur.a][cur.b] + pour) {
                dp[nxt.a][nxt.b] = dp[cur.a][cur.b] + pour;
                in[nxt.a][nxt.b] = true;
                if(q.size()) {
                    P t = q.front();
                    if(dp[nxt.a][nxt.b] < dp[t.a][t.b])
                        q.push_front(nxt);
                    else q.push_back(nxt);
                } else q.push_back(nxt);
            }
        }
        //b - > a
        if(cur.b && cur.a < a) {
            nxt = cur;
            int pour = cur.b > a - cur.a ? a - cur.a : cur.b;
            nxt.b -= pour; nxt.a += pour;
            if(!in[nxt.a][nxt.b]
                    && dp[nxt.a][nxt.b] > dp[cur.a][cur.b] + pour) {
                dp[nxt.a][nxt.b] = dp[cur.a][cur.b] + pour;
                in[nxt.a][nxt.b] = true;
                if(q.size()) {
                    P t = q.front();
                    if(dp[nxt.a][nxt.b] < dp[t.a][t.b])
                        q.push_front(nxt);
                    else q.push_back(nxt);
                } else q.push_back(nxt);
            }
        }
        //a -> c;
        if(cur.a && cur.c < c) {
            nxt = cur;
            int pour = cur.a > c - cur.c ? c - cur.c : cur.a;
            nxt.a -= pour; nxt.c += pour;
            if(!in[nxt.a][nxt.b]
                    && dp[nxt.a][nxt.b] > dp[cur.a][cur.b] + pour) {
                dp[nxt.a][nxt.b] = dp[cur.a][cur.b] + pour;
                in[nxt.a][nxt.b] = true;
                if(q.size()) {
                    P t = q.front();
                    if(dp[nxt.a][nxt.b] < dp[t.a][t.b])
                        q.push_front(nxt);
                    else q.push_back(nxt);
                } else q.push_back(nxt);
            }
        }
        //c -> a
        if(cur.c && cur.a < a) {
            nxt = cur;
            int pour = cur.c > a - cur.a ? a - cur.a : cur.c;
            nxt.c -= pour; nxt.a += pour;
            if(!in[nxt.a][nxt.b]
                    && dp[nxt.a][nxt.b] > dp[cur.a][cur.b] + pour) {
                dp[nxt.a][nxt.b] = dp[cur.a][cur.b] + pour;
                in[nxt.a][nxt.b] = true;
                if(q.size()) {
                    P t = q.front();
                    if(dp[nxt.a][nxt.b] < dp[t.a][t.b])
                        q.push_front(nxt);
                    else q.push_back(nxt);
                } else q.push_back(nxt);
            }
        }
        //b -> c
        if(cur.b && cur.c < c) {
            nxt = cur;
            int pour = cur.b > c - cur.c ? c - cur.c : cur.b;
            nxt.b -= pour; nxt.c +=  pour;
            if(!in[nxt.a][nxt.b]
                    && dp[nxt.a][nxt.b] > dp[cur.a][cur.b] + pour) {
                dp[nxt.a][nxt.b] = dp[cur.a][cur.b] + pour;
                in[nxt.a][nxt.b] = true;
                if(q.size()) {
                    P t = q.front();
                    if(dp[nxt.a][nxt.b] < dp[t.a][t.b])
                        q.push_front(nxt);
                    else q.push_back(nxt);
                } else q.push_back(nxt);
            }
        }
        //c -> b
        if(cur.c && cur.b < b) {
            nxt = cur;
            int pour = cur.c > b - cur.b ? b - cur.b : cur.c;
            nxt.c -= pour; nxt.b += pour;
            if(!in[nxt.a][nxt.b]
                    && dp[nxt.a][nxt.b] > dp[cur.a][cur.b] + pour) {
                dp[nxt.a][nxt.b] = dp[cur.a][cur.b] + pour;
                in[nxt.a][nxt.b] = true;
                if(q.size()) {
                    P t = q.front();
                    if(dp[nxt.a][nxt.b] < dp[t.a][t.b])
                        q.push_front(nxt);
                    else q.push_back(nxt);
                } else q.push_back(nxt);
            }
        }
    }
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    int t; cin >> t;
    while(t--) {
        cin >> a >> b >> c >> d;
        ans = vol = 0;
        bfs();
        cout << vol << ' ' << ans << '\n';
    }
    return 0;
}
