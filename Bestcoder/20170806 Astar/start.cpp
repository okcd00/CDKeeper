/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : xxxx.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2088-88-88
#   desc     : 
#   blog.csdn.net/okcd00
# ==========================================================================*/

#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 100

int main()
{
	ios::sync_with_stdio(false);
	MATX<int> a = MATX<int>(3,3);
	a.set_one();
	a(1LL, 1LL) = 3;
	a = a * a.pow(3LL);
	a.show();
	return 0;	
} 
