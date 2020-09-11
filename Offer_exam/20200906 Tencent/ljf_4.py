T = int(input())
for i in range(T):
    n = int(input())
    rings = []
    Flag = False
    for j in range(n):
        values = input().split(' ')
        #values = [int(value) for value in values]
        rings.append(sorted(values))
    C = set()
    Flag = False
    #import pdb; pdb.set_trace()
    for ring in rings:
        ring_str = '*'.join(ring)
        if ring_str in C:
            Flag = True
            print('YES')
        else:
            C.add(ring_str)
    if not Flag:
        print('NO')


""" def is_same(n, rings):
        for i in range(len(rings)):
            rings[i] = sorted(rings[i])
        for i in range(n-1):
            for j in range(i+1, n):
                if rings[i] != rings[j]:
                    continue
                else:
                    return True
        return False

T = int(input())
for i in range(T):
    n = int(input())
    rings = []
    Flag = False
    for j in range(n):
        values = input().split(' ')
        values = [int(value) for value in values]
        rings.append(values)

    if is_same(n, rings):
        print('YES')
    else:
        print('NO') """