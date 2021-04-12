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


# Problem 
t = read_int()
for case_idx in range(t):
    ans = 0
    n = read_int()
    aa = read_int_list()
    # a = list(map(lambda x: bin(x)[2:], aa))

    # max_len = max(map(len, a))
    # a = [_e.zfill(max_len) for _e in a]
    # print(*a)

    mask = (1 << 31) - 1
    for i in range(31):
        if 0 not in [b & (1 << i) for b in aa]:
            mask -= 1 << i
                
    boundary = 0
    for i, e in enumerate(aa):
        # print(bin(e), bin(mask))
        if e & mask == 0:
            boundary += 1
    # print(boundary)
    b_candidates = (boundary * (boundary - 1)) % MOD
    print(b_candidates * fact(n-2, MOD) % MOD)