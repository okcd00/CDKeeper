#coding=utf-8

"""
两个有序数组的中位数
1 1 2 3 5 8 13 21 34 55
2 3 5 8 13 21 34 55 89 144
5
"""

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
k = int(input().strip())
n, m = len(a), len(b)
total_size = n + m


def get_kth_smallest(k):
    """
    从两个有序数组中找到第 k 小的数。
    具体思路：
    取 a[k//2-1] 和 b[k//2-1] 比较，取 pivot = min(a[k//2-1], b[k//2-1])
    两个数组中小于等于 pivot 的元素不超过 (k//2-1) * 2 = k-2 个，
    即 pivot 本身最多只能是第 k-1 小的数。    
    """
    offset_a = 0
    offset_b = 0
    while True:
        if offset_a >= n:
            return b[offset_b + k - 1]
        if offset_b >= m:
            return a[offset_a + k - 1] 
        if k == 1:
            return min(a[offset_a], b[offset_b])
        
        index_a = min(offset_a + k // 2 - 1, n - 1)
        index_b = min(offset_b + k // 2 - 1, m - 1)
        if a[index_a] <= b[index_b]:
            k -= index_a - offset_a + 1
            offset_a = index_a + 1
        else:
            k -= index_b - offset_b + 1
            offset_b = index_b + 1        


if total_size % 2 == 1:
    ans = get_kth_smallest( (total_size + 1) // 2 )
else:
    l = get_kth_smallest( total_size // 2 )
    r = get_kth_smallest( total_size // 2 + 1 )
    ans = (l + r) / 2
print(ans)
    