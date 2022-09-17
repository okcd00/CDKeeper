n, x, y = list(map(int, input().strip().split()))
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))

"""
7 3 4
3 1 2
4 5 6 7
"""

d = a + b[::-1]
rest = [1 for _ in range(n)]
index = {v: i for i, v in enumerate(d)}
pivot = len(a)  # pivot is **before** the k-th element
# print(d)

ans = 0
for target in range(1, n+1):
    src, dest = pivot, index[target]  # 3 4 (dest@2) 1@2 5 2
    cost = 0
    if src <= dest:
        cost = sum(rest[src:dest:1])  # travel src->dest
        move_to = index[target]
    else:  # src > dest
        cost = sum(rest[src-1:dest:-1])  # travel [dest+1, src)
        move_to = index[target] + 1
    ans += cost + 1  # pickup
    # print(f"pivot: {pivot}->{move_to}, cost {cost} + 1. {d[:move_to]+['v']+d[move_to:]}")
    pivot = move_to
    rest[index[target]] = 0
print(ans)
