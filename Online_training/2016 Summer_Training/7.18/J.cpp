//
//  POJ 3669 Meteor Shower
//
//  Created by TaoSama on 2015-02-20
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

struct Point {
    int x, y, t;
    Point(int x = 0, int y = 0, int t = 0): x(x), y(y), t(t) {}
};
int n, a[305][305];
int d[5][2] = {0, -1, 0, 1, 1, 0, -1, 0, 0, 0};
int bfs() {
    queue<Point> q; q.push(Point(0, 0));
    while(!q.empty()) {
        Point cur = q.front(); q.pop();
        for(int i = 0; i < 4; ++i) {
            Point nxt(cur.x + d[i][0], cur.y + d[i][1]);
            nxt.t = cur.t + 1;
            if(nxt.x < 0 || nxt.y < 0) continue;
            if(a[nxt.x][nxt.y] == INF) return nxt.t;
            if(nxt.t < a[nxt.x][nxt.y]) {
                a[nxt.x][nxt.y] = nxt.t;
//              cout<<"nxt: "<<nxt.t<<endl;
                q.push(nxt);
            }
        }
    }
    return -1;
}
int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(scanf("%d", &n) == 1) {
        memset(a, 0x3f, sizeof a);
        for(int i = 1; i <= n; ++i) {
            int x, y, t; scanf("%d%d%d", &x, &y, &t);
            for(int j = 0; j < 5; ++j) {
                int nx = x + d[j][0], ny = y + d[j][1];
                if(nx < 0 || ny < 0) continue;
                a[nx][ny] = min(t, a[nx][ny]);
            }
        }
        int ans = bfs();
        printf("%d\n", ans);
    }
    return 0;
}