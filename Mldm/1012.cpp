#include <bits/stdc++.h>
#define maxx INT_MAX
#define minn INT_MIN
#define inf 0x3f3f3f3f
#define n 2
#define MOD 10000
using namespace std;
typedef long long ll;

ll table[45];

ll first_four(ll num)
{
     double ans=-0.5*log10(5.0)+num*1.0*log10((1+sqrt(5.0))/2.0);
     ans=ans-(ll)ans;
     double a=pow(10.0,ans);
     a=1000*a;
     return (ll)a;
}

struct Matrix
{
    ll mat[2][2];
    Matrix operator * (const Matrix & m) const{
        Matrix tmp;
        for(int i=0;i<n;i++)
            for(int j=0;j<n;j++){
                tmp.mat[i][j]=0;
                for(int k=0;k<n;k++){
                    tmp.mat[i][j]+=mat[i][k]*m.mat[k][j]%MOD;
                    tmp.mat[i][j]%=MOD;
                }
            }
        return tmp;
    }
};

Matrix POW(Matrix &m,ll k){
    Matrix ans;
    memset(ans.mat,0,sizeof(ans.mat));
    for(int i=0;i<n;i++) ans.mat[i][i]=1;
    while(k){
        if(k&1) ans=ans*m;
        k/=2;
        m=m*m;
    }
    return ans;
}

int main() 
{
    ios::sync_with_stdio(false);
	cin.tie(0);
    
    table[0]=0;
	table[1]=1;
    for(int i=2;i<=39;i++) table[i]=table[i-1]+table[i-2];
    
    ll num;
    while(cin>>num)
	{
    	cout.fill('0');
    	cout.width(4);
        if(num<=39) 
        {
            cout<<table[num]<<endl;
        }
        else
        {
            Matrix m;
            memset(m.mat,0,sizeof(m.mat));
            m.mat[0][1]=m.mat[1][1]=m.mat[1][0]=1;m.mat[0][0]=0;
            Matrix ans=POW(m,num-1);
            cout<<ans.mat[1][1]%MOD<<endl;
        }
    } 
    return 0;
}
/**************************************************************
    Problem: 1012
    User: chendian
    Language: C++
    Result: ÕýÈ·
    Time:1 ms
    Memory:1584 kb
****************************************************************/
