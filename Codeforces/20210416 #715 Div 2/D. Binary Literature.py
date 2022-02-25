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


def solve(s1,s2,c):
    ans, i, j, n = [], 0, 0, len(s1)
    while True:
        while j<n and s1[j]!=c:
            ans.append(s1[j])
            j+=1
        while i<n and s2[i]!=c:
            ans.append(s2[i])
            i+=1
        if i==n and j==n:
            return "".join(ans)
        elif i==n:
            ans.append(s1[j])
            j+=1
        elif j==n:
            ans.append(s2[i])
            i+=1
        else:
            ans.append(c)
            i,j=i+1,j+1


def main():
    n = read_int()
    a = [input().rstrip() for _ in range(3)]
    for x,y in combinations([0,1,2], 2):
        if a[x].count("0")>=n and a[y].count("0")>=n:
            return solve(a[x], a[y], "0")
        if a[x].count("1")>=n and a[y].count("1")>=n:
            return solve(a[x], a[y], "1")


# Problem 
from copy import copy
from itertools import combinations
t = read_int()
for _ in range(t):
    print(main())

