#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
const int maxn = 1005;
int dp1[maxn],dp2[maxn];
int a[maxn];
int n;
int main() {
	int t;
	cin >> t;
	while (t--) {
		memset(dp1, 0, sizeof(dp1));
		memset(dp2, 0, sizeof(dp2));
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
		}
		dp1[0] = dp2[n - 1] = 1;
		for (int i = 1; i < n; i++) {
			dp1[i] = 1;
			for (int j = 0; j < i; j++) {
				if (a[j] > a[i]) dp1[i] = max(dp1[i], dp1[j] + 1);
			}
		}
		for (int i = n-2; i >=0 ; i--) {
			dp2[i] = 1;
			for (int j = n-1; j > i; j--) {
				if (a[j] > a[i]) dp2[i] = max(dp2[i], dp2[j] + 1);
			}
		}
		int ret = 0;
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (a[i] != a[j]) continue;
				ret = max(ret, min(dp1[i], dp2[j]));
			}
		}
		cout << ret * 2 << endl;
	}
	return 0;
}
/*
3
9
5 4 3 2 1 2 3 4 5
5
1 2 3 4 5
14
87 70 17 12 14 86 61 51 12 90 69 89 4 65
*/