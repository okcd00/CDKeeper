# N 个物品, X 元, Y 张折扣价
# from pprint import pprint
n, x, y = list(map(int, input().strip().split()))

c, d = [-1], [-1]
for i in range(n):
    cost, discount = list(map(int, input().strip().split()))
    c.append(cost)  # 1~50
    d.append(discount)

# backpack dp[N][N][Y] = 
# 3000ms = Y x 5000 x 5000 
# for i, only select one of c[i] and d[i].
# maximum count
# minimum cost
MAXIMUM_COST = 50 * 2 * n + 1
dp = [[[MAXIMUM_COST for _k in range(y+1)] for _j in range(n+1)] for _i in range(n+1)]

# travel
dp[0][0][0] = 0
for i in range(1, n+1):
    for j in range(n+1):
        for k in range(y+1):
            dp[i][j][k] = min(dp[i][j][k], dp[i-1][j][k])  # pass
            if j >= 1:  # take
                dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][k] + c[i])
                if k >= 1:  # take and take the discount
                    dp[i][j][k] = min(dp[i][j][k], dp[i-1][j-1][k-1] + d[i])
# pprint(dp)

# get results
ret = (n, MAXIMUM_COST)
for j in range(n+1):
    for k in range(y+1):
        if dp[n][j][k] <= x:
            ret = min(ret, (n-j, dp[n][j][k]))
print(n-ret[0], ret[1])

"""
3 5 1
4 3
3 1
6 5
"""


# 