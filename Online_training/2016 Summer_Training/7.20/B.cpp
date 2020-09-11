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
vector<int> v[35];

void findBlock(int x, int &pa, int &ha) {
    for(int i = 0; i < n; ++i) {
        for(int j = 0; j < v[i].size(); ++j) {
            if(v[i][j] == x) {
                pa = i, ha = j;
                return;
            }
        }
    }
}

void moveUpBack(int p, int h) {
    for(int i = h + 1; i < v[p].size(); ++i) {
        int &b = v[p][i];
        v[b].push_back(b);
    }
    v[p].resize(h + 1);
}

void moveTo(int pa, int ha, int pb) {
    for(int i = ha; i < v[pa].size(); ++i)
        v[pb].push_back(v[pa][i]);
    v[pa].resize(ha);
}

void print() {
    for(int i = 0; i < n; ++i) {
        cout << i << ":";
        for(int j = 0; j < v[i].size(); ++j)
            cout << ' ' << v[i][j];
        cout << '\n';
    }
}

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    while(cin >> n) {
        for(int i = 0; i < n; ++i) {
            v[i].clear();
            v[i].push_back(i);
        }

        while(true) {
            string opx, opy; cin >> opx;
            int a, b, pa, pb, ha, hb;
            if(opx == "quit") break;
            cin >> a >> opy >> b;

            findBlock(a, pa, ha);
            findBlock(b, pb, hb);
            if(pa == pb) continue;
//            pr(pa); prln(ha);
//            pr(pa); prln(hb);

            if(opx == "move") moveUpBack(pa, ha);
            if(opy == "onto") moveUpBack(pb, hb);

            moveTo(pa, ha, pb);
//            print();
        }
        print();
    }
    return 0;
}
