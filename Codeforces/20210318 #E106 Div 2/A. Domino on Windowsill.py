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

# Problem A

t = read_int()
for _ in range(t):
    n, k1, k2 = read_int_list()
    w, b = read_int_list()
    if k1 > k2:
        k1, k2 = k2, k1
    max_w = k1 + (k2 - k1) // 2
    max_b = (n - k2) + (k2 - k1) // 2
    # print(w, max_w, b, max_b)
    if (w <= max_w) and (b <= max_b):
        print("YES")
    else:
        print("NO")
        
