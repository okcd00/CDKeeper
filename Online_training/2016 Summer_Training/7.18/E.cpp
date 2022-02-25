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

int n, m, p, q;
int whx[50005], why[50005];

void pp(vector<vector<int> >& v) {
    for(int i = 1; i < v.size(); ++i) {
        for(int j = 1; j < v[i].size(); ++j)
            cout << v[i][j] << ' ';
        cout << endl;
    }
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    int kase = 0;
    while(cin >> n >> m && (n || m)) {
        vector<vector<int> > v(n + 1, vector<int>(m + 1));
        memset(whx, 0, sizeof whx);
        memset(why, 0, sizeof why);
        for(int i = 1; i <= n; ++i)
            for(int j = 1; j <= m; ++j)
                v[i][j] = (i - 1) * m + j;

//        pp(v);
        cin >> p;
        while(p--) {
            string op; int t;
            cin >> op >> t;
            if(op == "EX") {
                int x, y, z; cin >> x >> y >> z;
                swap(v[t][x], v[y][z]);
//                cout << "EX\n";
//                pp(v);
            } else {
                vector<int> num;
                while(t--) {
                    int x; cin >> x;
                    num.push_back(x);
                }
                sort(num.begin(), num.end(), greater<int>());
                if(op == "DR") {
                    for(int i = 0; i < num.size(); ++i)
                        v.erase(v.begin() + num[i]);
//                    cout << "DR\n";
//                    pp(v);
                } else if(op == "DC") {
                    for(int i = 0; i < num.size(); ++i)
                        for(int j = 1; j < v.size(); ++j)
                            v[j].erase(v[j].begin() + num[i]);
//                    cout << "DC\n";
//                    pp(v);
                } else if(op == "IC") {
                    for(int i = 0; i < num.size(); ++i)
                        for(int j = 1; j < v.size(); ++j)
                            v[j].insert(v[j].begin() + num[i], 0);
//                    cout << "IC\n";
//                    pp(v);
                } else {
                    for(int i = 0; i < num.size(); ++i)
                        v.insert(v.begin() + num[i], vector<int>((v.begin() + 1)->size(), 0));
//                    cout << "IR\n";
//                    pp(v);
                }
            }
        }

        for(int i = 1; i < v.size(); ++i) {
            for(int j = 1; j < v[i].size(); ++j) {
                int &t = v[i][j];
                whx[t] = i; why[t] = j;
            }
        }

        cin >> q;
        if(kase) cout << '\n';
        cout << "Spreadsheet #" << ++kase << '\n';
        while(q--) {
            int x, y; cin >> x >> y;
            int t = (x - 1) * m + y;
            cout << "Cell data in (" << x << "," << y << ") ";
            if(whx[t]) cout << "moved to (" << whx[t] << "," << why[t] << ")\n";
            else cout << "GONE\n";
        }
    }
    return 0;
}
