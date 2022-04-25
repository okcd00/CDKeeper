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


import random
CANDIDATES = [f"{bin(x)[2:]:>08s}" for x in range(256)]
# print(CANDIDATES[:10])
# sys.stdout.flush()


def flatten(nested_list, unique=False):
    ret = [elem for sub_list in nested_list for elem in sub_list]
    if unique:
        return list(set(ret))
    return ret


def update_candidates(candidates, my_response):
    ret = [[c] for c in candidates]
    return list(set(flatten(ret)))


# Problem 
t = read_int()
for case_idx in range(t):
    ret = 0
    # at first, Judge has a value x
    print("11111111")
    sys.stdout.flush()
    response = read_int()  
    if response == 0:
        continue

    while True:
        indexes = random.sample(
            list(range(8)), k=response)
        my_response = ['1' if i in indexes else '0' for i in range(8)]
        print(''.join(my_response))  # my string
        sys.stdout.flush()

        response = read_int()  
        if response in [1, 4, 7]:
            print("00000001")
            sys.stdout.flush()
            response = read_int()  
        if response == 0:
            # success
            break
        if response == -1:
            # failed
            break

