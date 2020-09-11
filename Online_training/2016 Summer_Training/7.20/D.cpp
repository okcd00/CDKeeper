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

int t;
map<int, int> mp, wh;

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    int kase = 0;
    while(scanf("%d", &t) == 1 && t) {
        mp.clear(); wh.clear();
        for(int i = 1; i <= t; ++i) {
            int n; scanf("%d", &n);
            for(int j = 1; j <= n; ++j) {
                int x; scanf("%d", &x);
                wh[x] = i;
            }
        }

        queue<int> all, each[1005];
        printf("Scenario #%d\n", ++kase);
        while(true) {
            char op[20]; scanf("%s", op);
            if(op[0] == 'E') {
                int x; scanf("%d", &x);
                if(!mp.count(wh[x])) {
                    all.push(wh[x]);
                    mp[wh[x]] = 1;
                }
                each[wh[x]].push(x);
            } else if(op[0] == 'D') {
//              cout << all.size() << endl;
                if(all.empty()) continue;
                int p = all.front();
                int cur = each[p].front(); each[p].pop();
                if(each[p].empty()) {
                    all.pop();
                    mp.erase(wh[cur]);
                }
                printf("%d\n", cur);
            } else break;
        }
        puts("");
    }
    return 0;
}
