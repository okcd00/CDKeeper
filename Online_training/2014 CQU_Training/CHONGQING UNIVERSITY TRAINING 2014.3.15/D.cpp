#include <iostream>
#include <cstdio>
#include <algorithm>
//�����ᣡ strlen�������ĸ�ͷ�ļ������� 
/*
#include <string>
#include <string.h>
#include <cstring>
*/

//���������ж���  1st Up 
//...�������ж��Ƿ����ȫ���ĵ������� 2nd Up 
//���س���ӣ� 3rd Up 
#include <stack>
using namespace std;
/* 
int main()
{
    char st[100001];
    cin>>st;
    int len = strlen(st);
    if (len%2) {
                       cout<<"No";
                       return 0;
               }
    char c1,c2;
    for(int i=0;i<len/2;i++)
    {
            c1=st[i];
            c2=st[len-1-i];
     if(c1!=c2){
                       cout<<"No";
                       return 0;
               }
     else continue;
    }
    cout<<"Yes";
    return 0;
}
*/


char tmp;
stack<char> s;

void solve()
{
	while (scanf("%c", &tmp) != EOF && tmp!='\n') //�ӣ� 
    {
		if (s.empty())
			s.push(tmp);
		else {
			char t = s.top();
			if (t == tmp)
				s.pop();
			else
				s.push(tmp);
		     }
	}
}

int main() 
{
    solve();
	if (s.size())
		cout<<"No";
	else
		cout<<"Yes";
	return 0;
}
