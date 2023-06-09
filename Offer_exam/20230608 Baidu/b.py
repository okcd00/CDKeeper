# dp? dfs? greedy?

# assume 1: dp[i] 指到达第 i 座山的时候，已经攀登的山数 
# X # 需要看当前能力值

# assume 2: dp[i][j] 到达第 i 座山【前】，已经攀登了 j 座时，最高能力值是多少 
# 如何为dp追加判断，能否过去这座山

# assume 3: search for maximum benefit
# AC

"""
3 x x x x x
3 x x x x x
3 4 x x x x
x 5 6 x x x  
x 
x  
"""

from heapq import heappop, heappush

n, k = list(map(int, str(input()).strip().split(' ')))
h = list(map(int, str(input()).strip().split(' ')))
a = list(map(int, str(input()).strip().split(' ')))

"""
5 3
3 2 5 4 6
1 2 1 3 0
"""

def greedy():  # AC
    ans = 0
    que = []
    for i in range(n):
        _h = h[i]
        _a = a[i]
        while k < _h and len(que) > 0:
            k -= heappop(que)
            ans += 1
        if k < _h:
            ans = -1
            break
        heappush(que, -_a)

    print(ans)

greedy()