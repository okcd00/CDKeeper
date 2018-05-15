/*==========================================================================
#   Copyright (C) 2018 All rights reserved.
#
#   filename : main.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2018-05-15
# ==========================================================================*/

#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

int main()
{
	int a[1024] = {0};
	int n; cin>>n;
	for(int i=0;i<n;i++)
		scanf("%d", &a[i]);
	sort(a, a+n);
	cout<<a[(n-1)/2]<<endl;
	return 0;
}
