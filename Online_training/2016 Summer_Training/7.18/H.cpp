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

int w, b;
int cur;
char a[10][10];

void getMove() {
    vector<pair<int, int> > mov;
    for(int i = 1; i <= 8; ++i) {
        for(int j = 1; j <= 8; ++j) {
            if(a[i][j] != cur) continue;
//            cout << i << ' '<< j << endl;
            for(int dx = -1; dx <= 1; ++dx) {
                for(int dy = -1; dy <= 1; ++dy) {
                    if(dx == 0 && dy == 0) continue;
                    int cnt = 0, k;
//                    pr(i); prln(j);
                    for(k = 1; ; ++k) {
                        int x = i + dx * k, y = j + dy * k;
//                        pr(x); prln(y);
                        if(x < 1 || x > 8 || y < 1 || y > 8 || a[x][y] == cur) {
                            cnt = 0;
                            break;
                        } else if(a[x][y] == '-') break;
                        else ++cnt;
                    }
                    if(cnt) mov.push_back({i + dx * k, j + dy * k});
                }
            }
        }
//        cout << endl;
    }
//    cout << endl;
    sort(mov.begin(), mov.end());
    mov.resize(unique(mov.begin(), mov.end()) - mov.begin());
    for(int i = 0; i < mov.size(); ++i) {
        if(i) putchar(' ');
        printf("(%d,%d)", mov[i].first, mov[i].second);
    }
    if(mov.empty()) printf("No legal move.");
    puts("");
}

bool go(int x, int y) {
    bool legal = false;
    for(int dx = -1; dx <= 1; ++dx) {
        for(int dy = -1; dy <= 1; ++dy) {
            if(dx == 0 && dy == 0) continue;
            int cnt = 0, k;
            for(k = 1; ; ++k) {
                int nx = x + dx * k, ny = y + dy * k;
                if(nx < 1 || nx > 8 || ny < 1 || ny > 8 || a[nx][ny] == '-') {
                    cnt = 0;
                    break;
                } else if(a[nx][ny] == cur) break;
                else ++cnt;
            }
            if(cnt) {
                legal = true;
                if(cur) b += cnt, w -= cnt;
                else b -= cnt, w += cnt;
                for(k = 1; ; ++k) {
                    int nx = x + dx * k, ny = y + dy * k;
                    if(a[nx][ny] == cur) break;
                    a[nx][ny] = cur;
                }
            }
        }
    }
    if(legal) {
        a[x][y] = cur;
        cur ? ++b : ++w;
        cur ^= 1;
    }
    return legal;
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);

    int t; scanf("%d", &t);
    int kase = 0;
    while(t--) {
        w = b = 0;
        if(kase++) puts("");
        for(int i = 1; i <= 8; ++i) {
            scanf("%s", a[i] + 1);
            for(int j = 1; j <= 8; ++j) {
                if(a[i][j] == 'W') {
                    a[i][j] = 0;
                    ++w;
                }
                if(a[i][j] == 'B') {
                    a[i][j] = 1;
                    ++b;
                }
            }
        }
//        pr(w); prln(b);
        int x, y;
        while(true) {
            char op[5]; scanf("%s", op);
            if(op[0] == 'W' || op[0] == 'B') cur = op[0] == 'B';
            else if(op[0] == 'L') {
//                prln(cur);
                getMove();
            } else if(op[0] == 'M') {
                x = op[1] - '0', y = op[2] - '0';
                if(!go(x, y)) {
                    cur ^= 1;
                    go(x, y);
                }
                printf("Black - %2d White - %2d\n", b, w);
            } else {
                for(int i = 1; i <= 8; ++i) {
                    for(int j = 1; j <= 8; ++j) {
                        if(a[i][j] == 1) putchar('B');
                        else if(a[i][j] == 0) putchar('W');
                        else putchar(a[i][j]);
                    }
                    putchar('\n');
                }
                break;
            }
        }
    }
    return 0;
}
