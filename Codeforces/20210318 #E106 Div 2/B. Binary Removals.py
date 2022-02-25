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

t = read_int()
for _ in range(t):
    s = input()
    length = s.__len__()
    lef_pivot, rig_pivot = -2, length + 1
    for lef, c in enumerate(s):
        if c == '1':
            if lef - lef_pivot <= 1:
                break
            lef_pivot = lef
            # print(lef_pivot, end=' ')
    else:
        lef_pivot = length + 1
    for _rig, c in enumerate(s[::-1]):
        rig = length - 1 - _rig
        if c == '0':
            if rig_pivot - rig <= 1:
                break
            rig_pivot = rig
            # print(rig_pivot, end=' ')
    else:
        rig_pivot = -2
    print("YES" if lef_pivot >= rig_pivot else "NO")