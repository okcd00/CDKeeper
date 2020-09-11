#define _CRT_SECURE_NO_WARNINGS
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
using namespace std;
typedef long long LL;
const LL mod = 1000000007;
map<vector<int>, int> mp;

int main() {
	int n, k;
	cin >> n >> k;
	int mm, prem;
	LL ret = 0;
	for (int i = 0; i < n; i++) {
		vector<int> a, b;
		for (int j = 0; j < k; j++) {
			scanf("%d", &mm);
			if(j) a.push_back(mm-prem);
			prem = mm;
		}
		for (int j = 0; j < k-1; j++) {
			b.push_back(-a[j]);
		}
		ret += mp[b];
		mp[a]++;
	}
	cout << ret << endl;
	return 0;
}
/*
5 3
2 11 21
19 10 1
20 11 1
6 15 24
18 27 36
*/