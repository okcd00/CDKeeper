#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<set>
using namespace std;
const int inf = 1e9;
const int maxn = 100005;
set<vector<int>> S;

int main() {
	int t = 100, n;
	scanf("%d", &t);
	while (t--) {
		S.clear();
		bool flag = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			vector<int> V;
			for (int j = 0; j < 6; j++) {
				int a;
				scanf("%d", &a);
				V.push_back(a);
			}
			if (flag) continue;
			sort(V.begin(), V.end());
			if (S.find(V) != S.end()) {
				flag = 1;
			}
			S.insert(V);
		}
		if (flag) printf("YES\n");
		else printf("NO\n");
	}
	return 0;
}
/*
2
2
1 2 3 4 5 6
2 3 4 5 6 1
3
1 2 3 4 5 6
8 5 4 1 2 3
2 3 4 5 6 7
*/