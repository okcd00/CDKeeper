//
//  POJ 3040 Allowance
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

struct Coin {
	int v, c;
	bool operator<(const Coin& rhs) const {
		return v > rhs.v;
	}
} a[25];
int n, p, need[25];

int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
//	freopen("out.txt","w",stdout);
#endif
	ios_base::sync_with_stdio(0);

	while(cin >> n >> p) {
		for(int i = 1; i <= n; ++i)
			cin >> a[i].v >> a[i].c;
		sort(a + 1, a + 1 + n);
		int ans = 0;
		while(true) {
			int rest = p; 		//发一次工资
			memset(need, 0, sizeof need);
			for(int i = 1; i <= n; ++i) {   //从大到小尝试
				if(a[i].c > 0) {
					int t = min(a[i].c, rest / a[i].v);
					rest -= t * a[i].v;
					need[i] = t;
				}
				if(rest == 0) break;
			}
			if(rest > 0) {
				for(int i = n; i > 0; --i) { //用小的补齐 抑或最后大于p的
					if(a[i].c > 0 && a[i].v >= rest) {
						rest = 0;
						++need[i];
						break;
					}
				}
			}
			if(rest > 0) break;  //还剩下的说明不能了
			int add = INF;
			for(int i = 1; i <= n; ++i) //获取发工资次数
				if(need[i])
					add = min(add, a[i].c / need[i]);
			for(int i = 1; i <= n; ++i) //更新剩余硬币
				if(need[i])
					a[i].c -= add * need[i];
			ans += add;
		}
		cout << ans << endl;
	}
	return 0;
}
