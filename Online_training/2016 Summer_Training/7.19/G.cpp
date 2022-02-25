//
//  POJ 1862 Stripies
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

int n;

int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
//	freopen("out.txt","w",stdout);
#endif
	ios_base::sync_with_stdio(0);

	while(cin >> n) {
		priority_queue<double> pq;
		for(int i = 1; i <= n; ++i) {
			double x; cin >> x;
			pq.push(x);
		}
		while(pq.size() > 1) {
			double x = pq.top(); pq.pop();
			x *= pq.top(); pq.pop();
			pq.push(2 * sqrt(x));
		}
		cout << fixed << setprecision(3) << pq.top() << endl;
	}
	return 0;
}
