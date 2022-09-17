n = int(input().strip())
a = sorted(map(int, input().strip().split()))


def dist(start):
    return sum([abs(v - (start+i)) for i, v in enumerate(a)])


ans = 10000 * 1000
for start in range(1, 10002-n):
    res = dist(start)
    if res < ans:
        ans = res
        # print(res)
print(ans)
