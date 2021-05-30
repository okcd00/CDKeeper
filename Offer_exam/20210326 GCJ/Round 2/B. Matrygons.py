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

# Problem 
if False:
    sys.stdin = open('./Offer_exam/20210326 GCJ/Round 2/B.in', 'r')
    # sys.stdout = open('./Offer_exam/20210326 GCJ/Round 1B/A.out', 'w')

def read_int_list(): 
    return list(map(int, input().split()))
def read_int_tuple(): 
    return tuple(map(int, input().split()))
def read_int(): 
    return int(input())

N = int(1e6) + 1
pvis = [0] * N
pri = [0] * N
prin = 0

def preprocess_prime_list():
    prin = 0
    for i in range(2, N):
        if pvis[i] == 0: 
            pri[prin] = i
            prin += 1
        for j in range(0, prin):
            if pri[j] * i >= N:
                break
            pvis[pri[j]*i] = 1
            if i % pri[j] == 0:
                break


# Problem 
import copy, math
preprocess_prime_list()  # pvis[i] = 1 means not a prime
prime_list = [i for i, t in enumerate(pvis) if t == 0]

t = read_int()
for case_idx in range(t):
    ans = 1
    n = read_int()
    ori_n = copy.copy(n)
    if pvis[n] == 0:
        ans = 1
        print("Case #{}: {}".format(case_idx + 1, ans))
        continue

    ans_queue = []
    rig = int(math.ceil(math.sqrt(n)))
    for pr in range(3, 1 + rig):
        if n % pr == 0:
            if n / (n // pr) - 1 >= 2:
                ans_queue.append([1, pr - 1, [n // pr]])
            if n / pr - 1 >= 2:
                ans_queue.append([1, int(n / pr) - 1, [pr]])

    ans_list = []
    while ans_queue:
        _ans, _n, _q = ans_queue[0]
        del ans_queue[0]
        if _n == 1:
            if _ans > ans:
                ans = _ans
                ans_list = _q
            continue

        components = []
        # print(_n)
        # print(math.sqrt(_n))
        rig = int(math.ceil(math.sqrt(_n)))
        for pr in range(2, 1 + rig):  # prime_list[2:]:
            if _n % pr == 0:
                if _n / pr - 1 >= 2:
                    components.append(pr)
                if pr - 1 >= 2:
                    components.append(n // pr)
        
        # print(_ans, _n, _q, components)
        for pr in components:
            if int(_n // pr) - 1 >= 2:
                item = [_ans+1, int(_n // pr) - 1, _q + [int(_q[-1] * pr)]]
                ans_queue.append(item)
        item = [_ans+1, 1, _q + [int(_q[-1] * _n)]]
        ans_queue.append(item)

    print("Case #{}: {}".format(case_idx + 1, ans))
    # print(ori_n, ans_list)

