//
//  Created by TaoSama on 2015-07-19
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

int n, sx, sy, gx, gy;
int d[][2] = { -1, 0, 0, -1, 1, 0, 0, 1};
int h[][2] = { -1, 2, 1, 2, -2, 1, -2, -1, -1, -2, 1, -2, 2, 1, 2, -1};
int no[][2] = {0, 1, -1, 0, 0, -1, 1, 0};
char wh[15][15];

struct P {
    char op;
    int x, y;
} a[10];

bool inBound(int x, int y) {
    return x >= 1 && x <= 10 && y <= 1 && y <= 9;
}

bool inGeneral(int x, int y) {
    return x >= 1 && x <= 3 && y >= 4 && y <= 6;
}

bool check(int x, int y) {
    int other = 0;
    for(int i = x + 1; i <= 10; ++i) {
        if(wh[i][y] == 'R' && !other) return true;
        if(wh[i][y] == 'G' && !other) return true;
        if(wh[i][y] == 'C' && other == 1) return true;

        if(isalpha(wh[i][y])) ++other;
    }

    other = 0;
    for(int i = x - 1; i; --i) {
        if(wh[i][y] == 'R' && !other) return true;
        if(wh[i][y] == 'G' && !other) return true;
        if(wh[i][y] == 'C' && other == 1) return true;

        if(isalpha(wh[i][y])) ++other;
    }

    other = 0;
    for(int i = y + 1; i <= 9; ++i) {
        if(wh[x][i] == 'R' && !other) return true;
        if(wh[x][i] == 'G' && !other) return true;
        if(wh[x][i] == 'C' && other == 1) return true;

        if(isalpha(wh[x][i])) ++other;
    }

    other = 0;
    for(int i = y - 1; i; --i) {
        if(wh[x][i] == 'R' && !other) return true;
        if(wh[x][i] == 'G' && !other) return true;
        if(wh[x][i] == 'C' && other == 1) return true;

        if(isalpha(wh[x][i])) ++other;
    }

    for(int i = 1; i <= 10; ++i) {
        for(int j = 1; j <= 9; ++j) {
            if(wh[i][j] == 'H') {
                for(int k = 0; k < 8; ++k) {
                    int nx = i + h[k][0], ny = j + h[k][1];
                    int bx = i + no[k >> 1][0], by = j + no[k >> 1][1];
                    if(nx == x && ny == y && !isalpha(wh[bx][by])) return true;
                }
            }
        }
    }

    return false;
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(cin >> n >> gx >> gy && (n || gx || gy)) {
        memset(wh, 0, sizeof wh);
        for(int i = 1; i <= n; ++i) {
            cin >> a[i].op >> a[i].x >> a[i].y;
            wh[a[i].x][a[i].y] = a[i].op;
        }

        bool die = true;
        for(int i = 0; i < 4; ++i) {
            int nx = gx + d[i][0], ny = gy + d[i][1];
            if(!inGeneral(nx, ny)) continue;

            char last = wh[nx][ny]; wh[nx][ny] = 0;

            if(!check(nx, ny)) {
                die = false;
                break;
            }

            wh[nx][ny] = last;
        }

        cout << (die ? "YES" : "NO") << '\n';
    }
    return 0;
}

/* 2->NO
2 1 4
G 10 5
R 6 4

3 1 5
H 4 5
G 10 5
C 7 5

4 1 5
G 10 5
R 1 1
H 2 3
C 2 2

3 3 4
G 10 5
R 1 4
H 2 4

1 3 4
G 10 4
0 0 0
*/
