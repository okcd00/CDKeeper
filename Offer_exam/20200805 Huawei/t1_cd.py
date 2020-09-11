def convert(s):
    s = s.strip().lower()
    s = sum([ord(x)-96 if (0 < ord(x)-96 < 27) else 0 for x in s])
    return s

# bbb a_a ccc fff AAZZ xyx
line = input().strip().split()
values = [convert(x) for x in line]
target = values.pop(0)

ans = ""
m = 255 * 11
for i, x in enumerate(values):
    dist = abs(x-target)
    # print(x, dist, line[i+1])
    if dist <= m:
        m = dist
        ans = line[i+1]
print(ans)