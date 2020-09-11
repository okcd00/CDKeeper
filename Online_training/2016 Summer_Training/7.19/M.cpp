//
//  Created by TaoSama on 2015-07-27
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

int n, maxd;

struct Sta {
    int a[15];
} st;

//incorrect successors
int getH(Sta &s) {
    int cnt = 0;
    for(int i = 1; i < n; ++i)
        if(s.a[i] + 1 != s.a[i + 1]) cnt++;
    return cnt;
}

bool dfs(Sta u, int d) {
    int h = getH(u);  //check the difference from the ascending order
    if(d == maxd) return h == 0;
    //a->b->c => a->c->b all of 3 successors changed
    if(3 * d + h > 3 * maxd) return false;
    //suspected cur max change + need to change > can change => pruning

    int b[15];
    for(int i = 1; i <= n; ++i) {
        for(int j = i; j <= n; ++j) {
            int cnt = 0;  Sta v;
            for(int k = 1; k <= n; ++k)  //cut [i, j]
                if(k < i || k > j) b[++cnt] = u.a[k];

            //insert before k (there's a position after the sequence so cnt+1)
            for(int k = 1; k <= cnt + 1; ++k) {
                int cnt2 = 0;
                for(int p = 1; p < k; ++p) v.a[++cnt2] = b[p];
                for(int p = i; p <= j; ++p) v.a[++cnt2] = u.a[p];
                for(int p = k; p <= cnt; ++p) v.a[++cnt2] = b[p];

                if(dfs(v, d + 1)) return true;
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

    int kase = 0;
    while(cin >> n && n) {
        for(int i = 1; i <= n; ++i) cin >> st.a[i];
        for(maxd = 0; ; maxd++) {
            if(dfs(st, 0)) break;
        }
        cout << "Case " << ++kase << ": " << maxd << '\n';
    }
    return 0;
}
