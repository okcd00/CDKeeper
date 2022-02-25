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

int n, k, cnt, a[105];

bool dfs(int dep) {
    if(++cnt == k + 1) {
        for(int i = 1; i < dep; ++i) {
            cout << char('A' + a[i]);
            if(i % 4 == 0 && i != dep - 1 && i % 64)
                cout << ' ';
            if(i % 64 == 0) cout << '\n';
        }
        cout << '\n' << dep - 1 << '\n';
        return true;
    }
    for(int i = 0; i < n; ++i) {
        a[dep] = i;
        bool can = true;
        for(int j = 1; j + j <= dep; ++j) {
            bool same = true;
            for(int k = dep - (j << 1) + 1; k <= dep - j; ++k) {
                if(a[k] != a[k + j]) {
                    same = false;
                    break;
                }
            }
            if(same) {can = false; break;}
        }
        if(can && dfs(dep + 1)) return true;
    }
    return false;
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(cin >> k >> n && (n || k)) {
        cnt = 0;
        dfs(1);
    }
    return 0;
}
