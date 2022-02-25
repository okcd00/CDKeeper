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
    sys.stdin = open('./Offer_exam/20210326 GCJ/Round 1B/A.in', 'r')
    # sys.stdout = open('./Offer_exam/20210326 GCJ/Round 1B/A.out', 'w')


import copy
from itertools import permutations
t_nanosecond = 1
t_second = int(1e9) * t_nanosecond
t_minutes = 60 * t_second
t_hour = 60 * t_minutes
t_round = 12 * t_hour


def solve(a, b, c):
    # h, m, s hands
    for more in range(0, 20):
        over = b + more * t_round - a
        if over >= 0 and over % 11 == 0:
            t = over // 11
            if t > t_round:
                return []
            if (a + 719 * t) % t_round == c:
                return [t//(t_hour), t//(t_minutes)%60, t//(t_second)%60, t%t_second]
    return []


t = read_int()
for case_idx in range(t):
    print("Case #{}:".format(case_idx + 1), end=' ')

    for a, b, c in list(permutations(read_int_list())):
        ans = solve(a, b, c)
        if ans:
            break
    print(*ans)
