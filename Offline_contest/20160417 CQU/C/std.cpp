//
//  Created by TaoSama on 2015-11-17
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

bool check(int x) {
    if(x % 36) return false; //bad, can't be divided by 36
    char s[100]; sprintf(s, "%d", x);
    int n = strlen(s);
    bool ok = false;
    for(int i = 0; i < n; ++i) {
        if(s[i] == '6') return false; //bad, single 6
        if(s[i] == '3') {
            if(i + 1 < n && s[i + 1] == '6') {
                ++i;
                ok = true; //ok, 36
            } else return false; //bad, single 3
        }
    }
    return ok; //maybe good
}

int main() {
    vector<int> all;
    for(int i = 1; i <= 1e5; ++i) {
        if(!check(i)) continue;
        all.push_back(i);
    }
    int t; scanf("%d", &t);
    while(t--) {
        int l; scanf("%d", &l);
        auto iter = lower_bound(all.begin(), all.end(), l);
        if(iter != all.end()) printf("%d\n", *iter);
        else puts("-1");
    }
    return 0;
}
