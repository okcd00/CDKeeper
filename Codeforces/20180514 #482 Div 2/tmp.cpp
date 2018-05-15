/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
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

int parse_color(char c)
{
	return (int)(c-'A');
}

int main()
{
	string s;
	cin>>s;
	cout<<parse_color(s[0])<<endl;
	return 0;
}
