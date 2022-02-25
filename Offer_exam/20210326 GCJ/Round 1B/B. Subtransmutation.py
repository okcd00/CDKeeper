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

DEBUG = False

# Problem 
if DEBUG:
    sys.stdin = open('./Offer_exam/20210326 GCJ/Round 1B/B.in', 'r')


import copy
N = 100010
n = -1
a = [0] * N
cnt = [0] * N
A, B = 0, 0
LIMIT = int(1e3)
INF = int(1e15) - 1

def check_valid(st):
    for i in range(101):
        cnt[i] = 0
    cnt[st] = 1
    flag = True
    for i in range(st, 99, -1):
        if cnt[i]:
            cnt[i-A] += cnt[i]
            cnt[i-B] += cnt[i]
            cnt[i-A] = min(cnt[i-A], INF)
            cnt[i-B] = min(cnt[i-B], INF)
            cnt[i] = 0

    for i in range(99, 0, -1):
        if a[i] > 0 or cnt[i] > 0:
            if cnt[i] < a[i]:
                flag = False
                break
            if i > A:
                cnt[i-A] = min(cnt[i-A] + cnt[i] - a[i], INF)
            if i > B:
                cnt[i-B] = min(cnt[i-B] + cnt[i] - a[i], INF)
            cnt[i] -= a[i]

    return flag


t = read_int()
for case_idx in range(t):
    for i in range(101):
        a[i] = 0
    n, A, B = read_int_list()
    _a = read_int_list()
    for i, v in enumerate(_a):
        a[i+1] = v
    lb = 0
    ub = -1
    for i in range(1, LIMIT + 1):
        if check_valid(i):
            ub = i
            break
    if ub != -1:
        print("Case #{}: {}".format(case_idx + 1, ub))
    else:
        print("Case #{}: {}".format(case_idx + 1, "IMPOSSIBLE"))