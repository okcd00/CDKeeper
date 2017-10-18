#include<cmath>
#include<queue>
#include<vector>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
using namespace std;
typedef queue<int> que;

int leaveNotFound(int sizeOfApprovalLog, int numRequests, int *leaveRequests)
{
	que q; 
	int m[55] = {0};
	while(!q.empty())q.pop();
	int ret = 0, size = 0;
	for(int i=0; i<numRequests; i++)
	{
		int cur = leaveRequests[i];
		
		if(m[cur] == 0)
		{
			size++;
			//cout<< cur <<" IN"<<endl;
			if(size > sizeOfApprovalLog)
			{
				int out = q.front();
				q.pop();
				m[out] = 0;
				size--;
				//cout<< out <<" OUT"<<endl;
			}
			q.push(cur);
			m[cur] = 1;
			ret++;
		}
		else continue;
	}
	return ret;
}



int main()
{
	
	int lr[] = {2,3,1,3,2,1,4,3,2}; 
	cout<<leaveNotFound(2, 9, lr)<<endl;
	
	return 0;
}

