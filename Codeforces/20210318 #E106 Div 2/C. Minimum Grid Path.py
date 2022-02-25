import os
import sys 
from io import BytesIO, IOBase
 
BUFSIZE = 8192
 
class FastIO(IOBase):
    newlines = 0
 
    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None
 
    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()
 
    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
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

# Problem C

t = read_int()
for _ in range(t):
    n = read_int()
    c = read_int_list()
    hor = c[0::2]
    ver = c[1::2]
    
    # store min value in segments
    ans = -1
    min_cost_h, min_cost_v = -1, -1
    cum_sum_h, cum_sum_v = 0, 0
    cost_each_h, cost_each_v = 0, 0

    total_cost_list_h = []
    total_cost_list_v = []
    cur_cost_h, cur_cost_v = -1, -1

    for end_pos, value in enumerate(c):
        
        if end_pos % 2 == 0:
            h_pos = end_pos // 2
            h_value = value
            if min_cost_h < 0 or min_cost_h > h_value:
                min_cost_h = h_value

            cost_each_h += hor[h_pos]
            cost_peak = (n - h_pos - 1) * min_cost_h
            cost_hor = cost_each_h + cost_peak
            cur_cost_h = cost_hor
        else:
            v_pos = (end_pos - 1) // 2
            v_value = ver[v_pos]
            if min_cost_v < 0 or min_cost_v > v_value:
                min_cost_v = v_value
            cost_each_v += ver[v_pos]
            cost_peak = (n - v_pos - 1) * min_cost_v
            cost_ver = cost_each_v + cost_peak
            cur_cost_v = cost_ver

        if cur_cost_h < 0 or cur_cost_v < 0:
            continue
        cost = cur_cost_h + cur_cost_v
        if ans < 0 or ans > cost:
            ans = cost

    print(ans)