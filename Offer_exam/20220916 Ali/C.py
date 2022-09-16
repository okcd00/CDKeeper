n = int(input().strip())
a = list(map(int, input().strip().split()))

# print(bin(128))

root = min(a)
a = [divmod(v, root) for v in a]
if sum([rest for times, rest in a]) > 0:
    print(-1)
else:
    a = [bin(times)[2:] for times, rest in a]
    if sum(['1' in _b[1:] for _b in a]) > 0:
        print(-1)
    else:
        a = [len(bin_str)-1 for bin_str in a]
        target = max(a)
        a = [target - v for v in a]
        ans = 0
        for i, v in enumerate(a + [0]):
            if i == 0:
                continue
            if v < a[i-1]:
                ans += a[i-1] - v
        print(ans)
