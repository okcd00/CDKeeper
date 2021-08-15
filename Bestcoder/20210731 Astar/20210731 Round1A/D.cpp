/*==========================================================================
#   Copyright (C) 2020 All rights reserved.
#
#   filename : 1004.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2021-07-31
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

/*
给定两个正整数 a, b，求最小和最大的 c 
满足 a mod c = b mod c，满足 c-1 为正整数，且 c ≤ max(a,b)
其中的 mod 表示取模运算。
*/

int main()
{
    int T;
	cin >> T;
    while(T--)
	{
        ll a, b;
        cin >> a >> b;
        if(a==b && a!=1)
		{
            cout<<2<<" "<<a<<endl;
            continue;
        }
        if(a==b && a==1)
		{
            cout<<-1<<" "<<-1<<endl;
            continue;
        }
        ll d = abs(a-b);
        if(d==1) 
		{
            cout<<-1<<" "<<-1<<endl;
            continue;
        }
        ll ans1 = d, ans2 = d;
        for(int i=2; i<=d/i; i++)
		{
            if(d%i == 0)
			{
                ans1 = i;
                break; 
            }
        }
        cout<<ans1<<" "<<ans2<<endl;
    }
    return 0;
} 
