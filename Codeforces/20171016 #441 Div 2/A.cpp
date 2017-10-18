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

int dist[101][3]={0};

int main()
{
	ios::sync_with_stdio(false);
	int n,a,b,c;
	cin>>n>>a>>b>>c;
	dist[0][0] = 0;
	dist[0][1] = dist[0][2] = 10024;
	for(int i=1;i<n;i++)
	{
		dist[i][0] = min( dist[i-1][1] + a, dist[i-1][2] + b );
		dist[i][1] = min( dist[i-1][0] + a, dist[i-1][2] + c );
	 	dist[i][2] = min( dist[i-1][0] + b, dist[i-1][1] + c );
	 	//cout<< dist[i][0] << dist[i][1] << dist[i][2] <<endl;
	} 
	cout<< min(dist[n-1][0], min(dist[n-1][1], dist[n-1][2])) <<endl;
	return 0;
}
