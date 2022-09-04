/*
小度热爱离散数学。

定义在bool变量（00 或 11）上的二元运算蕴含（ \rightarrow → ）：
0→0=1
0→1=1
1→0=0
1→1=1

问有多少种 nn 个元素的 0101 序列 x （x_1, x_2, \dots, x_n 每个都可以取 0 或 1）
同时满足以下两个条件：
左结合和右结合进行蕴含运算最终结果都为 1 ，输出序列的种数对 998244353 取模的值。

格式
输入格式：
一行一个正整数 n(2≤n≤10^{10^6})，表示序列长度。

输出格式：
一行一个整数，表示答案。
*/


#include <bits/stdc++.h>
using namespace std;
const int mod = 998244353;
int power(int a, int b) {
    long long res = a, ans = 1;
    for (; b; b >>= 1, res = res * res % mod) if (b & 1) ans = ans * res % mod;
    return ans;
}
int main() {
    int n = 0, c;
    while (isdigit(c = getchar())) n = (n * 10ll + c - '0') % 998244352;
    int inv3 = (mod + 1) / 3;
    cout << 1ll * (power(2, n + 1) + (n % 2 ? -1 : 1)) * inv3 % mod << endl;
}