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

int n, k, m;
bool vis[25];

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(cin >> n >> k >> m && n) {
        int l = 0, r = n - 1, sz = n;
        memset(vis, false, sizeof vis);
        while(sz) {
            for(int i = 0; i < k; ++i) {
                while(vis[l]) l = (l + 1) % n;
                l = (l + 1) % n;
            }
            for(int i = 0; i < m; ++i) {
                while(vis[r]) r = (r - 1 + n) % n;
                r = (r - 1 + n) % n;
            }

//          cout << "L: " << l << " R: " << r << endl;

            int lastl = (l - 1 + n) % n;
            int lastr = (r + 1) % n;

            if(lastl == lastr) {
                vis[lastl] = true;
                cout << setw(3) << lastl + 1;
                --sz;
            } else {
                vis[lastl] = vis[lastr] = true;
                cout << setw(3) << lastl  + 1 << setw(3) << lastr + 1;
                sz -= 2;
            }
            cout << (sz ? "," : "\n");
        }
    }
    return 0;
}
