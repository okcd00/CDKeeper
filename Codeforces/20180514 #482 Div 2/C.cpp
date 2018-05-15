/*==========================================================================
#   Copyright (C) 2018 All rights reserved.
#
#   filename : main.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2018-05-14
# ==========================================================================*/

#include <map>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
map<int, vector<int> > route;

int n,x,y; 
int cnt_f=0, cnt_b=0, cnt_both=0;
int vis_f[300008] = {0};
int vis_b[300008] = {0};

void bfs_f(int start, int stop)
{
	int cnt=0;
	queue<int> q;
	while(!q.empty())q.pop();
	q.push(start);
	while(!q.empty())
	{
		int node = q.front();
		q.pop();
		vis_f[node]=1;
		cnt_f++;
		for(vector<int>::iterator iter=route[node].begin(); iter!=route[node].end(); iter++)
		{
			int cur = *iter;
			if(cur==stop) continue;
			if(vis_f[cur]==1) continue;
			q.push(cur);
		}		
	}
}

void bfs_b(int start, int stop)
{
	int cnt=0;
	queue<int> q;
	while(!q.empty())q.pop();
	q.push(start);
	while(!q.empty())
	{
		int node = q.front();
		q.pop();
		vis_b[node]=1;
		cnt_b++;
		if(vis_f[node]==1) cnt_both++;
		for(vector<int>::iterator iter=route[node].begin(); iter!=route[node].end(); iter++)
		{
			int cur = *iter;
			if(cur==stop) continue;
			if(vis_b[cur]==1) continue;
			q.push(cur);
		}		
	}
}

int main()
{
	cin>>n>>x>>y;
	route.clear();
	vector<int> empty;
	for(int i=0;i<n;i++)
		route[i] = empty;
	
	for(int i=0;i<n-1;i++)
	{
		int ta, tb;
		scanf("%d %d", &ta, &tb);
		route[ta].push_back(tb);
		route[tb].push_back(ta);
	}
	
	bfs_f(x, y);
	bfs_b(y, x);
	cout<< (ll)n*(ll)(n-1)-(ll)(cnt_f-cnt_both)*(ll)(cnt_b-cnt_both) << endl;
	return 0;
}
