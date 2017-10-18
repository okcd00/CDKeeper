#include <map>
#include <cmath>
#include <queue>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 1024

int a[MAXN];

int main()
{
	//freopen("A.txt","r",stdin);
	int n; scanf("%d",&n);
	map<int,int> cnt;
	for(int i=1;i<=n;i++)
	{
		cin>>a[i-1];
		cnt[a[i-1]]++;
	}
	sort(a,a+n);
	int l = n>>1, r = n>>1, mid = a[n>>1];
	while(l>=0 && a[l]==mid)l--;
	while(r< n && a[r]==mid)r++;
	//cout<<l<<":"<<r<<endl;
	if(l+r == n-1) cout<<mid<<endl;
	else cout<<"-1"<<endl;
	return 0;
}

