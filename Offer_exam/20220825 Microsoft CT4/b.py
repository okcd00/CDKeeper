from collections import Counter


def solution(A):
    cum_sum = [0]
    for v in A:
        cum_sum.append(cum_sum[-1] + v)

    ret = 0
    for val, count in Counter(cum_sum).items():
        if count > 44722:
            return -1
        if count > 1:
            ret += count * (count - 1) // 2
            if ret > int(1e9):
                return -1
    return ret