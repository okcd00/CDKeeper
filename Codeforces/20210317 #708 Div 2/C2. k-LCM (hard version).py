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
    
# Problem C2
from collections import Counter
t = read_int()

for _ in range(t):
    n, k = read_int_list()
    while k > 3:
        print("1", end=" ")
        n -= 1
        k -= 1
    
    if n % 2 == 1:
        print("1 {} {}".format(n//2, n//2))
    elif n % 4 == 0:
        print("{} {} {}".format(n//2, n//4, n//4))
    else:  # n % 2 == 0 and n % 4 != 0
        print("2 {} {}".format(n//2 - 1, n//2 - 1))
    