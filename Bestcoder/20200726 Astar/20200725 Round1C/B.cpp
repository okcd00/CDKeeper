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


int main()    
{    
	//freopen("./in.txt", "r", stdin);
	//freopen("./out.txt", "w", stdout);
	
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    
    int T = 0;   
	float p = 0.0;
	
	cin >> T;
    while(T--)     
    {    
    	cin >> p;
    	if (p > 1.0){
    		cout<<"No"<<endl;
			continue; 
		}
		// 0.5 * E(more) + 0.5 * E(less) = 0.75  X
		//bool flag = p < 0.75;
		
    	float e_bob = (2.0 * p) * 0.5 + (p / 2.0) * 0.5;
    	// 2p * P(a-less|a=p) + p * P(a-more|a=p)
		cout << (e_bob > p ? "Yes" : "No") << endl;
    }    
    return 0;    
} 
