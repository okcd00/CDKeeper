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

int getDigitSum(ll x)
{
	ll ret = 0;
	while(x)
	{
		ret += x%10;
		x/=10;
	} 
	return ret;
}

int main()
{
	ios::sync_with_stdio(false);
	ll x; cin>>x;
	int ans = 0, answer[81] = {0};
	for(int vsum=1;vsum<=81;vsum++)
	{
		ll num = x-vsum;
		if(num <= 0) continue;
		if (vsum == getDigitSum(num))
		{
			answer[ans] = num;
			ans++;
		}
	}
	cout<<ans<<endl;
	sort(answer, answer+ans);
	for(int i=0;i<ans;i++)
	{
		cout<<answer[i]<<endl;
	}
	return 0;
}

