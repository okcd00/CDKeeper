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

int main()
{
	ll n=0; cin>>n;	
	if(n==0) cout<<0<<endl;
	else cout<<(n%2==1?(n+1)>>1:n+1)<<endl;
	return 0;
}
