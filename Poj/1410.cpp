#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#define Max(x, y)(x > y ? x : y)
#define Min(x, y)(x < y ? x : y)
using namespace std;
int n;
bool flag;//标志变量
struct Point
{
    double x;
    double y;
}rec[4], seg[2];//rec数组存储矩形的坐标,seg数组存储线段两点的坐标
double Multi(Point p1, Point p2, Point p3)//叉乘判断点与线的位置关系
{
    return (p1.x - p3.x) * (p2.y - p3.y) - (p2.x - p3.x) * (p1.y - p3.y);
}
//跨立试验，判断两线段是否相交
bool Isintersect(Point a1, Point a2, Point b1, Point b2)//判断两条线段是否相交（含顶点）
{
    if (Min(a1.x, a2.x) <= Max(b1.x, b2.x) &&
        Min(a1.y, a2.y) <= Max(b1.y, b2.y) &&
        Min(b1.x, b2.x) <= Max(a1.x, a2.x) &&
        Min(b1.y, b2.y) <= Max(a1.y, a2.y) &&
        Multi(a1, a2, b1) * Multi(a1, a2, b2) <= 0 &&
        Multi(b1, b2, a1) * Multi(b1, b2, a2) <= 0
        )
        return true;//说明两线段之间相交
    return false;
}
bool Inrectangle(int i)//判断点是否在矩形的内部
{
    if (seg[i].x > Max(rec[1].x, rec[3].x)) return false;
    if (seg[i].y > Max(rec[1].y, rec[3].y)) return false;
    if (seg[i].x < Min(rec[1].x, rec[3].x)) return false;
    if (seg[i].y < Min(rec[1].y, rec[3].y)) return false;
    //如果满足上面的，说明线段在矩形的内部并且没有和矩形没有交点（含线段的顶点）
    return true;
}
int main()
{
    int i;
    scanf("%d", &n);
    while (n --)
    {
        scanf("%lf%lf%lf%lf", &seg[0].x, &seg[0].y, &seg[1].x, &seg[1].y);
        scanf("%lf%lf%lf%lf", &rec[1].x, &rec[1].y, &rec[3].x, &rec[3].y);
        rec[0].x = rec[1].x;
        rec[0].y = rec[3].y;
        rec[2].x = rec[3].x;
        rec[2].y = rec[1].y;
        flag = false;//假设线段和矩形没有相交
        if (Inrectangle(0) || Inrectangle(1))
        {
            flag = true;
        }
        else
        {
            for (i = 0; i < 4; ++i)
            {
                if (Isintersect(rec[i], rec[(i + 1) % 4], seg[0], seg[1]))
                {
                    flag = true;//两线段已经相交了直接退出即可
                    break;
                }
            }
        }
        if (flag)//线段和矩形相交
        {
            printf("T\n");
        }
        else
        {
            printf("F\n");
        }
    }
    return 0;
}