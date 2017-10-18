/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : main.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2017-10-16
# ==========================================================================*/

#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

int a[300033]={0};
int m[300033]={0};

int main()
{
	ios::sync_with_stdio(false);
	int n; scanf("%d", &n);
	int tmp, ans = 1, rig = n;
	
	for(int i=1;i<=n;i++)
		scanf("%d", &a[i]);
	printf("1 ");
	for(int i=1;i<=n;i++)
	{
		m[a[i]]=1;
		ans++;
		
		if (i==n)
		{
			printf("1");
			break;
		}
		
		while(m[rig]==1)
		{
			rig--;
			ans--;
		}
		printf("%d ", ans);
	}
	return 0;
}
