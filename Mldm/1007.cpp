#include <cstdio>
#include <string>
#include <memory>
#include <cstring>
#include <iostream>
using namespace std;
typedef long long ll;

#define N 1000010

ll ans;
int a[N];

void merge(int s1,int e1,int s2,int e2)
{
    int p1,p2,p;
    int* temp = new int[e2-s1+5];
    p=0;p1=s1;p2=s2;
    while(p1<=e1&&p2<=e2)
    {
        if(a[p1]<=a[p2])
        {
            temp[p++]=a[p1++];
            continue;
        }
        else 
        {
            temp[p++]=a[p2++];
            ans+=e1-p1+1;
            continue;
        }
    }
    while(p1<=e1) temp[p++]=a[p1++];
    while(p2<=e2) temp[p++]=a[p2++];
    int i;
    for(i=s1;i<=e2;i++) a[i]=temp[i-s1];
    delete temp;
}

void merge_sort(int s,int e)
{
    int m;
    if(s<e)
    {
        m=(s+e)/2;
        merge_sort(s,m);
        merge_sort(m+1,e);
        merge(s,m,m+1,e);
    }
}

int main()
{
    int test;
    int n,i;
    ans=0;
    scanf("%d",&n);
    for(i=0;i<n;i++)
        scanf("%d",&a[i]);
    merge_sort(0,n-1);
    printf("%lld\n",ans);
    return 0;
}
