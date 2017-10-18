/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : 1002.cpp 
#   author   : chendian / okcd00@qq.com
#   date     : 2017-08-04
#   desc     : @Jiedai's solution 
#   http://acm.hdu.edu.cn/showproblem.php?pid=6020 
#   bestcoder.hdu.edu.cn/contests/contest_showproblem.php?cid=750&pid=1002
# ==========================================================================*/

#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;
#define M 100005
int n,m;
char str[M];
int main(){
    int T;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&n,&m);
        scanf("%s",str+1);
        int mx[3]={0},s0=0;
        for(int i=1;i<=n;i++){
            int x=str[i]-'0';
            int now[3]={0};
            if(x==0)s0=1;
            for(int j=0;j<3;j++){
                if(mx[j]==0){
                    if(x==0)continue;
                    if(j!=0)continue;
                }
                if(mx[j]==n-m-1&&(j+x)%3!=0||mx[j]==n-m)continue;
                now[(j+x)%3]=max(now[(j+x)%3],mx[j]+1);
            }
            for(int j=0;j<3;j++)mx[j]=max(mx[j],now[j]);
//        printf("%d : %d %d %d\n",i,mx[0],mx[1],mx[2]);
        }
        if(max(s0,mx[0])>=n-m)puts("yes");
        else puts("no");
    }
    return 0;
}
