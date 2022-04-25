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


t = read_int()
INF = 99999999999
from pprint import pprint

for case_idx in range(t):
    n, p = read_int_list()

    x = [[0 for _ in range(p+1)]]
    for i in range(1, n+1):
        x.append(sorted(read_int_list()))
    # pprint(x)

    dp = [[INF for _ in range(p+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(0, p):
            for k in range(0, p):
                # print('->', i, j, k)
                sup  = abs(x[i][p-1] - x[i-1][j])  # top
                sup += abs(x[i][p-1] - x[i][0])  # bottom
                sup += abs(x[i][0] - x[i][k])
                sdw  = abs(x[i-1][j] - x[i][0])  # bottom
                sdw += abs(x[i][0] - x[i][p-1])
                sdw += abs(x[i][p-1] - x[i][k])
                tmp = min(sup, sdw)
                dp[i][k] = min(dp[i][k], dp[i-1][j] + tmp)

    ret = INF
    for i in range(0, p):
        ret = min(ret, dp[n][i])

    print("Case #{}: {}".format(case_idx + 1, ret))
    