//
//  Created by TaoSama on 2015-07-20
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

int n, q;
vector<int> v;

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    int kase = 0;
    while(scanf("%d%d", &n, &q) == 2 && (n || q)) {
        v.clear();
        for(int i = 1; i <= n; ++i) {
            int x; scanf("%d", &x);
            v.push_back(x);
        }
        sort(v.begin(), v.end());
        printf("CASE# %d:\n", ++kase);
        while(q--) {
            int x; scanf("%d", &x);
            auto p = lower_bound(v.begin(), v.end(), x);
            if(p == v.end() || *p != x) printf("%d not found\n", x);
            else printf("%d found at %d\n", x, p - v.begin() + 1);
        }
    }
    return 0;
}
