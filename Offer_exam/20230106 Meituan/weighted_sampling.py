#coding=utf-8
import sys 
import random
from collections import OrderedDict

sales_dict = {  # fixed.
    1: 100,
    2: 214,
    3: 0,
    4: 50
}
sales_dict = OrderedDict(sales_dict.items())
key_case = list(sales_dict.keys())


def bisect_left(arr, pivot):
    lef, rig = 0, len(arr)
    while lef + 1 < rig:
        mid = (lef + rig) // 2
        if arr[lef] < pivot <= arr[lef+1]:
            # print(arr[lef], pivot, arr[lef+1])
            return lef
        if pivot >= arr[mid]:
            lef = mid
        elif pivot < arr[mid]:
            rig = mid 
    # print(arr[lef], pivot, arr[lef+1])
    return lef
    

cumsum_case = [0]
for k, v in sales_dict.items():
    cumsum_case.append(cumsum_case[-1] + v)

    
def weighted_sampling():
    pivot = random.randint(0, cumsum_case[-1])
    index = bisect_left(cumsum_case, pivot)
    # print(f"{pivot} in {index}")
    return key_case[index]


if __name__ == "__main__":
    res = weighted_sampling()
    print(res)
