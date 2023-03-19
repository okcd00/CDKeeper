import sys
if __name__ == "__main__":
    # 读取第一行的n
    n, x = list(map(int, sys.stdin.readline().strip().split()))
    a = [0] + list(map(int, sys.stdin.readline().strip().split()))
    
    # 哪些场景是必须一点一点敲的： FF(FI)II
    # dp ? 每两个相邻的判断是往左边合并还是往右边。
    attr = 'O' + sys.stdin.readline().strip()
    ans = sum(a)  # maximum cost
    
    # F6 (F8 W2) I3
    cost = [ans for _ in range(n+1)]  # 0 for placeholder
    cost[0] = 0
    for i in range(1, n+1):
        if i == 1:
            cost[i] = a[i]
            continue
        # 两个深渊法师都手打
        cost[i] = cost[i-1] + a[i]
        if attr[i] != attr[i-1]:  
            cost[i] = min(cost[i], cost[i-2] + x)
    # print(cost)
    print(cost[n])
