candidates = """
rededrdre
rdedererd
reddreedr
rdeerdder
erdrdeder
drerededr
dreedrred
erdderrde
edrdrered
dererdrde
derrdeerd
edrreddre
"""
candidates = [line.strip() for line in candidates.split('\n') if line.strip()]

def dist(src, dest):
    return sum([a != b for a, b in zip(src, dest)])

t = int(input().strip())
for _ in range(t):
    r = input().strip() 
    r += input().strip()
    r += input().strip()
    ans = min([dist(r, cand) for cand in candidates])
    print(ans)
