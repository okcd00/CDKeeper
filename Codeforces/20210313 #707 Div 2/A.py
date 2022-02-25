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
    a, b = [0], [0]
    for idx in range(n):
        _a, _b = read_int_list()
        a.append(_a)
        b.append(_b)
    tm = [0] + read_int_list()
 
    cur = 0
    for i in range(1, n+1):
        cur += (a[i] - b[i-1] + tm[i])
        # print("Arr:", cur)
        if i == n:
            break
        least_waiting = (b[i] + 1 - a[i]) // 2
        # print("Wait:", least_waiting)
        leaving = cur + least_waiting        
        if leaving < b[i]:
            cur = b[i]    
        else:
            cur = leaving
        # print("Leave:", cur)
    print(cur)