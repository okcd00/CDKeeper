from heapq import heappop, heappush

maxn = 1000
if __name__ == "__main__":
    n, M, T = input().split(' ')
    n = int(n)
    M = int(M)
    T = int(T)
    a, m, t = [0], [0], [0]
    for i in range(n):
        aa, mm, tt = input().split(' ')
        a.append(int(aa))
        m.append(int(mm))
        t.append((T + int(tt) - 1) // int(tt))
    dp = [[0] * (M + 5) for i in range(n + 1)]# [n][M]
    for i in range(1, n + 1): # 100
        for k in range(0, t[i] + 1): # 200
            m_lst = list(range(m[i] * k, M+1)) #
            m_lst.reverse()
            for j in m_lst:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - m[i] * k] + a[i] * k)
    print(dp[n][M])

# heappush(heap,i)
# heappop(heap)

'''
3 100 20
10 8 5
5 2 1
20 25 8
'''