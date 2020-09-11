//
//  POJ 3050 Hopscotch
//
//  Created by TaoSama on 2015-02-21
//  Copyright (c) 2015 TaoSama. All rights reserved.
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

char a[8][8];
int d[4][2] = { -1, 0, 1, 0, 0, 1, 0, -1};
set<string> s;
void dfs(int x, int y, string cur, int k) {
    if(k == 5) {
        s.insert(cur);
        return;
    }
    for(int i = 0; i < 4; ++i) {
        int nx = x + d[i][0], ny = y + d[i][1];
        if(nx < 1 || nx > 5 || ny < 1 || ny > 5) continue;
        dfs(nx, ny, cur + a[nx][ny], k + 1);
    }
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);
    for(int i = 1; i <= 5; ++i)
        for(int j = 1; j <= 5; ++j)
            cin >> a[i][j];
    for(int i = 1; i <= 5; ++i) {
        for(int j = 1; j <= 5; ++j) {
            string cur; cur += a[i][j];
            dfs(i, j, cur, 0);
        }
    }
    cout << s.size() << endl;
    return 0;
}