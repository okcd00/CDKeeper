import sys
from bisect import bisect_left, bisect_right


def solve():
    # clear 70% cases
    n, x = list(map(int, sys.stdin.readline().strip().split()))
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    # [0, x, x, x, x, MAXVALUE]
    cumsum = [0]
    for v in a:
        cumsum.append(cumsum[-1] + v)
    cumsum.append(cumsum[-1] + x + 1)
    ret = 0
    for i, v in enumerate(a):
        lef_boundary = 0
        if cumsum[i+1] >= x:
            lef_boundary = bisect_right(cumsum, cumsum[i+1] - x + 0.5)
            # print(cumsum[i+1] - x + 0.5, 'at', lef_boundary)
            lef_boundary += 1
        rig_boundary = 0
        if cumsum[-2] - cumsum[i] >= x:
            rig_boundary = bisect_right(cumsum, cumsum[i] + x - 0.5)
            # print(cumsum[i] + x - 0.5, 'at', rig_boundary)
        invalid_size = max(0, rig_boundary - max(1, lef_boundary))
        ret += n - invalid_size
        # print(cumsum)
        # print(f"Invalid at [{lef_boundary}:{rig_boundary}], they are {cumsum[lef_boundary:rig_boundary]}")
        # print(f"[{i}] {v}: +{n - invalid_size}")
    print(ret)


def solve2():
    # clear all cases
    n, x = list(map(int, sys.stdin.readline().strip().split()))
    a = list(map(int, sys.stdin.readline().strip().split()))
    
    # [0, x, x, x, x, MAXVALUE]
    cumsum = [0]
    for v in a:
        cumsum.append(cumsum[-1] + v)
    cumsum.append(cumsum[-1] + x + 1)
    
    ret = 0
    lef_pivot = 0
    rig_pivot = 1
    # print(cumsum)
    for i, v in enumerate(a):
        while cumsum[lef_pivot] <= cumsum[i+1] - x:
            lef_pivot += 1
        if rig_pivot < n + 1:
            while cumsum[rig_pivot] < cumsum[i] + x:
                rig_pivot += 1
        # print(lef_pivot, cumsum[lef_pivot], rig_pivot, cumsum[rig_pivot])
        invalid_size = max(0, rig_pivot-1 - lef_pivot)
        ret += n - invalid_size
        # print(i, v, cumsum[lef_pivot+1:rig_pivot-1], lef_pivot+1, rig_pivot-1, invalid_size)
        # print('+', n - invalid_size)
    print(ret)

    
if __name__ == "__main__":
    solve2()
