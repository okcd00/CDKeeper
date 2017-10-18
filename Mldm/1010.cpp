#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
#define MAXN 5000

int main()  
{  
	int n; cin>>n; 
	int array_num[MAXN];
	int total,rem=0,count,ix;
	for(ix=0;ix<MAXN;ix++)  array_num[ix]=0;      
	      
	ix=MAXN-1;              
	array_num[MAXN-1]=1;  
	  
	for(count=2;count<=n;count++)  
	{  
	    while(ix>0)  
	    {  
	        total=array_num[ix]*count+rem;  
	        rem=0;  
		    if(total>9)  
		    {  
		        array_num[ix]=total%10;  
		        rem=total/10;  
		    }  
		    else array_num[ix]=total;  
		    ix--;  
	   	}  
		rem=0;  
		total=0;  
		ix=MAXN-1;  
	}  
	  
	for(ix=0;ix<MAXN;ix++)              
	{  
	    if(array_num[ix]!=0 | count==1)  
	    {  
	      cout<<array_num[ix];  
	      count=1;
	    }  
	}  
	return 0;
}  
