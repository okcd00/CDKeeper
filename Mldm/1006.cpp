#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
using namespace std;
 
int alen=0,blen=0;
string a,b,ans="";
 
void swap()
{
    string t=a;
    a=b; b=t;
    int tlen=alen;
    alen=blen; blen=tlen;
}
 
int main()
{
    cin>>a>>b;
    alen=a.length(), blen=b.length();
    if(alen<blen) swap();
    else if(alen==blen && a<b) swap();
    int pos=0,carry=0;
    while(pos<=alen)
    {
        int aVal=(alen-pos-1<0)?0:a[alen-pos-1]-'0',
            bVal=(blen-pos-1<0)?0:b[blen-pos-1]-'0';
        int t=aVal+bVal+carry;
        carry=0;
        if(t>9)
        {
            t=t%10;
            carry=1;
        }
        if(pos==alen)
        {
            if(t!=0) 
            ans=(char)(t+'0')+ans;  
        }
        else ans=(char)(t+'0')+ans;
        pos++;
    }
    cout<<ans<<endl;
    return 0;
}
/**************************************************************
    Problem: 1006
    User: chendian
    Language: C++
    Result: ÕýÈ·
    Time:0 ms
    Memory:1504 kb
****************************************************************/
