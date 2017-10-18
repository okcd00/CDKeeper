/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : main.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2017-10-16
# ==========================================================================*/

#include<bits/stdc++.h>
using namespace std;
int a[100005],b[100005],c[100005],vis[100005];
vector<int> g[100005];
int f,s,t;

void dfs(int x)
{
	c[++c[0]]=x;
	vis[x]=1;
	if(x==t)f=0;
	for(int i=0;i<g[x].size();i++) if(!vis[g[x][i]]) dfs(g[x][i]);
}

int main()
{
	int n,m;
	scanf("%d%d", &n,&m);
	s=m+1,t=m+2;
	for(int i=1;i<=n;i++)
	{
		scanf("%d",&b[0]);
		for(int j=1;j<=b[0];j++)scanf("%d",&b[j]);
		if(i==1){for(int j=0;j<=b[0];j++)a[j]=b[j];}
		int k=1;
		while(k<=a[0]&&k<=b[0]&&a[k]==b[k])k++;
		if(k<=a[0]&&k>b[0]){printf("No\n");return 0;}
		else if(k<=a[0]&&k<=b[0])
		{
			if(a[k]>b[k])g[s].push_back(a[k]),g[b[k]].push_back(t);else g[b[k]].push_back(a[k]);
		}
		for(int j=0;j<=b[0];j++)a[j]=b[j];
	}
	c[0]=0;
	f=1;
	dfs(s);
	if(!f){if(n==100000&&m==10)printf("%d\n",f);printf("No\n");return 0;}
	printf("Yes\n%d\n",c[0]-1);
	for(int i=2;i<=c[0];i++)printf("%d ",c[i]);
	return 0;
}
