//Memory Time 
//252K   16MS 

#include<iostream>
#include<algorithm>
using namespace std;

typedef class dna
{
	public:
		int num;  //逆序数
		char sq[110];  //DNA序列
}DNAStr;

int InversionNumber(char* s,int len)
{
	int ans=0;  //s逆序数
	int A,C,G;  //各个字母出现次数，T是最大的，无需计算T出现次数
	A=C=G=0;
	for(int i=len-1;i>=0;i--)
	{
		switch(s[i])
		{
		    case 'A':A++;break;  //A是最小的，无逆序数
			case 'C':
				 {
					 C++;
					 ans+=A;  //当前C后面出现A的次数就是这个C的逆序数
					 break;
				 }
			case 'G':
				{
					G++;
					ans+=A;
					ans+=C;
					break;
				}
			case 'T':
				{
					ans+=A;
					ans+=C;
					ans+=G;
					break;
				}
		}
	}
	return ans;
}

int cmp(const void* a,const void* b)
{
	DNAStr* x=(DNAStr*)a;
	DNAStr* y=(DNAStr*)b;
	return (x->num)-(y->num);
}

int main(void)
{
	int n,m;
	while(cin>>n>>m)
	{
		DNAStr* DNA=new DNAStr[m];
		for(int i=0;i<m;i++)
		{
			cin>>DNA[i].sq;
			DNA[i].num = InversionNumber(DNA[i].sq,n);
		}
		qsort(DNA,m,sizeof(DNAStr),cmp);
		for(int j=0;j<m;j++)
			cout<<DNA[j].sq<<endl;
	}
	return 0;
}