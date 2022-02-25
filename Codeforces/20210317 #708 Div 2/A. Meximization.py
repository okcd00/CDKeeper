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
from collections import Counter
t = read_int()

for _ in range(t):
    n = read_int()
    a = read_int_list()
    b = dict(Counter(a).items())
    for k in sorted(b.keys()):
        print(k, end=' ')
    for k in sorted(b.keys()):
        for _ in range(1, b[k]):
            print(k, end=' ')
    print("")
    