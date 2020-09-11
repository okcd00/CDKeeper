//
//  POJ 3190 Stall Reservations
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

struct Cow {
	int l, r, id;
	bool operator<(const Cow& rhs) const {
		return r > rhs.r;
	}
} a[50005];
bool cmp(Cow x, Cow y) {
	return x.l < y.l;
}
int n, stall[50005];

int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
//	freopen("out.txt","w",stdout);
#endif
	ios_base::sync_with_stdio(0);

	while(cin >> n) {
		priority_queue<Cow> pq;
		memset(stall, 0, sizeof stall);
		for(int i = 1; i <= n; ++i) {
			cin >> a[i].l >> a[i].r;
			a[i].id = i;
		}
		sort(a + 1, a + 1 + n, cmp);
		int ans = 1;
		stall[a[1].id] = 1; pq.push(a[1]);
		for(int i = 2; i <= n; ++i) {
			Cow t = pq.top();
			if(a[i].l > t.r) {
				stall[a[i].id] = stall[t.id];
				pq.pop();
			} else	stall[a[i].id] = ++ans;
			pq.push(a[i]);
		}
		cout << ans << endl;
		for(int i = 1; i <= n; ++i)
			cout << stall[i] << endl;
	}
	return 0;
}

/*
//用set维护
int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
//	freopen("out.txt","w",stdout);
#endif
	ios_base::sync_with_stdio(0);

	while(cin >> n) {
		multiset<Cow> s;
		memset(stall, 0, sizeof stall);
		for(int i = 1; i <= n; ++i) {
			cin >> a[i].l >> a[i].r;
			a[i].id = i;
		}
		sort(a + 1, a + 1 + n, cmp);
		int ans = 1;
		stall[a[1].id] = 1; s.insert(a[1]);
		for(int i = 2; i <= n; i++) {
			Cow t = *s.begin();
			if(a[i].l > t.r) {
				s.erase(s.begin());
				stall[a[i].id] = stall[t.id];
			} else stall[a[i].id] = ++ans;
			s.insert(a[i]);
		}
		cout << ans << endl;
		for(int i = 1; i <= n; ++i)
			cout << stall[i] << endl;
	}
	return 0;
}
*/
