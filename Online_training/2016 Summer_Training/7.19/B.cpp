//
//  POJ 1328 Radar Installation
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

struct Seg {
	double l, r;
	bool operator<(const Seg& s) const {
		return l < s.l;
	}
} a[1005];
int n, kase, d;

int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
//	freopen("out.txt","w",stdout);
#endif
	ios_base::sync_with_stdio(0);

	while(cin >> n >> d && n && d) {
		bool ok = true;
		for(int i = 1; i <= n; ++i) {
			int x, y; cin >> x >> y;
			double t = sqrt(d * d - y * y);
			a[i].l = x - t; a[i].r = x + t;
			if(y > d) ok = false;
		}
		int ans = -1;
		if(ok) {
			sort(a + 1, a + 1 + n);
			ans = 1;
			Seg t = a[1];
			for(int i = 2; i <= n; ++i) {
				if(t.r > a[i].r)
					t = a[i];
				else if(t.r < a[i].l) {
					++ ans;
					t = a[i];
				}
			}
		}
		cout << "Case " << ++kase << ": " << ans << endl;
	}
	return 0;
}
