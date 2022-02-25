# Problem B
import sys
import math
 
def input(): 
    return sys.stdin.readline().rstrip()
def read_int_list(): 
    return list(map(int, input().split()))
def read_int_tuple(): 
    return tuple(map(int, input().split()))
def read_int(): 
    return int(input())
 
t = read_int()
 
for _ in range(t):
    n = read_int()
    a = read_int_list()
    ans = []
    lef = n - 1
    
    for i in range(n-1, -1, -1):
        # print(i, ':', i - a[i], lef, ans)
        _lef = i - a[i]
        if _lef >= lef:
            continue
        if _lef < lef:
            if i < lef:
                ans.append((0, lef - i))
            counts = min(max(-1, lef), i) - max(-1, _lef)
            if counts > 0:
                ans.append((1, counts))
            lef = _lef * 1
        if lef < -1:
            continue
    else:
        if lef > -1:
            ans.append((0, lef + 1))
        # print(i, ':', i - a[i], lef, ans)
                    
    for sign, length in ans[::-1]:
        print(' '.join([str(sign) for _ in range(length)]), end=' ')
