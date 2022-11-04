# left: all e in a[:i] have e < x
# right: all e in a[:i] have e <= x
from bisect import bisect_left


"""
位置连续的货箱从左到右整理成三堆，每堆至少1个箱子
要求三堆满足： 左堆货箱重量 <= 中堆货箱重量 <= 右堆货箱重量
请问有多少种满足要求的整理方案。
"""


def get_index(arr, pivot):
    # the first index for a[i] >= pivot
    return bisect_left(arr, pivot)


def get_solution_counts(arr, vmod=int(1e9)+8):
    ret = 0
    cum_sum = [arr[0]]
    for i, v in enumerate(arr):
        if i == 0:
            continue
        cum_sum.append(cum_sum[-1] + v)
    print(cum_sum)
    total = cum_sum[-1]  # at most 10^12
    
    # l, r = 0, len(arr-1)
    for l in range(len(arr)-2):
        l_sum = cum_sum[l] 

        left_sum = l_sum * 2
        mid_pile_left = max(l, get_index(cum_sum, left_sum))
        print(cum_sum, left_sum, mid_pile_left)

        right_sum = l_sum + (total - l_sum) // 2
        mid_pile_right = min(len(arr)-2, get_index(cum_sum, right_sum))
        print(cum_sum, right_sum, mid_pile_right)

        delta = max(0, mid_pile_right - mid_pile_left + 1)
        print(l, mid_pile_left, '~', mid_pile_right, ':', delta, 'counts.')
        
        ret += delta
        ret = ret % vmod
    return ret


if __name__ == "__main__":
    arr = [1,1,2,1,4]
    print(get_solution_counts(arr))
