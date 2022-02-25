T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    S = set()
    flag = True
    for _ in range(n):
        arr = input().strip().split()
        arr = '-'.join(sorted([x for x in arr]))
        if arr in S:
            print('YES')
            flag = False
            break
        else:
            S.add(arr)
    if flag:
        print('NO')


