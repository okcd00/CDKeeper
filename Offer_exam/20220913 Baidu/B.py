from copy import deepcopy
from collections import deque

n, m = list(map(int, input().strip().split()))
h = list(map(int, input().strip().split()))

"""
4 2
1 2 4 3
2 3
1 2
"""

ts, ks = [], []
for _ in range(m):
    t, k = list(map(int, input().strip().split()))
    if ks and k > ks[-1]:
        pivot = -1
        while k >= ks[pivot] and -pivot < len(ks):
            pivot -= 1
        pivot += 1
        ts = ts[:pivot]
        ks = ks[:pivot]
    ts.append(t)
    ks.append(k)

last_t, last_k = ts[0], ks[0]
right_piece = h[last_k:]

sorted_values = sorted(deepcopy(h[:last_k]))  # sv[i] = v
indexes = {v: i for i, v in enumerate(sorted_values)}
lsh_h = [indexes[v] for v in h[:last_k]]


ans = []
lef, rig = 0, last_k
for t, k in zip(ts[1:], ks[1:]):
    delta = last_k - k
    if last_t == 2:  # 3 2 1
        _rig = lef + delta
        ans.append((_rig-1, lef-1, -1))  # [lef, _rig-1]
        lef = _rig
        last_t, last_k = t, k
    else:  # 1 2 3
        _lef = rig - delta
        ans.append((_lef, rig, 1))  # [_lef, rig-1]
        rig = _lef
        last_t, last_k = t, k
    # print(lef, rig)
else:
    # print(lef, rig)
    if last_t == 2:
        ans.append((rig-1, lef-1, -1))  # [lef, _rig-1]
    else:
        ans.append((lef, rig, 1))  # [_lef, rig-1]

"""
for _l, _r, _step in ans[::-1]:
    for idx in range(_l, _r, _step):
        print(f"{idx}->{sorted_values[idx]}")
"""

for _l, _r, _step in ans[::-1]:
    for idx in range(_l, _r, _step):
        print(sorted_values[idx], end=' ')
for v in right_piece:
    print(v, end=' ')