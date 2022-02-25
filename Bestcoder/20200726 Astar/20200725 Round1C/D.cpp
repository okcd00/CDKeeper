/*==========================================================================
#   Copyright (C) 2020 All rights reserved.
#
#   filename : 1002.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2020-07-26
#   desc     : 
#   blog.csdn.net/okcd00
# ==========================================================================*/

#include<cmath>   
#include<queue> 
#include<cstdio>    
#include<string>    
#include<vector>    
#include<cstring>    
#include<iostream>    
#include<algorithm>    
using namespace std;    
typedef long long ll;    

int T = 0, time = 0;   
int n = 0, x = 0, y = 0;
priority_queue<int> lef, rig;

int corner_r = 0, corner_l1 = 0;
int corner_l2 = 0, corner_l3 = 0;


int pass_corner(int l, int r)
{
	time += 1;
	if(corner_r) corner_r = 0;  //out
	if(corner_l3) corner_l3 = 0;  //out
	if(corner_l2)
	{
		// l2 -> l3
		corner_l3 = 1;
		corner_l2 = 0; 
	}
	if (r)
	{
		// r -> cr
		corner_r = 1;
		if(corner_l1) 
		{
			// l1 -> l2
			corner_l2 = 1;
			corner_l1 = 0; 
		}
		if(l) 
		{
			corner_l1 = 1;  //in
			if (!lef.empty()) lef.pop();
		}
		if (!rig.empty()) rig.pop();
	}
	else  // no r
	{
		if(corner_l1) 
		{
			// l1 -> r
			corner_r = 1;
			corner_l1 = 0; 
		}
		if(l)
		{
			corner_l1 = 1;  //in
			if (!lef.empty()) lef.pop();
		}
	}
	
	//cout<<time<<"  [PASS]: "<<l<<" "<<r<<endl;
	//cout<<corner_l2 << corner_l3 <<endl;
	//cout<<corner_l1 << corner_r <<endl;
	return 0;
}

int standby(int pos)
{
	return pos == time + 1;
}

int main()    
{    
	//freopen("./in.txt", "r", stdin);
	//freopen("./out.txt", "w", stdout);
	
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
	
	cin >> T;
    while(T--)     
    {    
    	while(!lef.empty()) lef.pop();
    	while(!rig.empty()) rig.pop();
    	time = 0;
    	cin >> n;
    	for(int i=0; i<n; i++)
    	{
    		cin>>x>>y;
    		if(x==1)
    			rig.push(y);
    		else if (x==2)
    			lef.push(y);			
		}
		while(!lef.empty() or !rig.empty())
		{
			int l_front = lef.empty()?0:lef.top();
			int r_front = rig.empty()?0:rig.top();
			// cout<< l_front <<"\t"<< r_front <<endl;
			if (!standby(l_front) and !standby(r_front))
			{
				time += min(l_front, r_front);
				continue;	
			}
			int stb_l = standby(l_front)?1:0;
			int stb_r = standby(r_front)?1:0;
			pass_corner(stb_l, stb_r);	
		}	
		while(corner_r + corner_l1 + corner_l2 + corner_l3)
		{
			pass_corner(0, 0);
		}	
			
		cout << time << endl; 
    }    
    return 0;    
} 
