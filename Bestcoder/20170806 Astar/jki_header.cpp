/*==========================================================================
#   Copyright (C) 2017 All rights reserved.
#
#   filename : header.cpp
#   author   : chendian / okcd00@qq.com
#   date     : 2088-88-88
#   desc     : with jki14's header 
#   blog.csdn.net/okcd00
# ==========================================================================*/

#include <set>
#include <map>
#include <list>
#include <cmath>
#include <ctime>
#include <queue>
#include <bitset>
#include <vector>
#include <cstdio>
#include <string>
#include <numeric>
#include <utility>
#include <iomanip>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
using namespace std;

//HEAD_OF_JKI'S_HEADER_

    //CONST VALUE
    static const int MOD=10007;
    const double PI=acos(-1.0);
    const double EPS=1e-5;
    
	//TYPEDEF
    typedef long long lld;
    typedef unsigned long long u64;
    typedef double dou;
    typedef pair<int, int> pii;

    //COMPARE
    template<class T> inline T MIN(const T x, const T y){ return (x<y)?x:y; }
    template<class T> inline T MAX(const T x, const T y){ return (x>y)?x:y; }

    template<class T> inline void UPDMIN(T &x, const T y){ if(x>y)x=y; }
    template<class T> inline void UPDMAX(T &x, const T y){ if(x<y)x=y; }

    //STL
    template<class T1, class T2> inline pair<T1, T2> MP(const T1 &x, const T2 &y){ return make_pair(x, y); }

    //BIT
    inline int BINT(const int x){ return 1<<x; }
    inline lld BLLD(const int x){ return 1LL<<x; }
    inline int BINT_TEST(const int s, const int x){ return (s&BINT(x))!=0; }
    inline int BLLD_TEST(const lld s, const int x){ return (s&BLLD(x))!=0LL; }
    
    template<class T> inline T LOWBIT(const T x){ return (x^(x-1))&x; }
    template<class T> inline int BITCOUNT(const T x){ return (!x)?x:(1+BITCOUNT(x&(x-1))); }

    //CALCULATE
    template<class T> inline T SQR(const T x){ return x*x; }
    template<class T1, class T2> inline T1 POW(const T1 x, const T2 y){
        if(!y)return 1;else if((y&1)==0){
            return SQR(POW(x, y>>1));
        }else return POW(x, y^1)*x;
    }

    //NUMBERIC
    template<class T> inline T GCD(const T x, const T y){
        if(x<0)return GCD(-x, y);
        if(y<0)return GCD(x, -y);
        return (!y)?x:GCD(y, x%y);
    }
    template<class T> inline T LCM(const T x, const T y){
        if(x<0)return LCM(-x, y);
        if(y<0)return LCM(x, -y);
        return x*(y/GCD(x, y));
    }
    template<class T> inline T EEA(const T a, const T b, T &x, T &y){
        /* a*x+b*y == GCD(a, b) == EEA(a, b, x, y) */
        if(a<0){ T d=EEA(-a, b, x, y); x=-x; return d; }
        if(b<0){ T d=EEA(a, -b, x, y); y=-y; return d; }
        if(!b){
            x=1; y=0; return a;
        }else{
            T d=EEA(b, a%b, x, y);
            T t=x; x=y; y=t-(a/b)*y;
            return d;
        }
    }
    template<class T> inline vector<pair<T, int> > FACTORIZE(T x){
        vector<pair<T, int> > ret;
        if(x<0)x=-x;
        for (T i=2;x>1;){
            if(x%i==0){
                int count=0;
                for(;x%i==0;x/=i)count++;
                ret.push_back(MP(i, count));
            }
            i++;if(i>x/i)i=x;
        }
        return ret;
    }
    template<class T> inline int ISPRIME(const T x){
        if(x<=1)return 0;
        for(T i=2; SQR(i)<=x; i++)if(x%i==0)return 0;
        return 1;
    }
    template<class T> inline T EULARFUNCTION(T x){
        vector<pair<T, int> > f=FACTORIZE(x);
        for(typename vector<pair<T, int> >::iterator it=f.begin(); it!=f.end(); it++){
            x=x/it->first*(it->first-1);
        }
        return x;
    }
    template<class T> inline T INVERSEE(const T a, const T b){
        T x, y;
        EEA(a, b, x, y);
        return x?x:1;
    }

    //REMINDER-LIZATION
    template<class T> inline T MOD_STD(const T x, const T m){ return (x%m+m)%m; }
    template<class T> inline T MOD_STD(const T x){ return (x%MOD+MOD)%MOD; }
    
    template<class T> inline T MOD_ADD(const T x, const T y, const T m){ return (x+y)%m; }
    template<class T> inline T MOD_ADD(const T x, const T y){ return (x+y)%MOD; }
    
    template<class T> inline void MOD_ADD(T *x, const T y, const T m){ *x=(*x+y)%m; }
    template<class T> inline void MOD_ADD(T *x, const T y){ *x=(*x+y)%MOD; }
    
    template<class T> inline T MOD_MUL(const T x, const T y, const T m){ return (T)((1LL*x*y)%m); }
    template<class T> inline T MOD_MUL(const T x, const T y){ return (T)((1LL*x*y)%MOD); }
    
    template<class T> inline void MOD_MUL(T *x, const T y, const T m){ *x=(T)((1LL*(*x)*y)%m); }
    template<class T> inline void MOD_MUL(T *x, const T y){ *x=(T)((1LL*(*x)*y)%MOD); }
    
    template<class T1, class T2> inline T1 MOD_POW(const T1 x, const T2 y, const T1 m){
        if(y==0)return 1%m;else if((y&1)==0){
            T1 z=MOD_POW(x, y>>1, m); return MOD_MUL(z, z, m);
        }else return MOD_MUL(MOD_POW(x, y^1, m), x, m);
    }
    template<class T1, class T2> inline T1 MOD_POW(const T1 x, const T2 y){
        if(y==0)return 1%MOD;else if((y&1)==0){
            T1 z=MOD_POW(x, y>>1); return MOD_MUL(z, z);
        }else return MOD_MUL(MOD_POW(x, y^1), x);
    }

//TAIL_OF_JKI'S_HEADER_

static const lld LLMIN = 0xc0c0c0c0c0c0c0c0LL;
static const lld LLMAX = 0x3f3f3f3f3f3f3f3fLL;

int main()
{
	ios::sync_with_stdio(false);
	MATX<int> a = MATX<int>(3,3);
	a.set_one();
	a(1LL, 1LL) = 3;
	a = a * a.pow(3LL);
	a.show();
	return 0;	
} 
