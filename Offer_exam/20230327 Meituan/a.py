#coding=utf-8
import sys 

a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
k = int(input().strip())
n, m = len(a), len(b)
total_size = n + m


def get_kth_smallest(k):
    offset_a = 0
    offset_b = 0
    while True:
        if k == 1:
            return min(a[offset_a], b[offset_b])
        
        index_a = min(offset_a + k // 2 - 1, n - 1)
        index_b = min(offset_b + k // 2 - 1, m - 1)
        
        if offset_a >= n:
            return b[k - n + 1]
        if offset_b >= m:
            return a[k - m + 1] 
        
        if a[offset_a] > b[offset_b]:
            k -= index_a - offset_a + 1
            offset_a = index_a + 1
        else:
            k -= index_b - offset_b + 1
            offset_b = index_b + 1        

            
if __name__ == "__main__":
    if n+m % 2 == 1:
        ans = get_kth_smallest((n+m) // 2 - 1)
    else:
        l = get_kth_smallest((n+m) // 2 - 1)
        r = get_kth_smallest((n+m) // 2)
        ans = (l + r) / 2
    print(ans)
    