/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : 1001.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2017-08-04
#   desc     : Basic hash map
#   http://acm.hdu.edu.cn/showproblem.php?pid=6019 
#   bestcoder.hdu.edu.cn/contests/contest_chineseproblem.php?cid=750&pid=1001
# ==========================================================================*/

#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef map<ll, int> mii;

int main()
{
	int T; cin>>T;
	mii rec;
	for(int ti=0; ti<T; ti++)
	{
		int n, cnt; 
		cnt = 0;
		cin >> n; 
		rec.clear();
		for(int ni=0; ni<n; ni++)
		{
			ll c; scanf("%lld", &c);
			if(rec[c]!=1) rec[c]=1;
			else {
				cnt++;
				rec.clear();
				rec[c]=1; // Important
			}
		}
		printf("%d\n", cnt+1);
	}
	return 0;	
} 
