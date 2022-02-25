/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : 1001.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2017-06-13
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
const ll lim=1000000007;  //lim := vmod  
    
ll Jval[20001];  
void Jc_init() //��ʼ���׳�ֵ������    
{    
    Jval[0]=1;    
    for(int i=1;i<=20000;i++)    
    Jval[i]=(i*Jval[i-1])%lim;    
}    
    
//��Ԫ��gcd(a,b) == ax +by == d;       
struct gcdstruct //����ṹ��洢(_Ni�ļ���)  
{       
        ll d;      
        ll x;      
        ll y;      
};      

gcdstruct EXTENDED_EUCLID(ll a,ll b)  //EUCLID�㷨    
{      
    gcdstruct aa,bb;      
    if(b==0)  
    {  
        aa.d = a;      
        aa.x = 1;      
        aa.y = 0;      
        return aa;      
    }      
    else  
    {      
        bb = EXTENDED_EUCLID(b,a%b);       
        aa.d = bb.d;      
        aa.x = bb.y;      
        aa.y = bb.x - bb.y * (a/b);      
    }      
    return aa;      
}       
        
ll _Ni(ll a,ll m)  //���a��m��ģ��Ԫ    
 {      
      ll x;      
      gcdstruct aa;      
      aa = EXTENDED_EUCLID(a,m);      
      return aa.x;      
}         
    
ll C(ll n,ll m) //���C(n,m) ���������� := n!/((n-m)!*m!)  
{     
    ll  Cans=   (   Jval[n]*_Ni(Jval[m],lim) +lim   ) %lim;  // Get n!/m!   
        Cans=   (   Cans*_Ni(Jval[n-m],lim) +lim   ) %lim;      // Get Cans/(n-m)!   
    return (Cans+lim)%lim ;     
}    
  
int main()    
{    
	freopen("./in.txt", "r", stdin);
	//freopen("./out.txt", "w", stdout);
	
    ll mod = 1000000007;
    ios::sync_with_stdio(false);
    int T=0;    cin>>T;
    ll n=0, m=0;     Jc_init();     
    for(int cnt=1;cnt<=T;cnt++)     
    {    
        cin>>n>>m;
        if(n<=m) cout<<C(m,n)<<endl;    
        else cout<<C(n,m)<<endl;
    }    
    return 0;    
} 
