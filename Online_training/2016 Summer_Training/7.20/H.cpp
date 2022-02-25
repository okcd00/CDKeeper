//
//  Created by TaoSama on 2015-07-22
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

int d, s, b, parity;
int a[10][7000];

bool valid() {
    int cur, bad;
    for(int j = 1; j <= s * b; ++j) {
        cur = bad = 0;
        for(int i = 1; i <= d; ++i) {
            if(a[i][j] == -1) {
                if(bad) return false;
                else bad = i;
            } else cur ^= a[i][j];
        }
        if(!bad && cur != parity) return false;
        if(bad) a[bad][j] = cur ^ parity;
    }
    return true;
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    int kase = 0;
    while(scanf("%d", &d) == 1 && d) {
        char c[2]; scanf("%d%d%s", &s, &b, c);
        parity = c[0] == 'O'; //odd->1 even->0

        //read as the input
        for(int i = 1; i <= d; ++i) {
            char buf[7000]; scanf("%s", buf + 1);
            for(int j = 1; j <= s * b; ++j)
                a[i][j] = buf[j] == 'x' ? -1 : buf[j] - '0';
        }

        printf("Disk set %d is ", ++kase);
        if(!valid()) printf("invalid.");
        else {
            printf("valid, contents are: ");

            int cur = 0, cnt = 0;
            for(int i = 1; i <= b; ++i) { //block
                int p = (i - 1) * s;
                for(int j = 1; j <= d; ++j) { //disk
                    if((i - 1) % d + 1 == j) continue; //jump the parity
                    for(int k = 1; k <= s; ++k) { //size
                        cur = (cur << 1) + a[j][p + k];
                        if(++cnt == 4) {
                            printf("%X", cur);
                            cur = cnt = 0;
                        }
                    }
                }
            }
            if(cnt) printf("%X", cur << (4 - cnt)); //add the trailing zeros
        }
        puts("");
    }
    return 0;
}
