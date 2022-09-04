/*
给定一个长度为 nn 的序列 aa ，对其子区间 [a_l \dots a_r] 询问：
\sum_{i=l}^r a_i\times (\max_{j=l}^i a_j)

输入格式：
第一行两个正整数 n,q (1≤n,q≤5×10^5) ，分别表示序列长度和询问次数。
第二行 n 个整数 a_1, a_2, \dots, a_n (1 \leq a_i \leq 10^6) (1≤ai≤10^6) ，表示给定的序列。
接下来 q 行，每行两个整数 l,r(1\leq l\leq r\leq n)l,r(1≤l≤r≤n)，表示询问的区间。

输出格式：
q 行，对每次询问输出一行一个整数表示算式的结果。

TODO: need to learn this
*/


#include <bits/stdc++.h>
using namespace std;
constexpr int MAXN = 5e5 + 10;
int number[MAXN], pos[MAXN];
long long ans[MAXN], pre[MAXN], suf[MAXN];
struct Q {
    int l, r, od;
    inline bool operator < (const Q &o) const {return l > o.l;}
} query[MAXN];

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n, q;
    cin >> n >> q;
    for (int i = 1; i <= n; ++i) cin >> number[i];
    pre[0] = 0;
    for (int i = 1; i <= n; ++i) pre[i] = pre[i - 1] + number[i];
    for (int i = 1; i <= q; ++i) {
        query[i].od = i;
        cin >> query[i].l >> query[i].r;
    }
    sort(query + 1, query + q + 1);
    suf[0] = 0;
    pos[0] = n + 1;
    int maxn = 0, left = n;
    for (int i = 1; i <= q; ++i) {
        while (left >= query[i].l) {
            while (maxn && number[left] >= number[pos[maxn]]) maxn--;
            pos[++maxn] = left;
            suf[maxn] = suf[maxn - 1] + 1LL * number[left] * (pre[pos[maxn - 1] - 1] - pre[left - 1]);
            left--;
        }
        int od = query[i].od, R = query[i].r + 1;
        ans[od] = suf[maxn];
        int l = 0, r = maxn, p;
        while (l <= r) {
            int mid = (l + r) / 2;
            if (pos[mid] >= R) l = mid + 1, p = mid;
            else r = mid - 1;
        }
        ans[od] -= 1LL * number[pos[p + 1]] * (pre[pos[p] - 1] - pre[R - 1]);
        ans[od] -= suf[p];
    }
    for (int i = 1; i <= q; ++i) cout << ans[i] << '\n';
    return 0;
}