#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
#include<queue>
using namespace std;
typedef long long LL;
const LL mod = 1000000007;
LL dp[55][55];
bool vis[55][55];
void f(int n, int m) {
	vis[n][m] = 1;
	if (m == 0) {
		if (n) {
			dp[n][m] = 0;
		}
		else dp[n][m] = 1;
		return;
	}
	if (n <= 1) {
		dp[n][m] = 1;
		return;
	}
	dp[n][m] = 0;
	for (int i = 0; i < n; i++) {
		if (!vis[i][m - 1]) {
			f(i, m - 1);
		}
		if (!vis[n - 1 - i][m - 1]) f(n - 1 - i, m - 1);
		dp[n][m] = (dp[n][m] + dp[i][m - 1] * dp[n - 1 - i][m - 1]) % mod;
	}
}
int main() {
	int n, m;
	cin >> n >> m;
	f(n, m);
	cout << dp[n][m]<<endl;
	return 0;
}