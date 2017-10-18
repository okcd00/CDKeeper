#include<map>
#include<cmath>
#include<queue>
#include<vector>
#include<cstdio>
#include<string>
#include<cstring>
#include<iostream>
using namespace std;
typedef long long ll;
typedef map<int,int> mii;

vector<int> followTheFootSteps(int positionOfFather, int positionOfSon, int speed, int steps)
{
	vector<int> ret = vector<int>();
	int f=1, v1=speed, v2=dis+steps*v1;
	
	int dis = positionOfFather - positionOfSon;		
	for(int i=0; i<steps && i*v1*2 <= dis+steps*v1; i++)
	{
		tv2 = dis + i * v1;
		int tf = calc_f(tv2)
		if(tf >= f)
		{
			f = tf;
			if(tv2>v2) v2 = tv2;
		}
	}
	ret.push_back(f);
	ret.push_back(v2);
	return ret;
}



int main()
{
	vector<int> ans = followTheFootSteps(1, 0, 1, 2);
	cout<<ans[0]<<" "<<ans[1]<<endl;
	return 0;
}

