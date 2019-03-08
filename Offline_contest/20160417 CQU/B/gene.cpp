//
//  Created by TaoSama on 2015-11-17
//  Copyright (c) 2015 TaoSama. All rights reserved.
//
//#pragma comment(linker, "/STACK:1024000000,1024000000")
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
#include <ctime>
#include <random>

using namespace std;
#define pr(x) cout << #x << " = " << x << "  "
#define prln(x) cout << #x << " = " << x << endl
const int N = 1e5 + 10, INF = 0x3f3f3f3f, MOD = 1e9 + 7;

int rand32(){
	return (rand() << 16) + rand();
}

int rand8(){
	return rand() >> 8;
}

int main() {
#ifdef LOCAL
    freopen("C:\\Users\\TaoSama\\Desktop\\in.txt", "r", stdin);
//  freopen("C:\\Users\\TaoSama\\Desktop\\out.txt","w",stdout);
#endif
    ios_base::sync_with_stdio(0);

	int n = 1e3;
	unsigned int M = UINT_MAX;
	default_random_engine gene;
	uniform_int_distribution<long long> d;
	cout << n << '\n';
	cout << M << '\n';
	for(int i = 1; i < n; ++i)
		cout << d(gene) << '\n';
    return 0;
}
