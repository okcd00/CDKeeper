import os
from collections import Counter

s = input().strip()

rec = [(0, 0, 0)]  # init: empty

r, e, d = 0, 0, 0
for c in s:
    if c == 'r':
        r += 1
    if c == 'e':
        e += 1
    if c == 'd':
        d += 1
    minv = min([r, e, d])
    if minv > 0:
        r, e, d = r-minv, e-minv, d-minv
    rec.append((r, e, d))

ret = 0
for pattern, count in Counter(rec).most_common():
    # print(pattern, count)
    if count == 1:
        break
    # (head + tail) * count // 2
    ret += (1 + count - 1) * (count - 1) // 2
print(ret)