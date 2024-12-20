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
n, k = read_int_list()
if k == 1:
    print('a' * n)
else:
    ans = 'a'
    s = 'abcdefghijklmnopqrstuvwxyz'
    lef_pivot = 0
    rig_pivot = 0
    for i in range(n):
        lef = s[lef_pivot].strip()
        rig = s[rig_pivot].strip()
        rig_pivot += 1
        if lef == rig:
            continue
        
        ans += lef
        if len(ans) == n:
            break

        ans += rig
        if len(ans) == n:
            break

        if rig_pivot == k:
            rig_pivot = lef_pivot + 1
            lef_pivot += 1
            ans += s[lef_pivot].strip()
            if lef_pivot == k - 1:
                # print('->', s[k].strip())
                break
        if len(ans) == n:
            break
    if len(ans) != n:
        times = n // len(ans)
        rest = n % len(ans)
        ans = ans * times + ans[:rest]
    print(ans)