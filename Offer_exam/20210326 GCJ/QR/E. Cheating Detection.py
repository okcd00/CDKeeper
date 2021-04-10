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
import sys
import math

def sigmoid(_x):
    return 1. / (1 + math.exp(-_x))

def inv_sigmoid(_y):
    if 1 - _y == 0:
        return 3.
    if _y == 0:
        return -3.
    return min(3., max(-3., math.log(_y / (1-_y))))

def e_score(skl):
    # 反函数为 math.log(math.exp(x) - 1) -/+ 3
    def logit(_x):
        return math.log(1 + math.exp(_x))
    area = logit(3. + skl) - logit(-3. + skl)
    return area / 6.

PC = PERSON_COUNT = 100
QC = QUESTION_COUNT = 10000

def skl2score(_skl):
    return sigmoid(_skl)

def score2skl(_scr):
    return inv_sigmoid(_scr)

def score2dfc(_scr):
    return -inv_sigmoid(_scr)

"""
skl2score = [e_score(0.01 * _skl) for _skl in range(-300, 300, 1)]
def score2skl(score):
    return (lower_bound(skl2score, score) - 300) * 0.01
def score2dfc(score):
    # there's a little bias because of the cheater
    return (lower_bound(skl2score, score) - 300) * 0.01
"""

# sys.stdin = open('./Offer_exam/20210326 GCJ/QR/in.txt', 'r')
t = read_int()
p = read_int() 
for case_idx in range(t):    
    score = []  # 2-d matrix
    skill = [0] * PC  # avg hit rate on this problemset
    difficulty = [0] * QC  # avg pass count on this question
    for per_idx in range(PC):
        # person_score = [int(c) for c in input()]
        person_score = input()
        skill[per_idx] = score2skl(person_score.count('1') / QC)
        score.append(person_score)
    
    difficulty = [score2dfc(sum([score[_p][_q]=='1'
                            for _p in range(PC)]) / PC)
                  for _q in range(QC)]
    # difficulty = [score2dfc(d / PC) for d in difficulty]
    
    def calculate_loss(_skl, _dfc, score):
        _exp_score = sigmoid(_skl - _dfc)
        return abs(_exp_score - score)

    def calculate_prob(_skl, _dfc, score):
        _exp_score = sigmoid(_skl - _dfc)
        if score == '1':
            return _exp_score
        else:
            return 1. - _exp_score

    def ln(float_number):
        # if float_number == 0.:
        #     return 1.
        return math.log(float_number)

    cheater = 0
    max_loss = None
    for per_idx in range(PC):
        loss = 0.
        for q_idx in range(QC):
            prob = calculate_prob(
                skill[per_idx], difficulty[q_idx], score[per_idx][q_idx])
            if prob < 1. - .86:
                loss += ln(prob)
        # print(per_idx + 1, loss)
        if max_loss is None or loss < max_loss:
            cheater = per_idx + 1
            max_loss = loss
    print("Case #{}:".format(case_idx + 1), end=' ')
    print(cheater)
    