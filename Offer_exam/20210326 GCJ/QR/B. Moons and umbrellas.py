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
    x, y, s = input().split()
    x, y = int(x), int(y)
    ans = 0
    blanks = 0
    pivot = 'X'
    for idx, c in enumerate(s):
        if c == '?':
            blanks += 1 
            continue
        if pivot == 'X':
            # 1: ?J -> CJ -> 0 more pair + x?
            # 1: ?C -> JC -> 0 more pair + y?
            # 2: ??J -> JCJ / CJJ -> 0~1 more pair + x?
            # 2: ??C -> CJC / JCC -> 0~1 more pair + y?
            # 3: ???J -> CJCJ / JCCJ -> 0~1 more pair + x
            # 3: ???C -> CJCC / JCJC -> 0~1 more pair + y
            if c == 'J':
                if x < 0:
                    # ans += x
                    pivot = 'C'
                else:
                    pivot = 'J'
                blanks -= 1
            if c == 'C':
                if y < 0:
                    # ans += y
                    pivot = 'J'
                else:
                    pivot = 'C'
                blanks -= 1
        # 1: C?J -> 0 more
        # 2: C??J -> CJCJ / CJCJ -> 1 more pair
        # 3: C???J -> CJCJJ / CCJCJ -> 1 more pair
        # 4: C????J -> CJCJCJ -> 2 more pair
        # J..C / C..J are the same
        # 2: C??C -> CJCC / CCJC -> 1 more pair
        # 3: C???C -> CJCJC / CCJCC -> 0~2 more pair
        if x + y < 0:
            if pivot == c:
                ans += ((blanks + 1) // 2) * (x + y)  # mid bonus
            else:
                ans += (blanks // 2) * (x + y)  # mid bonus
            blanks = 0
        if c != pivot:
            pr = pivot + c
            if pr == 'CJ':
                ans += x
                pivot = c
            elif pr == 'JC':
                ans += y
                pivot = c
    else:
        if blanks:
            # 1: J? -> 0 + y?
            # 1: C? -> 0 + x?
            # 2: J?? -> 0~1 or y?
            # 2: C?? -> 0~1 or x?
            if pivot == 'J':
                if y < 0:
                    ans += y
                    # c = 'C'
                blanks -= 1
            if pivot == 'C':
                if x < 0:
                    ans += x
                    # c = 'J'
                blanks -= 1
            if x + y < 0:
                if pivot == c:
                    ans += ((blanks + 1) // 2) * (x + y)  # mid bonus
                else:
                    ans += (blanks // 2) * (x + y)  # mid bonus
                blanks = 0
    print("Case #{}: {}".format(case_idx + 1, ans))
