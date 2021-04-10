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
fake_list = [5, 3, 7, 1, 2, 4, 6, 8, 9, 10]

def read_int_list(): 
    return list(map(int, input().split()))
def read_int_tuple(): 
    return tuple(map(int, input().split()))
def read_int(): 
    return int(input())

def get_respond_fake(a, b, c):
    _index = map(lambda x: fake_list[x], [a-1, b-1, c-1])
    _mid_index = sorted(_index)[1]
    return fake_list.index(_mid_index) + 1

def get_respond(a, b, c):
    print(a, b, c, flush=True)
    # return get_respond_fake(a, b, c)
    return read_int()

def quick_sort(data, l=None, r=None):    
    """快速排序"""    
    if len(data) >= 2:  # 递归入口及出口      
        # 选取基准值  
        mid_mark = data[0]
        if (l is None) and (r is None):
            # at the beginning
            lef_mark = data[1]
            right_mark = data[2]
        else:
            lef_mark = l if l is not None else data[1]
            right_mark = r if r is not None else data[1]

        # print(lef_mark, right_mark, mid_mark, end='->')
        mid = get_respond(lef_mark, right_mark, mid_mark) 
        if mid == lef_mark:
            mid_mark, lef_mark = lef_mark, mid_mark
        elif mid == right_mark:
            mid_mark, right_mark = right_mark, mid_mark
        # print(lef_mark, right_mark, mid_mark)

        # 定义基准值左右两侧的列表   
        left, right = [], []       

        # 从原始数组中移除基准值        
        for num in data:            
            if num == mid_mark:
                continue
            if num == lef_mark:
                left.append(num)
                continue        
            elif num == right_mark:
                right.append(num)
                continue
            mid = get_respond(lef_mark, mid_mark, num)
            if mid_mark == mid:                
                right.append(num)            
            else:                
                left.append(num)        
        
        results = quick_sort(left, l=None, r=mid_mark) + [mid_mark] + \
                  quick_sort(right, l=mid_mark, r=None)
        # print(data, 'to', results)
        # print(list(map(lambda x: fake_list[x-1], data)), 'to', 
        #       list(map(lambda x: fake_list[x-1], results)))
        return results
    else:        
        return data


# Problem 
t, n, q  = read_int_list()
for case_idx in range(t):
    data = list(range(1, n + 1))
    print(*quick_sort(data), flush=True)
    result = read_int()
    if result == -1:
        break