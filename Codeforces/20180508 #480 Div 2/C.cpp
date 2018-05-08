#include <map>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;

int key[300] = {0};

int main()
{
	//ios::sync_with_stdio(false);
	memset(key, 0, sizeof(key[0]));
	int i,j;
	int n=0, k=0, p=0, ans=0;
	cin>>n>>k;

	for(i=0;i<300;i++)
	{
		key[i] = -1;
	}
	
	for(i=0; i<n; i++)
	{
		scanf("%d", &p);
		if(key[p] != -1)
		{
		    ans = key[p];
		}
		else
		{
			int cur_key = 0;
			for(j=max(k,0);j>=0;j--)
			{
				int cur_pos = max(p-j+1, 0);
				if(key[cur_pos] != -1)
				{
					int kval = key[cur_pos], kpos = cur_pos;
					if(kpos-kval == k-1) continue;
					else if(p-kval < k)
					{
						cur_key = kval;
						break;
					}
				}
				else
				{
					cur_key = cur_pos;
					break;
				}
			}
			ans = max(cur_key, 0);
			for(j=ans; j<=p; j++)
			{
				//cout<<"Marked "<<j<<" as "<<ans[i]<<endl;
				key[j] = ans;
			}
		}
		cout<<ans<<" ";
	}
	return 0;
}
