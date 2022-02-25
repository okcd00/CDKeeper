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


# Problem B
from collections import Counter
t = read_int()

for _ in range(t):
    n, m = read_int_list()
    a = read_int_list()
    a = Counter([x % m for x in a])
    ans = 0
    if m % 2 == 0 and a[m//2] > 0:
        ans += 1
    for k in range((m+1)//2): 
        if k == 0 and a[k] > 0:
            ans += 1
            continue
        if a[k] + a[m-k] == 0:
            continue
        ans += 1
        diff = abs(a[k] - a[m-k])
        if diff > 1:
            ans += abs(a[k] - a[m-k]) - 1
    print(ans)