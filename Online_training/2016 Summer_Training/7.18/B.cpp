//
//  1979 Red and Black
//
//  Created by TaoSama on 2015-02-19
//  Copyright (c) 2014 TaoSama. All rights reserved.
//
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
#define CLR(x,y) memset(x, y, sizeof(x))

using namespace std;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 1e5 + 10;

int n, m, sx, sy;
char a[25][25];
bool vis[25][25];
int d[4][2] = { -1, 0, 1, 0, 0, 1, 0, -1};
void dfs(int x, int y) {
    vis[x][y] = 1;
    for(int i = 0; i < 4; ++i) {
        int nx = x + d[i][0], ny = y + d[i][1];
        if(!vis[nx][ny] && nx >= 1 && nx <= n && ny >= 1
                && ny <= m && a[nx][ny] == '.') dfs(nx, ny);
    }
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(cin >> m >> n && n != 0 && m != 0) {
        memset(vis, 0, sizeof vis);
        for(int i = 1; i <= n; ++i) {
            for(int j = 1; j <= m; ++j) {
                cin >> a[i][j];
                if(a[i][j] == '@') sx = i, sy = j;
            }
        }
        dfs(sx, sy);
        int ans = 0;
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= m; ++j)
                if(vis[i][j]) ++ans;
        cout << ans << endl;
    }
    return 0;
}