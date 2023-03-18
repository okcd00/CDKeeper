from collections import defaultdict

n, k = list(map(int, input().strip().split()))
s = list(map(int, input().strip().split()))

ret = 0
lef = 0
color_diversity = 0
color_count = defaultdict(int)  # 2000
for rig, c in enumerate(s):
    color_count[c] += 1
    if color_count[c] == 1:  # 0 -> 1
        color_diversity += 1
        while color_diversity > k:
            lef += 1
            color_count[s[lef-1]] -= 1
            if color_count[s[lef-1]] == 0:  # 1 -> 0
                color_diversity -= 1
    # print(lef, rig, rig-lef+1, color_diversity)
    ret = max(ret, rig - lef + 1)
print(ret)

"""
8 3
1 2 3 2 1 4 5 1
"""