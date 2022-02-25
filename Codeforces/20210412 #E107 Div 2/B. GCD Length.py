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

import math
# Problem 

def gen():
    with open('./B.in', 'w') as f:
        f.write('285\n')
        for a in range(1, 10):
            for b in range(1, 10):
                for c in range(1, 10):
                    if c <= min(a, b):
                        f.write('{} {} {}\n'.format(a,b,c))

# sys.stdin = open('./B.in', 'r')

t = read_int()
for case_idx in range(t):
    a, b, c = read_int_list()
    # gcd_xy = int(''.join(['1'] * c))
    z = 11 ** (c - 1) + 1
    x = 11 ** (a - c) * z
    y = 11 ** (b - c) * z
    if a > b:
        x += z
    else:
        y += z
    print(x, y)
    # if len(str(x)) != a or len(str(y)) != b or len(str(math.gcd(x, y))) != c:
        # print(x, y)
        # print(a, b, c)
        # print(x, y, z, math.gcd(x, y))
        # break