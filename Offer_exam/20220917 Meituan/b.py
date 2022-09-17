from bisect import bisect_left

n, x, y = list(map(int, input().strip().split()))
lvl = sorted(map(int, input().strip().split()))

"""
5 6 8
3 4 2 5 1
"""

ans = 0
for i, junior in enumerate(lvl):
    # 2 3 5 (6) 7 11, index = 3, senior = 5 - 3 = 2
    # 2 3 (5) 5 7 11, index = 2, senior = 5 - 2 = 3
    invalid_x = bisect_left(lvl, x - junior)
    # one-player party is not allowed.
    if invalid_x <= i:  # or lvl[invalid_x] == junior:
        invalid_x += 1
    invalid_y = bisect_left(lvl, y / junior)
    if invalid_y <= i:  # or lvl[invalid_y] == junior:
        invalid_y += 1
    # print(i, junior, n - invalid_x, n - invalid_y)
    senior = min(n - invalid_x, n - invalid_y)
    ans += senior
print(ans // 2)
