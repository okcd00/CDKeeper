#include <map>
#include <queue>
#include <vector>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
 
 
int main()
{
	int n, t = 0;
	scanf("%d", &n);
	
	int ret = 0;
	int last_t = 0, last_cnt = 0, cur_cnt = 0;
	for(int i=0; i<=n; i++)
	{
		if(i==n)
			t = 0;
		else
			scanf("%d", &t);	
 
		if(t==last_t)
		{
			cur_cnt += 1;
		}
		else
		{
			ret = max(ret, min(cur_cnt, last_cnt));
			last_cnt = cur_cnt;
			cur_cnt = 1;
			last_t = t;
		}
	} 
	printf("%d", ret*2);
	return 0;
}