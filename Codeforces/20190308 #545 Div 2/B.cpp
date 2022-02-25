#include<bits/stdc++.h>
using namespace std;
const int maxn=1005;
int a[maxn][maxn],b[maxn][maxn],t[maxn][maxn],len1[maxn],len2[maxn];
int main()
{
    int n,m;scanf("%d%d",&n,&m);
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
            scanf("%d",&t[i][j]);
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
            a[i][++len1[i]]=t[i][j];
        sort(a[i]+1,a[i]+m+1);
        len1[i]=unique(a[i]+1,a[i]+m+1)-a[i]-1;
    }
    for(int j=1;j<=m;j++)
    {
        for(int i=1;i<=n;i++)
            b[j][++len2[j]]=t[i][j];
        sort(b[j]+1,b[j]+n+1);
        len2[j]=unique(b[j]+1,b[j]+n+1)-b[j]-1;
    }
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=m;j++)
        {
            int v1=upper_bound(a[i]+1,a[i]+len1[i]+1,t[i][j])-a[i]-1;
            int v2=upper_bound(b[j]+1,b[j]+len2[j]+1,t[i][j])-b[j]-1;
            //cout<<i<<" "<<j<<" "<<v1<<" "<<v2<<endl;
            int mx=0;
            if(v1>v2) mx=v1+len2[j]-v2;
            else mx=v2+len1[i]-v1;
            mx=max(mx,max(len1[i],len2[j]));
            printf("%d ",mx);
        }
        printf("\n");
    }
}