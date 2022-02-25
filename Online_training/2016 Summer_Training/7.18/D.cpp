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

string s, t, x;
int cur, sz;
vector<char> code[N];

bool readMore(int& cur) {
    if(!sz) {
        for(int i = 1; i <= 3; ++i) {
            int x = cin.get();
            if(x == ' ' || x == '\n') {
                --i;
                continue;
            }
            sz = (sz << 1) + x - '0';
        }
        if(!sz) return false;
    }

    cur = 0;
    for(int i = 1; i <= sz; ++i) {
        int x = cin.get();
        if(x == ' ' || x == '\n') {
            --i;
            continue;
        }
        cur = (cur << 1) + x - '0';
    }
    if(cur == (1 << sz) - 1) sz = 0;
    return true;
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(getline(cin, s)) {
        while(s.empty()) getline(cin, s);
//      cout << s << endl;
        for(int i = 0, j = 0, k = 0; i < s.size(); ++i) {
            if(code[j].size() == (1 << j) - 1) code[++j].clear();
            code[j].push_back(s[i]);
        }

        sz = 0;
        while(readMore(cur)) {
            if(sz) {
//              pr(sz); prln(cur);
                cout << code[sz][cur];
            }
        }
        cin.get();
        cout << '\n';
    }
    return 0;
}
