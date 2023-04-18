# encoding: utf-8
# a = input("please input a number:")


def total_raindrops(heights):
    cur_max = 0
    max_left = []
    for i, h in enumerate(heights):
        if i == 0:
            max_left.append(0)
            cur_max = max(cur_max, h)
            continue
        max_left.append(cur_max)
        cur_max = max(cur_max, h)

    cur_max = 0
    max_right = []
    for i, h in enumerate(heights[::-1]):
        if i == 0:
            max_right.append(0)
            cur_max = max(cur_max, h)
            continue
        max_right.append(cur_max)
        cur_max = max(cur_max, h)
    max_right = max_right[::-1]

    ret = 0
    for i, h in enumerate(heights):
        ret += max(0, min(max_left[i], max_right[i]) - h)
    return ret

"""
x    x
xx   xx x
xxx xxxxxx 
"""

rain_drops = [0,1,3,2,1,0,1,3,2,1,2,1]
print(total_raindrops(rain_drops))
