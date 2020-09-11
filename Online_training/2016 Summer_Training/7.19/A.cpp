//
//  POJ 2376 Cleaning Shifts
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

int n, t;
struct ACM {
	int st, ed;
	bool operator<(const ACM& r) const {
		if(st != r.st) return st < r.st;
		return ed > r.ed;
	}
} a[25005];

int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
//	freopen("out.txt","w",stdout);
#endif
	//ios_base::sync_with_stdio(0);

	while(cin >> n >> t) {
		for(int i = 1; i <= n; ++i)
			cin >> a[i].st >> a[i].ed;
		sort(a + 1, a + 1 + n);

		int l = 0, r = 0, ok, idx = 1;
		int ans = 0;
		while(r < t && idx <= n) {
			if(a[idx].st > l + 1) break;
			while(a[idx].st <= l + 1 && idx <= n) {
				if(a[idx].ed > r) {
					r = a[idx].ed;
					ok = idx;
				}
				++idx;
			}
			l = a[ok].ed, ++ans;
		}
		if(r < t) ans = -1;
		cout << ans << endl;
	}
	return 0;
}
