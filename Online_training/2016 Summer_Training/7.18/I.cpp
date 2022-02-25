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

string s, t;

string trans(int x, int y, int z) {
    string ns = s;
    for(int i = 1; i <= x; ++i) {
        char c = s[4];
        s[4] = s[3]; s[3] = s[1]; s[1] = s[2];
        s[2] = c;
    }
    for(int i = 1; i <= y; ++i) {
        char c = s[4];
        s[4] = s[5]; s[5] = s[1]; s[1] = s[0];
        s[0] = c;
    }
    for(int i = 1; i <= z; ++i) {
        char c = s[3];
        s[3] = s[0]; s[0] = s[2]; s[2] = s[5];
        s[5] = c;
    }
    return ns;
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(cin >> s) {
        t = s.substr(6, 6); s.erase(6, 6);
        bool ok = false;
        for(int i = 1; i <= 4; ++i) {
            for(int j = 1; j <= 4; ++j) {
                for(int k = 1; k <= 4; ++k) {
                    string x = trans(i, j, k);
//                  cout << i << ' ' << j << ' ' << x << endl;
                    if(x == t) {
                        ok = true;
                        break;
                    }
                }
            }
            if(ok) break;
        }
        cout << (ok ? "TRUE" : "FALSE") << '\n';
    }
    return 0;
}
