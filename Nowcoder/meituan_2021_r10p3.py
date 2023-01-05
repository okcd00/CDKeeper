"""
公司食堂
小美和小团所在公司的食堂有N张餐桌，从左到右摆成一排，每张餐桌有2张餐椅供至多2人用餐，公司职员排队进入食堂用餐。
小美发现职员用餐的一个规律并告诉小团：当男职员进入食堂时，他会优先选择已经坐有1人的餐桌用餐，
只有当每张餐桌要么空着要么坐满2人时，他才会考虑空着的餐桌；
当女职员进入食堂时，她会优先选择未坐人的餐桌用餐，只有当每张餐桌都坐有至少1人时，她才会考虑已经坐有1人的餐桌；
无论男女，当有多张餐桌供职员选择时，他会选择最靠左的餐桌用餐。现在食堂内已有若干人在用餐，另外M个人正排队进入食堂，小团会根据小美告诉他的规律预测排队的每个人分别会坐哪张餐桌。

进阶：时间复杂度O(nlogn)\O(nlogn) ,空间复杂度O(n)\O(n) 
时间限制：C/C++ 2秒，其他语言4秒
空间限制：C/C++ 256M，其他语言512M

输入描述：
第一行输入一个整数T（1<=T<=10），表示数据组数。
每组数据占四行，第一行输入一个整数N（1<=N<=500000）；
第二行输入一个长度为N且仅包含数字0、1、2的字符串，第i个数字表示左起第i张餐桌已坐有的用餐人数；
第三行输入一个整数M（1<=M<=2N且保证排队的每个人进入食堂时都有可供选择的餐桌）；
第四行输入一个长度为M且仅包含字母M、F的字符串，若第i个字母为M，则排在第i的人为男性，否则其为女性。

输出描述：
每组数据输出占M行，第i行输出一个整数j（1<=j<=N），表示排在第i的人将选择左起第j张餐桌用餐。

示例1
输入例子：
1
5
01102
6
MFMMFF
输出例子：
2
1
1
3
4
4
"""


import sys
from queue import PriorityQueue as pq

input = lambda: sys.stdin.readline().rstrip("\r\n")


T = int(input())
for _T in range(T):
    n = int(input())
    c = list(map(int, input()))

    table0, table1 = pq(), pq()
    for _idx, _v in enumerate(c):
        if _v == 0:
            table0.put(_idx + 1)
        elif _v == 1:
            table1.put(_idx + 1)

    m = int(input())
    s = list(map(lambda x: int(x == "M"), input()))

    sit = []
    for gender in s:
        # print(gender)
        if (gender == 0 and not table0.empty()) or (
            gender == 1 and table1.empty()
        ):  # sit 0
            cur = table0.get()
            sit.append(cur)
            table1.put(cur)
        else:  # sit 1
            cur = table1.get()
            sit.append(cur)

    for v in sit:
        print(v)
