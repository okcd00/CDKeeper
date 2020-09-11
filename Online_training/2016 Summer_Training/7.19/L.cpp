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
const int N = 150, INF = 0x3f3f3f3f, MOD = 1e9 + 7;

int n, m, k, cnt, s[3], t[3];
char a[20][20];
int x[N], y[N], id[20][20];
int dp[N][N][N]; //bit compressed for each ghost state
int d[][2] = {0, 0, -1, 0, 0, -1, 0, 1, 1, 0};
vector<int> G[N]; //16*16*0.75-60=130 transition for each vertex

int getId(int a, int b, int c) {
    return a << 16 | b << 8 | c;
}

bool conflict(int a, int b, int a2, int b2) {
    return a2 == b2 || a == b2 && b == a2;
}

int bfs() {
    queue<int> q; q.push(getId(s[0], s[1], s[2]));
    memset(dp, 0x3f, sizeof dp);
    dp[s[0]][s[1]][s[2]] = 0;
    while(q.size()) {
        int u = q.front(); q.pop();
        int a = u >> 16 & 0xff, b = u >> 8 & 0xff, c = u & 0xff;
        for(auto &a2 : G[a]) {
            for(auto &b2 : G[b]) {
                if(conflict(a, b, a2, b2)) continue;
                for(auto &c2 : G[c]) {
                    if(conflict(a, c, a2, c2)) continue;
                    if(conflict(b, c, b2, c2)) continue;
                    if(dp[a2][b2][c2] != INF) continue;
                    dp[a2][b2][c2] = dp[a][b][c] + 1;
                    q.push(getId(a2, b2, c2));
                }
            }
        }
    }
    return dp[t[0]][t[1]][t[2]] == INF ? -1 : dp[t[0]][t[1]][t[2]];
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(scanf("%d%d%d ", &m, &n, &k) == 3 && (n || m || k)) {
        for(int i = 1; i <= n; ++i) gets(a[i] + 1);
//        for(int i = 1; i <= n; ++i) puts(a[i] + 1);
        cnt = 0;
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= m; ++j) {
                if(a[i][j] != '#') {
                    ++cnt; x[cnt] = i, y[cnt] = j, id[i][j] = cnt;
                    if(islower(a[i][j])) s[a[i][j] - 'a'] = cnt;
                    if(isupper(a[i][j])) t[a[i][j] - 'A'] = cnt;
                }
            }
        }
        //save the transition
        for(int i = 1; i <= cnt; ++i) {
            G[i].clear();
            for(int j = 0; j < 5; ++j) {
                //due to the outermost walls we needn't check the bounds
                int nx = x[i] + d[j][0], ny = y[i] + d[j][1];
                //just check whether is the wall
                if(a[nx][ny] != '#') G[i].push_back(id[nx][ny]);
            }
        }

        //add fake ghost to shorten the code
        if(k <= 2) {G[++cnt].push_back(cnt); s[2] = t[2] = cnt;}
        if(k <= 1) {G[++cnt].push_back(cnt); s[1] = t[1] = cnt;}

        printf("%d\n", bfs());
    }
    return 0;
}
