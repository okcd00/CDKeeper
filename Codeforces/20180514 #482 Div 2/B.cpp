/*==========================================================================
#   Copyright (C) 2018 All rights reserved.
#
#   filename : main.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2018-05-14
# ==========================================================================*/

#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

int cnt[3][60] = {0};
int max_cnt[3] = {0};
string name[4] = {"Kuro", "Shiro", "Katie", "Draw"};

int parse_color(char c)
{
	return (int)(c-'A');
}


int main()
{
	int n; cin>>n;
	string ribbon[3];
	cin>>ribbon[0]>>ribbon[1]>>ribbon[2];
	
	int len = ribbon[0].length();
	for(int i=0;i<len;i++)
	{
		for(int j=0;j<3;j++)
		{
			int cur_color = parse_color(ribbon[j][i]);
			cnt[j][cur_color]++;
			max_cnt[j] = max(cnt[j][cur_color], max_cnt[j]);
		}
	}
	for (int j=0;j<3;j++)
	{
		if (max_cnt[j]==len && n==1)  max_cnt[j] = len-1;
		else max_cnt[j] = min(len, max_cnt[j]+n);		
	}
	
	int ans = 3;
	for (int i=0;i<3;i++)
	{
		int _ans = i;
		for (int j=0;j<3;j++)
		{
		 	if(i==j) continue;
			else if(max_cnt[i]<=max_cnt[j]) _ans = 3;	
		}
		if(_ans!=3) ans = _ans;
	}
	
	//cout<<max_cnt[0]<<"|"<<max_cnt[1]<<"|"<<max_cnt[2]<<endl;
	cout<<name[ans]<<endl;
	return 0;
}
