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

int n, m;
int bomb[128][128] = {0};
int field[128][128] = {0};

void set_effects(int x, int y)
{
	bomb[x][y] = 1;
	for(int i=-1;i<=1;i++)
	{
		for(int j=-1;j<=1;j++)
		{
			if(x+i>=n or x+i<0) continue; 
			if(y+j>=m or y+j<0) continue;
			if(i==0 and j==0) continue;
			field[x+i][y+j]--;
		}
	}
}

int main()
{
	char c;
	cin>>n>>m;
	memset(bomb, 0, sizeof(bomb[0][0]));
	memset(field, 0, sizeof(field[0][0]));
	for(int i=0;i<n;i++)
	{
		scanf("%c", &c);
		for(int j=0;j<m;j++)
		{
			scanf("%c", &c);
			//cout<<c-'0'<<endl;
			if (c=='*') set_effects(i,j);
			if (c-'0'>=0 && c-'0'<=8) field[i][j] += (c-'0');
		}
	}
	string ans = "YES";
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
		{
			if(field[i][j]!=0 and bomb[i][j]==0)
			{
				//cout<<i<<"|"<<j<<endl;
				ans = "NO";
				break;
			}
		}
		if(ans == "NO") break;
	}
	cout<<ans<<endl;
	return 0;
}
