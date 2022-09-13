from bisect import bisect_right

n, m, t = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

"""
5 3 14
1 3 2 2 1
4 6 1
"""

cost_a = [0]
for _cost in a:
    cost_a.append(cost_a[-1] + _cost)

cost_b = [0]
for _cost in b:
    cost_b.append(cost_b[-1] + _cost)

ans = 0
for rank_a in range(n+1):
    if cost_a[rank_a] > t:
        break
    rest = t - cost_a[rank_a]
    rank_b = bisect_right(cost_b, rest) - 1
    # print(rank_a, rank_b)
    # print(cost_a[rank_a], cost_a)
    # print(rest, cost_b)
    if rank_a + rank_b > ans:
        ans = rank_a + rank_b
print(ans)