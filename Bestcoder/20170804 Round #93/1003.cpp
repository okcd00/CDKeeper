/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : 1003.cpp 
#   author   : chendian / okcd00@qq.com
#   date     : 2017-08-04
#   desc     : @werkeytom's solution 
#   http://acm.hdu.edu.cn/showproblem.php?pid=6021 
#   bestcoder.hdu.edu.cn/contests/contest_chineseproblem.php?cid=750&pid=1003
# ==========================================================================*/

#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef map<ll, int> mii;

#define fo(i,a,b) for(i=a;i<=b;i++)

const int mo=1000000007;
int a[7],c[7],b[30],bz[30],f[30];
int C[30][30];
bool pd[30];
int i,j,k,l,t,n,m,top,ca,ans;
char ch;

char get(){
    char ch=getchar();
    while (ch<'a'||ch>'z') ch=getchar();
    return ch;
}

int gcd(int a,int b){
    return b?gcd(b,a%b):a;
}

int lcm(int a,int b){
    return a*b/gcd(a,b);
}

int quicksortmi(int x,int y){
    if (!y) return 1;
    int t=quicksortmi(x,y/2);
    t=(ll)t*t%mo;
    if (y%2) t=(ll)t*x%mo;
    return t;
}

void dfs(int x,int y,int z,int v){
    if (x==top+1){
        (ans+=(ll)y*f[z]%mo*v%mo)%=mo;
        return;
    }
    int i;
    fo(i,0,a[x]){
        dfs(x+1,i?lcm(y,c[x]):y,z+i,(ll)v*C[a[x]][i]%mo);
    }
}

int main(){
    C[0][0]=1;
    fo(i,1,26){
        C[i][0]=1;
        fo(j,1,i) C[i][j]=(C[i-1][j]+C[i-1][j-1])%mo;
    }
    scanf("%d",&ca);
    while (ca--){
        scanf("%d",&n);
        f[1]=1;
        fo(i,2,26){
            f[i]=quicksortmi(i,n);
            fo(j,1,i-1) (f[i]-=(ll)f[j]*C[i][j]%mo)%=mo;
        }
        fo(i,1,26){
            ch=get();
            b[i]=ch-'a'+1;
        }
        fo(i,1,26) pd[i]=bz[i]=0;
        top=0;
        fo(i,1,26)
            if (!pd[i]){
                k=b[i];
                pd[i]=1;
                t=1;
                while (k!=i){
                    t++;
                    pd[k]=1;
                    k=b[k];
                }
                if (!bz[t]){
                    bz[t]=++top;
                    c[top]=a[top]=t;
                }
                else a[bz[t]]+=t;
            }
        ans=0;
        dfs(1,1,0,1);
        (ans+=mo)%=mo;
        printf("%d\n",ans);
    }
}
