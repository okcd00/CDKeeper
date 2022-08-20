"""
费马小定理(Fermat's little theorem)是数论中的一个重要定理，在1636年提出。
如果p是一个质数，而整数a不是p的倍数，则有a^（p-1）≡1（mod p）。
"""

def MOD(_val, vmod=int(1e9) + 7):
    # return (_val + MOD) % MOD
    return _val % vmod


def fast_pow(_val, _pow):
    while _pow > 1:
        if _pow % 2 == 1:
            _val = MOD(MOD(_val * _val) * _val)
        else:
            _val = MOD(_val * _val)
        _pow >>= 1
    return _val


a, b, n = list(map(int, input().strip().split()))
a, b = MOD(a), MOD(b)

#1: a^1 * b^0
#2: a^0 * b^1
#3: a^2 * b^2
#4: a^4 * b^6 (verified)
#5: a^12 * b^16
#6: a^32 * b^44
#7: a^88 * b^120
#8: a^240 * b^328

def fibo_exp(n): 
    # 感觉应该还是需要一个费马小定理之类的，一时记不起来了
    # k^(v-1) % v = 1?
    
    # a1, b1 = 1, 0
    a2, b2 = 0, 1
    for _ in range(3, n+1):
        # a3, b3 = (a1 + a2) * 2, (b1 + b2) * 2
        # a1, a2 = a2, a3
        # b1, b2 = b2, b3
        a3 = (b2 + b2) % int(1e9+6)
        b3 = (a3 + a2) % int(1e9+6)
        a2, b2 = a3, b3
    return a2, b2

if n == 1:
    print(a)
elif n == 2:
    print(b)
else:
    exp_a, exp_b = fibo_exp(n)
    print(MOD( fast_pow(a, exp_a) * fast_pow(b, exp_b) ))