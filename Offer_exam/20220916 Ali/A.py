from collections import defaultdict
k = int(input().strip())
s = input().strip()

candidates = defaultdict(int)
origin_length = len(s)

for i, c in enumerate(s):
    if i == 0:
        continue
    if c == s[i-1]:
        candidates[c] += 1

# print(candidates)
        
reduce = 0
_ord_a = ord('a')
for i in range(26):  # 0~25 'a'~'z'
    rest = candidates[chr(_ord_a + i)]
    if i + 1 > k:
        break
    if rest:
        take = min(k // (i+1), rest)
        k -= take * (i+1)
        reduce += take
        
print(origin_length - reduce)