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

const int N = 5005;
ll a[N][N] = {0};
ll m[N][N] = {0};

int main()
{
	int n; cin>>n;
	for(int i=0;i<n;i++)
	{
		scanf("%I64d", &a[0][i]);
		m[0][i]=a[0][i];
	}
		
	for(int i=1;i<n;i++)
	{
		for(int j=0;j<n-i;j++)
		{
			a[i][j] = a[i-1][j] ^ a[i-1][j+1];
		 	m[i][j] = max(a[i][j], max(m[i-1][j], m[i-1][j+1]));
		}
	}
		
	int q; cin>>q;
	int l,r;
	for(int i=0;i<q;i++)
	{
		scanf("%d %d", &l, &r);
		printf("%I64d\n", m[r-l][l-1]);
	}
	
	/*
	for(int i=1;i<n;i++)
	{
		printf("\n");
		for(int j=0;j<n-i;j++)
			printf("%d ",a[i][j]);
	}
	*/
			
	return 0;
}
