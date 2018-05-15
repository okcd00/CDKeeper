/*==========================================================================
#   Copyright (C) 2018 All rights reserved.
#
#   filename : main.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2018-05-15
# ==========================================================================*/

#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

ll get_gcd(ll m, ll n)
{
    ll temp;  
    if(m<n)  
    {  
        swap(m,n);  
    }  
    while((temp=m%n)!=0)  
    {  
        m=n;  
        n=temp;  
    }  
    return n;  
}

int main()
{
	int n; cin>>n;
	ll p,q,b; 
	for(int i=0;i<n;i++)
	{
		scanf("%I64d %I64d %I64d", &p, &q, &b);
		if(p==0)
		{
			printf("Finite\n");
			continue;
		}
		q /= get_gcd(p,q);
		
		while(1) 
		{
			ll gcd = get_gcd(b,q);
			if(gcd==1) break;
			while(q%gcd==0) q/=gcd;
		}
		if (q==1) printf("Finite\n");
		else printf("Infinite\n");		
	}
	return 0;
}
