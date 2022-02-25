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

int n, vis[20], cur[20];

bool isPrime(int n) {
    for(int i = 2; i * i <= n; ++i)
        if(n % i == 0) return false;
    return true;
}

void dfs(int dep) {
    if(dep == n + 1) {
        if(isPrime(cur[n] + cur[1])) {
            for(int i = 1; i <= n; ++i)
                cout << cur[i] << (i == n ? "\n" : " ");
        }
        return;
    }
    for(int i = 2; i <= n; ++i) {
        if(vis[i] || !isPrime(i + cur[dep - 1])) continue;
        cur[dep] = i;
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

    int kase = 0;
    while(cin >> n) {
        if(kase) cout << "\n";
        cout << "Case " << ++kase << ":\n";
        memset(vis, false, sizeof vis);
        cur[1] = 1;
        dfs(2);
    }
    return 0;
}
