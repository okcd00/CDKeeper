//
//  POJ 1017 Packets
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

//5*5的还能装36-25=11个1*1
//4*4的还能装36-16=20/(2*2)=5个2*2
//3*3情况如b数组
int a[10], b[4] = {0, 5, 3, 1};
int main() {
#ifdef LOCAL
	freopen("in.txt", "r", stdin);
//	freopen("out.txt","w",stdout);
#endif
	ios_base::sync_with_stdio(0);

	while(cin >> a[1]) {
		for(int i = 2; i <= 6; ++i) cin >> a[i];
		if(count(a + 1, a + 7, 0) == 6) break;

		int ans = a[4] + a[5] + a[6] + (a[3] + 3) / 4;
		int n2 = 5 * a[4] + b[a[3] % 4];
		//2*2装满需要36/4 = 9
		if(a[2] > n2)	ans += (a[2] - n2 + 8) / 9;
		int n1 = 36 * (ans - a[6]) - 25 * a[5] - 16 * a[4] - 9 * a[3] - 4 * a[2];
		if(a[1] > n1)	ans += (a[1] - n1 + 35)/36;
		cout << ans << endl;
	}
	return 0;
}
