from collections import defaultdict

n, k = list(map(int, str(input()).strip().split(' ')))
arr = list(map(int, str(input()).strip().split(' ')))

"""
6 5
5 6 7 8 9 10
"""

maxv = max(arr)
n_bucket = maxv // k + 1
buckets = [defaultdict(int) for _ in range(n_bucket)]
# print(buckets)

# bucketing O(n)
for v in arr:
    t = v // k
    r = v % k
    buckets[t][r] += 1

ans = 0
for t, bucket in enumerate(buckets):
    if len(bucket) == 0:
        continue
    if t >= n_bucket - 1 or len(buckets[t+1]) == 0:
        continue
    next_bucket = buckets[t+1]
    for r, count in bucket.items():
        aibo = next_bucket.get(r,0)
        if aibo > 0:
            ans += count * aibo

# print(buckets)
print(ans)