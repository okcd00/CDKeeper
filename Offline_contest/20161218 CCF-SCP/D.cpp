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
#define MP(a,b) make_pair(a,b)
typedef pair<int, int> pii;
typedef map<pii, int> mpi;

int t[MAXN];
inline int lowbit(int x){return x&-x;}

int getSum(int l, int r)
{
	int ret = 0;
	for(int i=l;i<=r;i++)
	{
		ret+=t[i];
	//	cout<< t[i];
	}
	return ret;
}

int main()
{
	freopen("D.txt","r",stdin);
	int n; cin>>n;
	int i,j,k;
	mpi opt;
	for(i=0;i<n;i++)
	{
		cin>>t[i];
		opt[MP(i,i)]=t[i];
		if(i!=0) opt[MP(i-1,i)]=t[i]+t[i-1];
	}
	//cout<<endl;
	for(i=2;i<n;i++) //Step
	{
		int ret = 0x7FFFFFFF;
		for(j=i;j<n;j++) //StartPoint
		{
			for(k=0;k<i;k++) //SplitPoint
			{
				ret = min(
					ret,
					opt[MP(j-i,j-i+k)] + opt[MP(j-i+k,j)] + getSum(j-i,j)
				);
			//	cout<<"@"<<opt[MP(j-i,j-i+k-1)]<<":"<<opt[MP(j-i+k,j)]<<":"<<getSum(j-i,j)<<endl;
			}
			opt[MP(j-i,j)] = ret;
			//cout<<j-i<<","<<j-i+k-1<<","<<opt[MP(j-i,j-i+k)]<<":"<<j-i+k<<","<<j<<":"<<ret<<endl;
		}
	}
	cout<<opt[MP(0,n-1)];
	return 0;
}

