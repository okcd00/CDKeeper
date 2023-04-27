import sys

# Only passed 85.71% cases
t = int(sys.stdin.readline().strip())
ans = 0
for i in range(t):
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    a = list(map(int, line.split()))
    
    has_answer = False
    for i, lef in enumerate(a):
        if has_answer:
            break
        for j in range(i+1, len(a)):
            rig = a[j]
            v = lef * rig
            if v ** 0.5 != int(v ** 0.5):
                print(lef, rig)
                has_answer = True
                break
    else:
        print(-1, -1)
# print(ans)