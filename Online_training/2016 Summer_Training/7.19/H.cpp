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

int n, ans, now[10];
bool vis[10], have[10];

void dfs(int dep) {
    if(dep == 5 + 1) {
        int cur = 0;
        memset(have, false, sizeof have);
        for(int i = 1; i <= 5; ++i) {
            cur = cur * 10 + now[i];
            have[now[i]] = true;
        }
        int lef = cur * n;
        char s[10]; sprintf(s, "%d", lef);
        if(strlen(s) != 5) return;

        bool ok = true;
        for(int i = 0; s[i]; ++i) {
            if(have[s[i] - '0']) {
                ok = false;
                break;
            } else have[s[i] - '0'] = true;
        }
        if(ok) ++ans, printf("%d / %05d = %d\n", lef, cur, n);
        return;
    }
    for(int i = 0; i < 10; ++i) {
        if(vis[i]) continue;
        now[dep] = i;
        vis[i] = true;
        dfs(dep + 1);
        vis[i] = false;
    }
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    bool first = false;
    while(scanf("%d", &n) == 1 && n) {
        memset(vis, false, sizeof vis);
        if(!first) first = true;
        else puts("");
        ans = 0;
        dfs(1);
        if(!ans) printf("There are no solutions for %d.\n", n);
    }
    return 0;
}
