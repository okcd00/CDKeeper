#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll; 

int main()
{
    int N;  cin>>N;
    ll a[26][26];
	ll dp[26][26];
    memset(a, 0, sizeof(a[0][0]));
	memset(dp, 0, sizeof(dp[0][0]));
    for(int i=0;i<N;i++) 
    	for(int j=0;j<=i;j++)
    		cin>>a[i][j];
	
	dp[0][0]=a[0][0];
	for(int i=1;i<N;i++) 
    {
    	dp[i][0] = dp[i-1][0] + a[i][0];
    	dp[i][i] = dp[i-1][i-1] + a[i][i];
		for(int j=1;j<i;j++)
    	{
    		dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + a[i][j]; 
		}
	}
	
	ll ans = 0;
	for(int i=0;i<N;i++)
		if(dp[N-1][i]>ans) ans=dp[N-1][i];
	cout<<ans<<endl;
    return 0;
}
