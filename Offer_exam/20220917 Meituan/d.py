"""
小美有n个蓝色的球，上面分别写着1到n。小团有n个红色的球，上面也写着1到n。
有一天，神秘人把这2n个球混到了一起并排成了一列。
在将这2n个球分开之前，小美和小团必须通过进行数次“交换相邻的两个球”的操作
使得任意两个分别写着 i 和 i+1的同色球，有 i 在 i+1的左边。
现在小美和小团想知道它们需要进行多少次操作才能达成条件。


输入描述
第一行有一个正整数n(1<=n<=200)，代表球的个数。
第二行有2n个整数，代表从左到右的2n个球。正数代表红球，负数代表蓝球。-n到n之间的每个非零整数均会出现恰好一次。

输出描述
输出一个非负整数，代表所求的答案。

Failed.
"""

n = int(input().strip())
a = list(map(int, input().strip().split()))
ball_index = {v: i for i, v in enumerate(a)}

"""
4
3 -3 1 -4 2 -2 -1 4

10
"""


def dfs(red_pivot, blue_pivot, cur_ans=0):
    # initial
    red = ball_index[red_pivot] if red_pivot <= n else None
    blue = ball_index[-blue_pivot] if blue_pivot <= n else None

    for i in range(red_pivot + blue_pivot - 2, 2*n):
        if red is None:
            take_red = False
        elif blue is None:
            take_red = True
        elif abs(red - i) < abs(blue - i):
            take_red = True
        elif abs(red - i) > abs(blue - i):
            take_red = False
        else:
            return min(
                dfs(red_pivot=red_pivot+1,
                    blue_pivot=blue_pivot,
                    cur_ans=cur_ans+abs(ball_index[red_pivot] - i)),
                dfs(red_pivot=red_pivot,
                    blue_pivot=blue_pivot+1,
                    cur_ans=cur_ans+abs(ball_index[blue_pivot] - i))
            )
        
        # 1 2 3 -1 -2 4 -3 -4 ?
        # print(i, red, blue, take_red, end=' ')
        if take_red:
            # ans_permutation.append(red)
            cur_ans += abs(red - i)
            # print(f"+{abs(red - i)}")
            red_pivot += 1
            red = ball_index[red_pivot] if red_pivot <= n else None
        else:
            # ans_permutation.append(blue)
            cur_ans += abs(blue - i)
            # print(f"+{abs(blue - i)}")
            blue_pivot += 1
            blue = ball_index[-blue_pivot] if blue_pivot <= n else None

    return cur_ans

# print(dfs(1, 1, 0))
print(dfs(1, 1, 0) // 2)
