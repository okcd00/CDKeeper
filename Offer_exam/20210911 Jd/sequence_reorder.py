def read_int_list(): 
    return list(map(int, input().split()))

def read_int(): 
    return int(input())

import collections

n = read_int()
# [6 4 8 2 10 1 9 3 7 5]
#  [5 4 7 2 9 1 8 3 6]

ret = 0
ans = [0] * n  
arr = sorted(read_int_list())

if n == 1:
    print(arr[0])
else:
    ret = 0
    lp = (n-1) // 2
    rp = lp + 1
    ans[lp] = arr[-1]
    ans[rp] = arr[0]

    for pivot, r_num in enumerate(arr[1:-1]):
        l_num = arr[n-pivot-2]
        lp = lp + (-1)**pivot * (pivot+1) * 2  # 4 -> 6 -> 2 -> 8 -> 0
        rp = rp + (-1)**(pivot+1) * (pivot+1) * 2  # 5 -> 3 -> 7 -> 1 -> 9
        if 0 <= lp < n:
            ans[lp] = l_num            
        if 0 <= rp < n:
            ans[rp] = r_num 
        if l_num > r_num:
            break
    ret = sum([abs(ans[i] - ans[i-1]) for i in range(1, n)])
    print(ret)
