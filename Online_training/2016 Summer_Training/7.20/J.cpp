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

long long n, p, q;

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(cin >> n >> p >> q) {
        long long K = 1LL << 60, A, B;
        for(int i = 0; i < 32; ++i) {
            for(int j = 0; j < 32; ++j) {
                long long t = (((n - 1) * p + ((n - 1) * p << i)) >> j) + q;
                if(t >= n * q && t < K) {
                    K = t;
                    A = i;
                    B = j;
                }
            }
        }
        cout << K << ' ' << A << ' ' << B << '\n';

    }
    return 0;
}
