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
typedef map<ll, int> mli;

class T
{
public:
    ll count;
    mli record;
    void __init(){
    	this->count = 0;
		this->record.clear();
	}
};

typedef map<ll, T> mlt;

int main()
{
	ios::sync_with_stdio(false);
	mli a, rest;
	mlt rec;
	
	int n, k, m;
	cin>>n>>k>>m;
	
	ll tmp;
	for(int i=0;i<n;i++)
	{
		cin>>tmp;
		ll res = (tmp%m+m)%m;
		
		rest[res] += 1;	
		rec[res].count += 1;
		rec[res].record[tmp] += 1;
	}
	
	for(mlt::iterator it=rec.begin();it!=rec.end();++it)
	{
		ll c = it->first;
		T cur = it->second;
		
		if (cur.count < k) continue;
		mli r = cur.record;
		cout<<"Yes"<<endl;
		int kk=0;
		for (mli::iterator mit=r.begin(); mit!=r.end(); ++mit)
		{
			ll num = mit->first;
			int cnt = mit->second;
			// cout<<num<<"#"<<cnt<<endl;
			for(int _t=0;_t<cnt;_t++)
			{
			 	cout<<num<<" ";	
			 	kk++;
			 	if(k-kk==0) return 0;
			}
		}
	}
	cout<<"No"<<endl;
	return 0;
}
