#include <queue>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;
typedef long long ll;
#define maxn 1280000

//string num[maxn];

//int judge(string a,string b)
//{
//	if(a.length()!=b.length()) return a.length()-b.length();
//	else if(a>b) return 1;
//	else if(a<b) return -1;
//	else return 0;
//}

int main()
{
	priority_queue<ll> pq;
	while(!pq.empty()) pq.pop();
	int m,k;	cin>>m>>k;
	ll t=0,Vlast;
	for(int i=0;i<m;i++)
	{
		cin>>t;
		if(i<k) pq.push(-t);
		else 
		{
			Vlast=pq.top();
			if(Vlast>-t)
			{
				pq.pop();
				pq.push(-t);
			}
		}
	} 
	cout<<-pq.top()<<endl;
	return 0;
}
/**************************************************************
	Problem: 1005
	User: chendian
	Language: C++
	Result: ÕýÈ·
	Time:73 ms
	Memory:1692 kb
****************************************************************/

