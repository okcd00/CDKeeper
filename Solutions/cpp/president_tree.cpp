#include <bits/stdc++.h>
using namespace std;

/*
  https://www.bilibili.com/video/BV1PT411L7XQ
  主席树板子: 可持久化权值线段树
  主席树功能：给定序列，对于指定闭区间 [l, r] 内的第 k 小/大 值

  【对比】
  普通线段树：给定序列，以下标区间作节点区间，节点维护区间最值、区间和等
  权值线段树：给定序列，以序列值域作节点区间，节点维护值域内数的出现次数
*/

#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

#define rep(i, l, r) for (int i = (l); i <= (r); ++i)

const int maxn = 200001;        // 最多有多少个节点 1<<18
int n, q = 0;                   // 值域 1~n，询问次数 q，
int mid = 0, node_idx = 0;      // 二分中点 mid，节点计数器 node_idx
int a[maxn], b[maxn];           // a 即待处理数组, b 为用于排序和记录的数组（也可以由 vector<int> v 替代）
vector<int> v;                  // 用于排序和记录的数组 v
int root[maxn];                 // root[i] 表示第 i 颗线段树的根节点编号
int L[maxn << 5], R[maxn << 5]; // L[i] 表示节点 i 的左子节点编号; R[i] 表示节点 i 的右子节点编号
int counts[maxn << 5];          // count[i] 表示节点 i 对应的值域区间内有多少个数

/*
    build(int &x, int l, int r)
    建空树：递归创建值域 [1, n] 内的各个节点。
    x 为当前节点的编号，x 是 "传递引用"，通过子空间的 x，给父空间的 L[x], R[x] 赋值
*/
void build(int &x, int l, int r)
{
    // 为当前节点分配编号
    x = ++node_idx;

    // 递归边界：值域只有一个数，不再分割
    if (l == r)
        return;

    // 建树时是建的空树，所以 counts 都为 0
    counts[x] = 0;

    // 二分中点，双指针同步搜索
    mid = (l + r) >> 1;
    build(L[x], l, mid);     // 递归创建左子空间
    build(R[x], mid + 1, r); // 递归创建右子空间
}

/*
    insert(int x, int &y, int l, int r, int v)
    建主席树：递归建立每个历史版本的线段树。
    y 是 "传递引用"，通过子空间的 y，给父空间的 L[y], R[y] 赋值

    usage:
    for(int i=1; i<=n; i++)
        insert(root[i-1], root[i], 1, n, a[i]);
*/
void insert(int x, int &y, int l, int r, int v)
{
    // 为当前节点分配编号
    y = ++node_idx;

    // 首先复制父节点 x 的信息给 y
    L[y] = L[x], R[y] = R[x], counts[y] = counts[x] + 1;

    // 递归边界：值域只有一个数，不再分割
    if (l == r)
        return;

    // 二分中点，双指针同步搜索
    mid = (l + r) >> 1;
    if (v <= mid) // v 在左子空间时，递归插入左子空间
        insert(L[x], L[y], l, mid, v);
    else // v 在右子空间时，递归插入右子空间
        insert(R[x], R[y], mid + 1, r, v);
}

/*
    void update(int x, int l, int r, int v)
    更新主席树：递归更新每个历史版本的线段树。
*/
void update(int x, int l, int r, int v)
{
    // 递归边界：值域只有一个数，不再分割
    if (l == r)
    {
        counts[x]++; // 更新当前节点的信息
        return;
    }

    // 二分中点，双指针同步搜索
    mid = (l + r) >> 1;
    if (v <= mid) // v 在左子空间时，递归更新左子空间
        update(L[x], l, mid, v);
    else // v 在右子空间时，递归更新右子空间
        update(R[x], mid + 1, r, v);
}

/*
    query(int x, int y, int l, int r, int k)
    查询主席树：在主席树上查询区间 [l,r] 中的第 k 小
    简化：找到插入 r 时的历史版本，在权值线段树上做二分搜索
    扩展：求 [l,r] 区间第 k 小，可以用前缀和，即 [1,r] - [1,l-1]

    usage:
    scanf("%d%d%d", &l,&r,&k);
    query(root[l-1], root[r], 1, n, k)
*/
int query(int x, int y, int l, int r, int k)
{
    // 递归边界：值域只有一个数，不再分割
    if (l == r)
        return l; // 返回当前节点的值域

    // 二分中点，双指针同步搜索
    mid = (l + r) >> 1;

    // 左子空间的节点数
    int cnt = counts[L[y]] - counts[L[x]];

    if (k <= cnt) // k 在左子空间时，递归查询左子空间
        return query(L[x], L[y], l, mid, k);
    else // k 在右子空间时，递归查询右子空间
        return query(R[x], R[y], mid + 1, r, k - cnt);
}

/*
    discretization algorithm
    离散化: 把数据排序，然后用 1, 2, 3, ..., n 来代表数据

    for (int i = 1; i <= n; i++)
        insert(root[i-1], root[i], 1, vn, getid(a[i]))

    int id = query(root[l-1], root[r], 1, vn, k) - 1;
    print("%d\n", v[id]);
*/
void discretization_list()
{
    // int b[MAXN];
    // usage: lower_bound(b + 1, b + n + 1, a[i]) - b;
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &a[i]);
        b[i] = a[i]; // if use another list
    }
    sort(b + 1, b + n + 1);
    mid = unique(b + 1, b + n + 1) - b - 1;
}

void discretization_vector()
{
    // vector<int> v;
    // usage: lower_bound(v.begin(), v.end(), x) - v.begin() + 1;
    for (int i = 1; i <= n; i++)
    {
        scanf("%d", &a[i]);
        v.push_back(a[i]); // if use vector
    }
    sort(v.begin(), v.end());
    v.erase(unique(v.begin(), v.end()), v.end());
}

int getid(int x)  //返回x的下标
{ 
    return lower_bound(v.begin(), v.end(), x) - v.begin() + 1;
}

int main()
{
    scanf("%d%d", &n, &q);
    discretization_vector();
    int vn = v.size();  // 值域边界 vn

    // build(root[0], 1, n);  // 有时 build 可以省去
    // 例如：可持久化权值线段树入门题——静态区间第 kk 小
    // https://www.luogu.com.cn/problem/P3834
    for (int i = 1; i <= n; i++)
        insert(root[i - 1], root[i], 1, vn, getid(a[i]));

    while (q--)
    {
        int l, r, k;
        scanf("%d%d%d", &l, &r, &k);
        int id = query(root[l - 1], root[r], 1, vn, k) - 1;
        printf("%d\n", v[id]);
    }
    return 0;
}