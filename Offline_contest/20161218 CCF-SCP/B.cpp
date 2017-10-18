#include <map>
#include <cmath>
#include <queue>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 100024

int rate[8]  = {0,    3,   10,   20,    25,    30,    35,     45};
int rank[8]  = {0, 1500, 4500, 9000, 35000, 55000, 80000, 154400};
int limit[8] = {0, 1455, 4155, 7755, 27255, 41255, 57505, 100000};

//	limit[i] = limit[i-1]  \
//	+( rank[i]-rank[i-1] ) \
//	-( rank[i]-rank[i-1] ) * rate[i]/100;

int main()
{
	int t; cin>>t;
	int a = t - 3500;
	
	if(a<=0)
	{
		cout<<t<<endl; 
		return 0;
	}
	
	for(int i=1; i<8; i++)
	{
		if(a <= limit[i])
		{
			int rest = a - limit[i-1];
			// Using integer calculation to avoid float_point error
			int ret = rank[i-1] + rest*100/(100-rate[i]);
			cout<< ret + 3500 <<endl;
			return 0;
		}
	}
	
	return 0;
}

