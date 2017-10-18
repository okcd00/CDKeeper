/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : 1006.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2017-06-13
#   desc     : 
#   blog.csdn.net/okcd00
# ==========================================================================*/

#include<map>
#include<cmath>    
#include<cstdio>    
#include<string>    
#include<vector>    
#include<cstring>    
#include<iostream>    
#include<algorithm>    
using namespace std;    
typedef long long ll;    
typedef map<int, int> mii;

template<class T> inline void UPDMAX(T &x, const T y){ if(x<y)x=y; }
template<class T1, class T2> inline pair<T1, T2> MP(const T1 &x, const T2 &y){ return make_pair(x, y); }

template<class T> struct SEG
{

	T lef, rig;
	T data;
	
	void __init(){
		this->data = this->rig - this->lef + 1;
	}


	SEG(){ 
		this->lef=this->rig=-1;
		__init();
	}
	SEG(const ll _l, const ll _r){
		this->lef=_l;
		this->rig=_r;
		__init();
	}
};

int main()    
{    
    ios::sync_with_stdio(false);
    ll n=0, m=0;
	while(scanf("%lld%lld",&n,&m)!=EOF)
	{
		mii inp;
		vector< SEG<ll> > rec;
		ll maxlen=0LL;
		inp.clear();
		rec.clear();
		ll l=-1, r=-1;
		for(int i=0;i<n;i++)
		{
			ll lef, rig;
			cin>>lef>>rig;
			UPDMAX(maxlen, rig-lef);
			if (lef>l or l==-1)
			{
	            if(l!=-1 and r!=-1)
	            {
	            	rec.push_back(SEG<ll>(l,r));
	            	//cout<<"PUSH "<<l<<":"<<r<<endl;
				}
				l = lef;
				r = rig;
			}
			else if(l<=lef and r>=rig) continue;
			else if(l<=lef and r<rig)
			{
				r = rig;
			}
		}
		rec.push_back(SEG<ll>(l,r));
		
		int rec_size = rec.size();
	    ll *dp_len, *dp_ticket;
		dp_len = (ll*)malloc(sizeof(ll) * rec_size);
		dp_ticket = (ll*)malloc(sizeof(ll) * rec_size);
		int idx = 0;
		SEG<ll> last = SEG<ll>();
		for(vector< SEG<ll> >::iterator vit=rec.begin();vit!=rec.end();++vit)
		{
			SEG<ll> cur = (*vit);
			if(idx>0)
			{
				ll dist = cur.lef - last.rig - 1;
			    dp_len[idx] = dp_len[idx-1] + dist + cur.data;
			    dp_ticket[idx] = dp_ticket[idx-1] + dist;
		    } 
		    else
			{
				dp_len[idx] = cur.data;
				dp_ticket[idx] = 0LL;
			}
		    idx++;
		}
		for(int i=0;i<rec_size;i++) cout<<dp_len[i]<<endl;
		for(int i=0;i<rec_size;i++) cout<<dp_ticket[i]<<endl;
		
	}    
    return 0;    
} 

