//
//  POJ 2392 Yogurt Factory
//
//  Created by TaoSama on 2015-02-22
//  Copyright (c) 2015 TaoSama. All rights reserved.
//
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
#define CLR(x,y) memset(x, y, sizeof(x))

using namespace std;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 1e5 + 10;

struct ACM {
	int p, q;
} a[10005];
int n, s, day[10005];

int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
//	freopen("out.txt","w",stdout);
#endif
	ios_base::sync_with_stdio(0);

	while(cin >> n >> s) {
		memset(day, 0x3f, sizeof day);
		for(int i = 1; i <= n; ++i) {
			cin >> a[i].p >> a[i].q;
			for(int j = 0; j < i; ++j) {
				day[i] = min(day[i], a[i - j].p + s * j);
			}
		}
		long long ans = 0;
		for(int i = 1; i <= n; ++i) {
			ans += day[i] * a[i].q;
		}
		cout << ans << endl;
	}
	return 0;
}
