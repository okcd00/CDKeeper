#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

# define N 2000

int dp[N+2][N+2];
int main()
{
    int i, j, la, lb;
    char str1[N+1],str2[N+1];
    scanf("%s%s",str1,str2);
	la = strlen(str1);
	lb = strlen(str2);
	memset(dp, 0, sizeof(dp[0][0]));
	for(j=0;j<la;j++)
	{
		for(i=0;i<lb;i++)
		{
			if(str1[j]==str2[i]) dp[i+1][j+1] = dp[i][j]+1;
			else dp[i+1][j+1] = max(dp[i][j+1],dp[i+1][j]);
		}
    }
    printf("%d\n", dp[lb][la]);
    return 0;
}
