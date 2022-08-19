# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque


def solution(X, Y, W):
    ret = 0
    has_potholes = sorted(set(X))
    
    pivot = 0
    while pivot < len(has_potholes):
        cur = has_potholes[pivot]
        ret += 1
        while has_potholes[pivot] <= cur + W:
            pivot += 1
            if pivot == len(has_potholes):
                break
    return ret 
