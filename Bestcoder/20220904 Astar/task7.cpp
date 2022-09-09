/*
	小度是个粉刷匠，粉刷括号本领强。

	墙上有从左到右 n 个瓷砖，小度有 k 种颜料可以在每个位置刷上一个任意一种颜色的左括号或者右括号，
	问最后有多少种不同的粉刷方案，使得每一种颜色的括号构成的子序列都是合法的括号序列。

	两种方案不同，当且仅当存在某个位置，两种方案中一个是左括号而另一个是右括号或者颜色不同，
	输出方案数对 998244353 取模的值。

	定义合法的括号序列：

	1 空序列合法； 
	2 如果 S 合法，则(S) 合法，这里的左右括号可以是任意一种相同的颜色；
	3 如果 S 和 T 都合法，则 ST（把两者首尾相接）合法。

	举例说明，如果 n = 10，小度有 3 种颜料对应的左右括号分别用()、[]、{} 表示，
	则 [[](({)])} 这种粉刷方案符合条件，因为 ()()、[[]]、{} 都是合法的括号序列，而方案 []))(())[] 不满足条件。

	格式
	输入格式：
	一行两个正整数 n,k (1 ≤ n ≤ 5×10^5,1 ≤ k ≤ 1000)，表示瓷砖个数和颜料种数。

	输出格式：
	一行一个整数，表示方案数取模后的值。

	TODO: learn this problem
*/

#include <bits/stdc++.h>
#define rep(i, x, y) for (int i = x; i <= y; ++i)
#define repd(i, x, y) for (int i = x; i >= y; --i)

using namespace std;
typedef long long LL;
const int N=2000005,mod=998244353;
int n,k,len,bin[N];
LL flv[N],Inv[N],Wn[20][N];
LL lim,f[N],a[N],b[N],c[N],G[N],A0[N],A[N],B[N],inv[N];

int getint()
{
	char ch;
	while (!isdigit(ch = getchar()))
		;
	int x = ch - 48;
	while (isdigit(ch = getchar()))
		x = x * 10 + ch - 48;
	return x;
}

LL getmi(LL a,LL x)
{
	LL rt = 1;
	while (x)
	{
		if (x & 1)
			rt = rt * a % mod;
		a = a * a % mod, x >>= 1;
	}
	return rt;
}

void FFT(LL a[],int len,int tp)
{
	rep(i, 0, len - 1) bin[i] = bin[i >> 1] >> 1 | ((i & 1) * (len >> 1));
	rep(i, 0, len - 1) if (i < bin[i]) swap(a[i], a[bin[i]]);
	for (int i = 1, cnt = 0; i < len; ++cnt, i <<= 1)
	{
		for (int j = 0; j < len; j += i << 1)
		{
			LL w = 0, x, y;
			rep(k, 0, i - 1)
			{
				x = a[j + k], y = a[i + j + k] * Wn[cnt][w + i] % mod, w += tp;
				a[j + k] = (x + y) % mod, a[i + j + k] = (x - y + mod) % mod;
			}
		}
	}
	if (tp == -1)
	{
		LL x = getmi(len, mod - 2);
		rep(i, 0, len - 1) a[i] = a[i] * x % mod;
	}
}	

void get_inv(LL a[],LL b[],int n)
{
	if (n == 1)
	{
		b[0] = getmi(a[0], mod - 2);
		return;
	}
	get_inv(a, b, n >> 1);
	rep(i, 0, n - 1) G[i] = a[i];
	rep(i, n, 2 * n - 1) G[i] = 0;
	FFT(G, n << 1, 1), FFT(b, n << 1, 1);
	rep(i, 0, 2 * n - 1) b[i] = b[i] * (2 - G[i] * b[i] % mod + mod) % mod;
	FFT(b, n << 1, -1);
	rep(i, n, 2 * n - 1) b[i] = 0;
}

void get_ln(LL a[],LL b[],int n)
{
	rep(i, 0, 2 * n - 1) A[i] = B[i] = 0;
	get_inv(a, A, n);
	rep(i, 0, n - 2) B[i] = a[i + 1] * (i + 1) % mod;
	FFT(A, n << 1, 1), FFT(B, n << 1, 1);
	rep(i, 0, 2 * n - 1) A[i] = A[i] * B[i] % mod;
	FFT(A, n << 1, -1), b[0] = 0;
	rep(i, 1, n - 1) b[i] = A[i - 1] * inv[i] % mod;
}

void get_exp(LL a[],LL b[],int n)
{
	if (n == 1)
	{
		b[0] = lim;
		return;
	}
	get_exp(a, b, n >> 1);
	rep(i, 0, 2 * n - 1) A0[i] = 0;
	get_ln(b, A0, n);
	rep(i, 0, n - 1) A0[i] = (a[i] + mod - A0[i]) % mod;
	++A0[0], FFT(A0, n << 1, 1), FFT(b, n << 1, 1);
	rep(i, 0, 2 * n - 1) b[i] = b[i] * A0[i] % mod;
	FFT(b, n << 1, -1);
	rep(i, n, 2 * n - 1) b[i] = 0;
}

int main()
{
	n = getint(), k = getint();

	rep(i, 0, 19)
	{
		int x = 1 << i;
		Wn[i][x] = 1;
		LL wn = getmi(3, (mod - 1) / (x << 1));
		rep(j, 1, x - 1) Wn[i][j + x] = Wn[i][j + x - 1] * wn % mod;
		wn = getmi(wn, mod - 2);
		rep(j, 1, x - 1) Wn[i][-j + x] = Wn[i][-j + x + 1] * wn % mod;
	}

	flv[0] = 1;
	rep(i, 1, n) flv[i] = flv[i - 1] * i % mod;
	Inv[n] = getmi(flv[n], mod - 2);
	repd(i, n, 1) Inv[i - 1] = Inv[i] * i % mod;
	rep(i, 1, n) inv[i] = Inv[i] * flv[i - 1] % mod;

	rep(i, 0, n) if (!(i & 1))
	{
		int x = i >> 1;
		f[i] = Inv[x] % mod * Inv[x] % mod * getmi(x + 1, mod - 2) % mod;
	}
	for (len = lim = 1; len <= n; len <<= 1)
		;
	get_ln(f, a, len);
	rep(i, 0, len - 1) a[i] = a[i] * k % mod;
	get_exp(a, b, len);
	LL ans = b[n] * flv[n] % mod;
	printf("%lld\n", (ans + mod) % mod);
	return 0;
}