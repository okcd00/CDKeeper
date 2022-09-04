/*
给定一个长为 n 的只含有0、1的字符串。

现在你可以删除最多m个字符(不改变剩余字符相对位置),将得到字符串长度记为len,
把该字符串每k个字符分为一段，即分为1~ k, k+1~ 2k …… 共 ⌈len/k⌉ 段，
现计算这 ⌈len/k⌉ 段中每段 1 的数目减去 0 的数目，所得的最大值记为该种删除方案的差异值。

请求出所有删除方案的最小差异值。

输入格式：
一行三个正整数 n,m,k (1≤n≤1×10^6, 1≤m<n, 1≤k≤1×10^6)，表示字符串长度，最多删除字符数，分段长度。
一行一个字符串 s (1≤strlen(s)≤1×10^5，保证只含0、1字符), 代表这个 01 字符串。

输出格式：
一行一个整数，表示所有删除方案的最小差异值。
*/

#include <bits/stdc++.h>
using namespace std;
const int N = 1e6 + 5;
char s[N];
int n, m, k;
int main()
{
    scanf("%d%d%d", &n, &m, &k);
    scanf("%s", s);
    int l = -k, r = k;
    while (l < r)
    {
        int mid = (l + r) >> 1;
        int tmp = m;
        int num = 0, cnt = 0;
        for (int i = 0; i < n; i++)
        {
            int c = s[i] - '0';
            if (num == k)
            {
                if (cnt > mid)
                {
                    num--;
                    cnt--;
                    tmp--;
                }
                if (num == k)
                {
                    num = 0;
                    cnt = 0;
                }
            }
            if (c == 1)
            {
                cnt++;
                num++;
            }
            else
            {
                num++;
                cnt--;
            }
        }
        if ((num + cnt) / 2 - num > mid)
        {
            tmp -= num;
            num = 0;
            cnt = 0;
        }
        else
            while (num + cnt > 0 && cnt > mid)
                tmp--, num--, cnt--;
        if (tmp >= 0 && (cnt <= mid || num == 0))
            r = mid;
        else
            l = mid + 1;
    }
    printf("%d\n", l);
}