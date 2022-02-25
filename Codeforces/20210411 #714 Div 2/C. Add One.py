import os
import sys 
from io import BytesIO, IOBase
 

class FastIO(IOBase):
    newlines = 0
    BUFSIZE = 8192
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self.BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, self.BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()
 
    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)
 
 
class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")
 
 
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")


def read_int_list(): 
    return list(map(int, input().split()))
def read_int_tuple(): 
    return tuple(map(int, input().split()))
def read_int(): 
    return int(input())


MOD = 10**9 + 7
FACT_ARR = [1]
EXP_ARR = [1]
 

def fact(x, MOD=0):
    """
    fact table, output x!
    """
    if MOD:
        while x >= len(FACT_ARR):
            FACT_ARR.append(FACT_ARR[-1] * len(FACT_ARR) % MOD)
    else:
        while x >= len(FACT_ARR):
            FACT_ARR.append(FACT_ARR[-1] * len(FACT_ARR))
    return FACT_ARR[x]

def exp2(x, MOD=0):
    while x >= len(EXP_ARR):
        EXP_ARR.append(EXP[-1] * 2 % MOD)
    return EXP_ARR[x]

def counts(num, jumps):
    cycles = jumps // 10
    ret = exp2(cycles)
    for r in range(jumps % 10, 0, -1):
        ret += 0
    return ret

# Problem C (Not-solved)
import copy
t = read_int()
for case_idx in range(t):
    ans = 0
    n, m = read_int_list()
    count = [0] * 10
    for i, d in enumerate(str(n)):
        count[int(d)] += 1
    # for i, d in enumerate(count):
    #     ans += (get_count(d, m+i)) % MOD
    for i in range(m):
        new_count = [0] * 10
        for j, c in enumerate(count):
            if j + 1 == 10:
                new_count[0] += count[j]
                new_count[1] += count[j]
            else:
                new_count[(j+1)%10] += count[j]
        print(new_count[-1], sum(new_count))
        count = copy.copy(new_count)
    print(ans)