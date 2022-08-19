# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter


def solution(S):
    ret = []
    max_mid_value = None
    for k, v in sorted(Counter(str(S)).items(), key=lambda x: -int(x[0])):
        # print(k, v, '|')
        # in case of `N is a STRING with the length (1e5)`
        ret.extend( [f'{k}'] * (v//2) )  
        if v % 2 > 0 and max_mid_value is None:
            max_mid_value = k
    
    # remove leading zeros
    pivot = 0  
    while ret and ret[pivot] == '0':
        pivot += 1
        if pivot == len(ret):
            if max_mid_value is None:
                max_mid_value = '0'
            break
    ret = ret[pivot:]

    # construct the entire string
    ret = ret + ([max_mid_value] if max_mid_value is not None else []) + ret[::-1]
    
    # print(ret, max_mid_value)
    return ''.join(ret)
