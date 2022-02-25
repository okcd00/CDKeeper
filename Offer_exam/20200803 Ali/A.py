from heapq import heappush, heappop

n, m = input().strip().split()
n, m = int(n), int(m)
line = input().strip().split()
x_arr = sorted([int(x) for x in line])

houses = []
for _ in range(m):
    a, b = input().strip().split()
    a, b = int(a), int(b)
    houses.append((a, b))
houses.sort(key=lambda t: t[1])

j, ans = 0, 0
heap = []
for x in x_arr:
    while j < len(houses):
        if x < houses[j][1]:
            break
        heappush(heap, -houses[j][0])
        j += 1
    if len(heap) > 0:
        a = heappop(heap)
        ans += -a
print(ans)