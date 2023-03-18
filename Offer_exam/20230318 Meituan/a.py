# from pprint import pprint
from collections import defaultdict
n, a, b = list(map(int, input().strip().split()))

enemy = defaultdict(int)
max_x = 0  # 最大横坐标
max_y = 0  # 最大纵坐标
for i in range(n):
    x, y = list(map(int, input().strip().split()))    
    if x > max_x:
        max_x = x 
    if y > max_y:
        max_y = y
    enemy[(x, y)] += 1
# print(enemy)

record = [[0 for _j in range(max_y+1)] for _i in range(max_x+1)]
# 记录 = 上+左-左上+(1 if 有 else 0)
for x in range(1, max_x + 1):
    for y in range(1, max_y + 1):
        record[x][y] = record[x-1][y] + record[x][y-1] - record[x-1][y-1] + enemy[(x, y)]
# pprint(record)

max_catch = 0
# 捕获 = 矩形右下+左上-左下-右上?
for x in range(1, max_x + 1):
    for y in range(1, max_y + 1):
        x_right = min(max_x, x+a)
        y_down = min(max_y, y+b)
        catch = record[x_right][y_down] + record[x-1][y-1] - record[x-1][y_down] - record[x_right][y-1]
        # print(x,y,x_right,y_down,'|',catch)
        if catch > max_catch:
            max_catch = catch
print(max_catch)

"""
5 1 2
1 1
2 2
3 3
1 3
1 4
"""