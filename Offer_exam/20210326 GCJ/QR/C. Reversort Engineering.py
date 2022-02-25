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
t = read_int()
for case_idx in range(t):
    n, c  = read_int_list()
    a = list(range(1, n + 1))
    min_value = n - 1
    max_value = ((2 + n) * (n - 1)) // 2
    if c < min_value or c > max_value:
        print("Case #{}: {}".format(case_idx + 1, "IMPOSSIBLE"))
        continue
    c -= (n - 1)
    for idx in range(1, n):
        if c == 0:
            break
        pivot = (n - 1) - idx
        max_reverse_length = n - 1 - pivot
        cur_cost = min(c, max_reverse_length)
        reverse_boundary = pivot + cur_cost
        reverse_boundary += 1  # for range(l, r+1)
        c -= cur_cost
        # print('>', pivot, reverse_boundary-1)
        a = a[:pivot] + a[pivot: reverse_boundary][::-1] + a[reverse_boundary:]
        # print('list:', *a)
    print("Case #{}:".format(case_idx + 1), end=' ')
    print(*a)

