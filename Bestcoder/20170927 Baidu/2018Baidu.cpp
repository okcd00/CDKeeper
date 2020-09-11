#include<cmath>
#include<queue>
#include<vector>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
using namespace std;
typedef long long ll;

class T
{
public:
	ll value;
	int n;
	int a_idx;
	T(ll a, int b, int c):value(a),n(b),a_idx(c){}
};

bool operator > (const T &t1, const T &t2) 
{
     return t1.value > t2.value;
} 

ll calc(ll* a, int n)
{
	ll ret = 0LL;
	for(int i=0;i<8;i++)
		ret += a[i] * pow(ll(n), ll(7-i));
	return ret;
}

int main()
{
	freopen("./in.txt", "r", stdin);
	ll a[10001][8]={0};
	
	priority_queue<T, vector<T>, greater<T> > q;
	while(!q.empty()) q.pop();
	
	int n; scanf("%d", &n);
	for(int i=0; i<n; i++)
	{
		for(int j=0; j<8; j++)
			scanf("%lld", &a[i][j]);
		q.push(T(calc(a[i], 1), 1, i));
		//cout<<q.top().value<<endl;
	}
	int k; scanf("%d", &k);
	ll ret = 0LL;
	for(int i=0; i<k; i++)
	{
		T cur = q.top();
		q.pop();
		int _n = cur.n;
		int _i = cur.a_idx;
		ret = cur.value;
		
		T inp = T( calc(a[_i], _n+1), _n+1, _i );
		q.push(inp);
	}
	cout<<ret<<endl;
	
	fclose(stdin);
	return 0;
}

