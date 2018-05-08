/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : main.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2018-05-08
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
	ios::sync_with_stdio(false);
	int l=0, p=0;
	string necklace;
	cin>>necklace;
	for(int i=0;i<necklace.length();i++)
	{
		(necklace[i]=='o'?p:l)++;
	}
	cout<<((p==0 or l%p==0)?"YES":"NO")<<endl;
	return 0;
}
