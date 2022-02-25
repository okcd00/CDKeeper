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
#include<cstdio>    
#include<string>    
#include<vector>    
#include<cstring>    
#include<iostream>    
#include<algorithm>    
using namespace std;    
typedef long long ll;    


ll calc(ll k)
{
	return k * (k - 1LL) / 2LL;
}

int main()    
{    
	//freopen("./in.txt", "r", stdin);
	//freopen("./out.txt", "w", stdout);
	
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int T = 0;   
	ll n = 0, m = 0;
	
	cin >> T;
    while(T--)     
    {    
    	cin >> n >> m;
    	ll ans = 0LL;
    	if (n == 1)
    		cout<< 0 <<endl;    		
		else if (n == 2)
			cout<< m%2 <<endl;
		else if (n/2 <= m)
			cout << calc(n) << endl;		
		else		
			cout << calc(n) - calc(n-m*2LL) << endl;
    }    
    return 0;    
} 
