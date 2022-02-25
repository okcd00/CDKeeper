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

string x, s, t;
int cntx[30], cnty[30];

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(getline(cin, x)) {
        s.clear(); t.clear();
        memset(cntx, 0, sizeof cntx);
        memset(cnty, 0, sizeof cnty);
        for(int i = 0; i < x.size(); ++i)
            if(isupper(x[i])) s += x[i], ++cntx[x[i] - 'A'];
        getline(cin, x);
        for(int i = 0; i < x.size(); ++i)
            if(isupper(x[i])) t += x[i], ++cnty[x[i] - 'A'];

//      pr(s); prln(t);

//        sort(s.begin(), s.end());
//        sort(t.begin(), t.end());

        sort(cntx, cntx + 26);
        sort(cnty, cnty + 26);

//        pr(s); prln(t);

        bool ok = false;
        if(s.size() == t.size()) {
            ok = true;
            for(int i = 25; i; --i) {
//              pr(cntx[i]); prln(cnty[i]);
                if(cntx[i] && cntx[i] != cnty[i]) {
                    ok = false;
                    break;
                }
            }
        }
        cout << (ok ? "YES" : "NO") << '\n';
    }
    return 0;
}