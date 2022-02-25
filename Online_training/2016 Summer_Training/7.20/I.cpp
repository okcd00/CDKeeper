//
//  Created by TaoSama on 2015-07-21
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

int n, a[15], b[15], c[15];

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    int kase = 0;
    while(cin >> n, n) {
        int awake = 0, ans = -1;
        for(int i = 1; i <= n; ++i) {
            cin >> a[i] >> b[i] >> c[i];
            if(c[i] <= a[i]) ++awake;
        }

        for(int k = 1; k < 1e5; ++k) {
            if(awake == n) {
                ans = k;
                break;
            }
            bool can = n - awake > awake;
            for(int i = 1; i <= n; ++i) {
                ++c[i];
                if(c[i] == a[i] + 1) {
                    if(can) --awake;
                    else c[i] = 1;
                }
                if(c[i] == a[i] + b[i] + 1) {
                    c[i] = 1;
                    ++awake;
                }
            }
        }
        cout << "Case " << ++kase << ": " << ans << '\n';
    }
    return 0;
}
