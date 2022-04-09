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


def isSumSubset(arr, arrLen, requiredSum):
    """
    >>> isSumSubset([2, 4, 6, 8], 4, 5)
    False
    >>> isSumSubset([2, 4, 6, 8], 4, 14)
    True
    """
    # a subset value says 1 if that subset sum can be formed else 0
    # initially no subsets can be formed hence False/0
    subset = [[False for i in range(requiredSum + 1)] for i in range(arrLen + 1)]

    # for each arr value, a sum of zero(0) can be formed by not taking any element
    # hence True/1
    for i in range(arrLen + 1):
        subset[i][0] = True

    # sum is not zero and set is empty then false
    for i in range(1, requiredSum + 1):
        subset[0][i] = False

    for i in range(1, arrLen + 1):
        for j in range(1, requiredSum + 1):
            if arr[i - 1] > j:
                subset[i][j] = subset[i - 1][j]
            if arr[i - 1] <= j:
                subset[i][j] = subset[i - 1][j] or subset[i - 1][j - arr[i - 1]]

    # uncomment to print the subset
    # for i in range(arrLen+1):
    #     print(subset[i])
    print(subset[arrLen][requiredSum])


def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if nums == []:
        return True
    if sum(nums) % 2 == 1:
        return False
    target = sum(nums) // 2
    print(target)
    dp = [0] * (target + 1)
    dp[0] = 1
    for n in nums:
        i = target
        while(i >= n):
            dp[i] = dp[i] + dp[i-n]
            i = i - 1
    if dp[target] >= 2:
        return True
    else:
        return False


def lowbit(_val):
    return _val & -_val

# Problem 
t = read_int()
for case_idx in range(t):
    n = read_int()
    hacked_list = [1 << _i for _i in range(min(n, 30))]  # fixed 30
    # for i, v in enumerate(hacked_list):  print(i, v)
    other_numbers = [int(1e7) * _i for _i in range(1, 70+1)]
    other_numbers_sum = 24850000000
    print(' '.join(map(str, hacked_list + other_numbers)))
    # print(len(hacked_list + other_numbers))
    sys.stdout.flush()
    response = read_int_list()
    if response == [-1]:
        break
    response_sum = sum(response)
    half_value = (response_sum + hacked_list[-1] * 2 - 1 + other_numbers_sum) // 2
    candidates = sorted(response + other_numbers)
    cur_sum, pivot = 0, 0
    while half_value - cur_sum > int(1e9):
        cur_sum += candidates[pivot]
        pivot += 1
    ret = candidates[:pivot]
    rest_val = half_value - cur_sum
    while rest_val:
        _lb = lowbit(rest_val)
        ret.append(_lb)
        rest_val -= _lb
    print(' '.join(map(str, ret)))
    # print(sum(ret), half_value)
    sys.stdout.flush()        
        
