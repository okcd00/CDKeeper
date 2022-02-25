#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
using namespace std;
const int maxn = 10000005;
priority_queue<int> Q;
int p_lst[10] = { 6, 10, 14, 15};
char s[300005];
int dp[3][3];
int get_id(char a) {
	if (a == 'a' || a == 'b') return 0;
	if (a == 'c' || a == 'd') return 1;
	if (a == 'e' || a == 'f') return 2;
}

int main() {
	scanf("%s", s);
	int n = strlen(s);
	int ret = 0;
	for (int i = 0; i < n; i++) {
		int x = get_id(s[i]);
		if (s[i] == 'a' || s[i] == 'c' || s[i] == 'e') {
			for (int k = 0; k < 3; k++) {
				for (int j = x; j >= 0; j--) {
					dp[x][k] = max(dp[x][k], dp[j][k] + 1);
				}
			}
		}
		else {
			for (int j = 0; j < 3; j++) {
				for (int k = x; k >= 0; k--) {
					dp[j][x] = max(dp[j][x], dp[j][k] + 1);
				}
			}
		}
	}
	for (int i = 0; i < 3; i++) {
		for (int j = 0; j < 3; j++) {
			ret = max(ret, dp[i][j]);
		}
	}
	cout << ret << endl;
	return 0;
}