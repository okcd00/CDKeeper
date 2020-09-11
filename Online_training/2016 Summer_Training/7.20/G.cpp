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

map<char, string> morse;
map<string, string> dict;

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
//  freopen("out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

    char c; string s;
    while(cin >> c, c != '*') {
        cin >> s;
        morse[c] = s;
    }
    while(cin >> s, s != "*") {
        string t;
        for(auto &i : s) t += morse[i];
        dict[s] = t;
    }
    while(cin >> s, s != "*") {
        bool yes = false;
        for(auto &i : dict) {
            if(i.second == s) {
                if(!yes) {
                    yes = true;
                    cout << i.first;
                } else {
                    cout << '!';
                    break;
                }
            }
        }
        if(!yes) {
            int diff = INF;
            string ans, p, q;
            for(auto &i : dict) {
                p = s, q = i.second;
                if(p.size() < q.size()) swap(p, q);
                if(p.size() - q.size() < diff && p.substr(0, q.size()) == q) {
                    diff = p.size() - q.size();
                    ans = i.first;
                }
            }
            cout << (diff != INF ? ans : dict.begin()->first) << '?';
        }
        cout << '\n';
    }
    return 0;
}
