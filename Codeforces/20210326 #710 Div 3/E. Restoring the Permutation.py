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


# Problem 
import bisect
def lower_bound(num_list, target_num):
    return bisect.bisect_left(
        num_list, target_num, lo = 0, hi = len(num_list))


t = read_int()
for _ in range(t):
    n = read_int()
    q = read_int_list()
    
    pivot, i, j = 1, 0, 0
    rest_min, rest_max = [], []
    ans_min, ans_max = [], []
    
    while i < n:
        rest_min.extend(list(range(pivot, q[i])))
        rest_max.extend(list(range(pivot, q[i])))
        pivot = q[i] + 1
        x = q[i]
        # print('>', pivot, q[i])
        ans_min.append(x)
        ans_max.append(x)
        i += 1
        if i >= n:
            break
        while q[i] == x:
            ans_min.append(rest_min[j])
            j += 1
            ans_max.append(rest_max.pop())
            i += 1
            if i == n:
                break
    
    print(*ans_min)
    print(*ans_max)
