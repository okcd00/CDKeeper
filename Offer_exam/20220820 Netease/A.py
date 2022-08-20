n = int(input().strip())

# position(-1): val
v = list(map(int, input().strip().split()))

# val: position(-1)
position = {val: pos for pos, val in enumerate(v)}

# simulation
ret = []
pivot = n - 1
while pivot:
    while v[pivot] != pivot + 1:
        swap_position = position[v[pivot] + 1]
        # position update
        position[v[pivot]], position[v[pivot]+1] = swap_position, pivot
        # value update
        v[pivot], v[swap_position] = v[swap_position], v[pivot]
        ret.append(f"{pivot+1} {swap_position+1}")
        # print(v)
    pivot -= 1

# print results
print(len(ret))
for line in ret:
    print(line)