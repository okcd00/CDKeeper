from heapq import *
from bisect import *
from itertools import *
from functools import *
from collections import *
from math import gcd, ceil, sqrt, floor, inf
from operator import add, mul, sub, xor, truediv, floordiv
 
#------------------------------------------------------------------------

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
 
 
#------------------------------------------------------------------------
sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip("\r\n")

def read_int_list(): 
    return list(map(int, input().split()))
def read_int_tuple(): 
    return tuple(map(int, input().split()))
def read_int(): 
    return int(input())
#------------------------------------------------------------------------
 
 
def bootstrap(f, stack=[]):
    from types import GeneratorType
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
 
    return wrappedfunc
 

MOD = 10**9 + 7
FACT_ARR = [1]
FACTI_ARR = []
 

def fact(x, MOD=0):
    """
    fact(x) = x! = x * (x-1) * ... * 2 * 1
    """
    if MOD:
        while x >= len(FACT_ARR):
            FACT_ARR.append(FACT_ARR[-1] * len(FACT_ARR) % MOD)
    else:
        while x >= len(FACT_ARR):
            FACT_ARR.append(FACT_ARR[-1] * len(FACT_ARR))
    return FACT_ARR[x]
 

def ifact(x, MOD=0):
    """
    a * ifact(x) == a / fact(x)
    """
    global FACTI_ARR
    fact(x, MOD)
    FACTI_ARR.append(pow(FACT_ARR[-1], MOD-2, MOD))
    for i in range(x,0,-1):
        FACTI_ARR.append(FACTI_ARR[-1] * i % MOD)
    FACTI_ARR.reverse()
 

def per(i, j, MOD=0):
    """calculate P_ij: permutation"""
    if i < j: 
        return 0
    if not MOD:
        return fact(i) // fact(i-j)
    return FACT_ARR[i] * FACTI_ARR[i-j] % MOD


def com(i, j, MOD=0):
    """calculate C_ij: combination"""
    if i < j: 
        return 0
    if not MOD:        
        return per(i, j) // fact(j)
    return per(i, j, MOD) * FACTI_ARR[j] % MOD
 

def catalan(n):
    return com(2 * n, n) // (n + 1)
 

def isprime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
 

def floorsum(a, b, c, n):  # sum((a*i+b)//c for i in range(n+1))
    if a == 0:
        return b // c * (n + 1)
    if a >= c or b >= c: 
        ret = floorsum(a=a%c, b=b%c, c=c, n=n) 
        ret += b // c * (n+1) + a // c * n * (n+1) // 2
        return ret
    m = (a * n + b) // c
    return n * m - floorsum(c, c-b-1, a, m-1)
 

def inverse(a, m):
    a %= m
    if a <= 1: 
        return a
    return ((1 - inverse(m, a) * m) // a) % m
 

def lowbit(n):
    return n & -n
 

class BIT:
    """Shu Zhuang Shu Zu"""
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr) - 1
        
    def update(self, x, v):
        while x <= self.n:
            self.arr[x] += v
            x += x & -x
 
    def query(self, x):
        ans = 0
        while x:
            ans += self.arr[x]
            x &= x - 1
        return ans
 

class ST:
    """BeiZeng RMQ"""
    def __init__(self,arr):  # n != 0
        n = len(arr)
        mx = n.bit_length()  # not reachable
        self.st = [[0] * mx for i in range(n)]
        for i in range(n):
            self.st[i][0] = arr[i]
        for j in range(1, mx):
            for i in range(n-(1<<j)+1):
                self.st[i][j] = max(self.st[i][j-1], self.st[i+(1<<j-1)][j-1])
    
    def query(self, l, r):
        if l > r:
            return -inf
        s=(r+1-l).bit_length()-1
        return max(self.st[l][s], self.st[r-(1<<s)+1][s])

   
class UFS: 
    """Union Find Set"""
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.ranks = [0] * n
 
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
 
    def union(self, u, v):
        pu, pv=self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.ranks[pu] >= self.ranks[pv]:
            self.parent[pv] = pu
            if self.ranks[pv] == self.ranks[pu]:
                self.ranks[pu] += 1
        else:
            self.parent[pu] = pv
 

def Prime(n):
    c = 0
    prime = []
    flag=[0] * (n+1) 
    for i in range(2, n+1):
        if not flag[i]:
            prime.append(i)
            c += 1
        for j in range(c):
            if i * prime[j] > n: 
                break
            flag[i * prime[j]] = prime[j]
            if i % prime[j] == 0: 
                break
    return flag


def dij(s,graph):
    d={}
    d[s]=0
    heap=[(0,s)]
    seen=set()
    while heap:
        dis,u=heappop(heap)
        if u in seen:
            continue
        seen.add(u)
        for v,w in graph[u]:
            if v not in d or d[v]>d[u]+w:
                d[v]=d[u]+w
                heappush(heap,(d[v],v))
    return d
 

def bell(s,g):  # bellman-Ford
    dis=AI(n,inf)
    dis[s]=0
    for i in range(n-1):
        for u,v,w in edge:
            if dis[v]>dis[u]+w:
                dis[v]=dis[u]+w
    change=A(n)
    for i in range(n):
        for u,v,w in edge:
            if dis[v]>dis[u]+w:
                dis[v]=dis[u]+w
                change[v]=1
    return dis
 

def lcm(a,b): 
    return a*b // gcd(a,b)


def lis(nums):
    res=[]
    for k in nums:
        i=bisect.bisect_left(res,k)
        if i==len(res):
            res.append(k)
        else:
            res[i]=k
    return len(res)
 

def RP(nums): # Reverse Pair
    n = len(nums)
    s=set(nums)
    d={}
    for i,k in enumerate(sorted(s),1):
        d[k]=i
    bi=BIT([0]*(len(s)+1))
    ans=0
    for i in range(n-1,-1,-1):
        ans+=bi.query(d[nums[i]]-1)
        bi.update(d[nums[i]],1)
    return ans
 

class DLN:
    def __init__(self,val):
        self.val=val
        self.pre=None
        self.next=None
 

def nb(i,j,n,m):
    for ni,nj in [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]:
        if 0<=ni<n and 0<=nj<m:
            yield ni,nj
 

def topo(n):
    q=deque()
    res=[]
    for i in range(1,n+1):
        if ind[i]==0:
            q.append(i)
            res.append(i)
    while q:
        u=q.popleft()
        for v in g[u]:
            ind[v]-=1
            if ind[v]==0:
                q.append(v)
                res.append(v)
    return res
 
 
@bootstrap
def gdfs(r,p):
    if len(g[r])==1 and p!=-1:
        yield None
    for ch in g[r]:
        if ch!=p:
            yield gdfs(ch,r)
    yield None