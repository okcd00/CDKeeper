/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : 1001.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2017-06-13
#   desc     : 
#   blog.csdn.net/okcd00
# ==========================================================================*/

#include<cmath>    
#include<cstdio>    
#include<string>    
#include<vector>    
#include<cstring>    
#include<iostream>    
#include<algorithm>    
using namespace std;    
typedef long long ll;    


int main()    
{    
	//freopen("./in.txt", "r", stdin);
	//freopen("./out.txt", "w", stdout);
	
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int T = 0, n = 0;    
    int b = 0;
	float c = 0.0;
	float p = 0.0, max_p = 0.0;
	
	cin >> T;
    while(T--)     
    {    
    	cin >> n;
    	p = 0.0, max_p = 0.0;
    	while(n--)
		{
    		cin>>b>>c;
    		float rest = 1. - c;
    		p = rest / (float(b) + rest);
        	max_p = p > max_p ? p : max_p;
		}
		printf("%.5f\n", max_p);
    }    
    return 0;    
} 
