/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : main.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2018-05-08
# ==========================================================================*/

#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

int grid[100][200]={0};

int main()
{
	ios::sync_with_stdio(false);
	int r=4, n=0, k=0;
	cin>>n>>k;
	memset(grid, 0, sizeof(grid[0]));
	int mid = n / 2; 
	int cnt = k / 2;
	int res = k % 2;
	grid[1][mid] = (res==1?1:0);
	for(int i=1;i<=cnt;i++)
	{
		if(mid-i>0)
		{
			grid[1][mid-i] = 1;
			grid[1][mid+i] = 1;	
		}
		else if(mid-i+k-3>0)
		{
			int d = i-k+3;
			grid[2][mid-d] = 1;
			grid[2][mid+d] = 1;	
		}
		else
		{
			grid[2][mid] = 1;
		}
	}
	cout<<"YES"<<endl;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<n;j++)
		{
			printf(grid[i][j]==1?"#":".");
		}
		cout<<endl;
	}
	return 0;
}
