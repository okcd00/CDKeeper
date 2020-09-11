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

int n;
typedef unsigned int uint;

void print(uint x) {
    for(int i = 3; i >= 0; --i) {
        if(i != 3) putchar('.');
        printf("%u", x >> (3 << 3));
        x <<= 8;
    }
    puts("");
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(scanf("%d", &n) == 1) {
        uint a[4];
        uint maxv = 0, minv = ~0u;
        for(int i = 1; i <= n; ++i) {
            scanf("%u.%u.%u.%u", a + 3, a + 2, a + 1, a);
            uint x = 0;
            for(int j = 3; j >= 0; --j) {
                x += a[j] << (j * 8);
            }
//            cout << x << endl;
            maxv = max(maxv, x);
            minv = min(minv, x);
        }
//        pr(minv); prln(maxv);

        int zero = 0;
        if((long long)maxv - minv + 1 != 1) {
            for(int i = 0; i < 32; ++i) {
                minv &= ~(1u << i);
                ++zero;
//          prln(minv);
//          printf("...%d   %d\n", 1u << zero, (long long)maxv - minv + 1);
                if(1LL << zero >= (long long)maxv - minv + 1) break;
            }
        }
//      cout << zero << endl;

        maxv = ~0u;
        for(int i = 0; i < zero; ++i)
            maxv &= ~(1u << i);
//        cout << minv << ' ' << maxv << endl;

        print(minv);
        print(maxv);
    }
    return 0;
}
