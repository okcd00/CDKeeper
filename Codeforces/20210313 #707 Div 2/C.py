# Problem C
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
 
n = read_int()
x = read_int_list()
 
vk = dict()
flag = False
for _i, va in enumerate(x):
    if flag:
        break
    for off, vb in enumerate(x[_i+1:]):
        _j = _i + off + 1
        if (va + vb) in vk:
            _io, _jo = vk[va + vb]
            if list(set([_i, _j, _io, _jo])).__len__() == 4:
                print("YES")
                print(_i + 1, _j + 1, _io + 1, _jo + 1)
                flag = True
                break
        vk[va+vb] = (_i, _j)
else:
    print("NO")    