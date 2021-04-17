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
    n = read_int()
    a = input()
    tc = a.count('T')
    mc = a.count('M')
    if mc == 0:
        print("NO")
        continue
    if tc / mc != 2:
        print("NO")
        continue
    
    ts = []
    ms = []
    for i, c in enumerate(a):
        if c == 'T':
            ts.append(i)
        else:
            # ms.append((i, len(ts), tc - len(ts)))
            ms.append(i)

    flag = "YES"
    for m_idx, m_pos in enumerate(ms):
        lef = ts[m_idx]
        # print(lef, m_pos, '>')
        if m_pos < lef:
            flag = "NO"

    for m_idx, m_pos in enumerate(ms[::-1]):
        rig = ts[len(ts) - 1 - m_idx]
        # print('<', m_pos, rig)
        if m_pos > rig:
            flag = "NO"

    print(flag)