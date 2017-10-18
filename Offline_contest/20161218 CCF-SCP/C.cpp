#include <map>
#include <cmath>
#include <queue>
#include <cstdio>
#include <string>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

// Define Un-leveled is -1; level +1; Ignored 0;
typedef pair<string, string> pss;
typedef map<string, int> psi;
typedef map<pss, int> mpi;

mpi ra; //roleAuthor;
mpi ua; //userAuthor;

#define MAXN 233
#define MP(a,b) make_pair(a,b)

void update(string user, string role, string cate)
{
	int original_level = ua[make_pair(user, cate)];
	int current_level = ra[make_pair(role, cate)];
	ua[make_pair(user, cate)] = (
		abs(current_level) >= abs(original_level)?
		current_level : original_level
	);
	// cout<<"Update "<<user<<":"<<role<<":"<<cate<<endl;
	// cout<<original_level<<" "<<current_level<<endl;
}

int split(string s, char delim = ' ')
{
	int ret = s.find(delim);
	return ret;
}

int main()
{
	//freopen("C.txt","r",stdin);
	string str;
	int i,j,k;
	// pss testPair = make_pair("chendian", "CCFTest");
	// cout << author[testPair]; // Initial is 0
	
	int p; cin>>p;
	string anames[MAXN];
	for(i=0;i<p;i++)
	{
		cin>>str;
		int sp = split(str,':');
		//cout<<str<<" -> "<<split(str,':')<<endl;
		if (sp != -1) anames[i] = str.substr(0,sp);
		else anames[i] = str;
	}
	
	// R-Para
	int r; cin>>r;
	string rname; //roleName
	for(i=0;i<r;i++)
	{
		int s;
		cin>>rname>>s;
		for(j=0;j<s;j++)
		{
			cin>>str;
			int level = 0;
			int sp = split(str,':');			
			string category = "";
			if (sp != -1)
			{
				category = str.substr(0,sp);
				level = str.substr(sp+1)[0] - '0';
				// cout << category <<":"<< level << endl;
				ra[make_pair(rname, category)] = level+1;
			}
			else
			{
				category = str; // cate
				ra[make_pair(rname, category)] = -1;
			}
		}
	}
	
	int u; cin>>u;
	string uname; //userName
	for(i=0;i<u;i++)
	{
		int s;
		cin>>uname>>s;
		for(j=0;j<s;j++)
		{
			cin>>str; // role
			for(k=0;k<p;k++)
			{
				update(uname, str, anames[k]);
				// cout<<uname<<":"<<anames[k]<<":"<<ua[make_pair(uname, anames[k])]<<endl;
			}
		}
	}
	
	// Q-Para
	int q; cin>>q;
	string qname; //queryName
	for(i=0;i<q;i++)
	{
		cin>>qname>>str;
		int sp = split(str,':');
		string cate = "";
		cate = (sp != -1)?str.substr(0,sp):str;
		// cout<<qname<<":"<<cate<<endl;
		if(sp == -1)
		{
			int lev = ua[make_pair(qname,cate)];
			if(lev==0) cout<<"false"<<endl;
			else if(lev==-1) cout<<"true"<<endl;
			else cout<<lev-1<<endl;
		}
		else
		{
			int lev = ua[make_pair(qname,cate)]-1;
			int qlevel = str.substr(sp+1)[0]-'0';
			//cout<<lev<<":"<<qlevel<<endl;
			if(lev>=qlevel) cout<<"true"<<endl;
			else cout<<"false"<<endl;
		}
	}
	
	return 0;
}

