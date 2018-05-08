#include<iostream>
#include<string>
#include<cstdio>
#include<cstring>
using namespace std; 

	short a[2][5001]; 
	string s; 
int main() 
{ 
	int n; 
	int i,j,p; 
	while(cin>>n) 
	{
		getchar();
		cin>>s;
		memset(a,0,sizeof(a));
	for(i=1;i<=s.size();i++)
	{
		p=1;
	for(j=s.size();j>=1;j--,p++) 
	{ 
		if(s[i-1]==s[j-1]) a[i%2][p]=a[(i-1)%2][p-1]+1;
		else { 
			if(a[i%2][p-1]>=a[(i-1)%2][p]) a[i%2][p]=a[i%2][p-1]; 
			else a[i%2][p]=a[(i-1)%2][p]; 
			 } 
	} 
	} 
	cout<<n-a[n%2][n]<<endl; 
	}
	return 0;
}