# s='abcde', itertools.pairwise(s) 的输出应该为 [('a', 'b'), ('b', 'c'), ('c', 'd'), ('d', 'e')]
from itertools import pairwise

# 组合数模板
MOD = 1_000_000_007
MX = 100_000
fac = [0] * MX
fac[0] = 1
for i in range(1, MX):
    fac[i] = fac[i - 1] * i % MOD

inv_fac = [0] * MX
inv_fac[MX - 1] = pow(fac[MX - 1], -1, MOD)
for i in range(MX - 1, 0, -1):
    inv_fac[i - 1] = inv_fac[i] * i % MOD

def comb(n: int, k: int) -> int:
    return fac[n] * inv_fac[k] % MOD * inv_fac[n - k] % MOD

class Solution:
    def numberOfSequence(self, n: int, sick: List[int]) -> int:
        """
        组合数学：
        1. sick[0, n-1]: s^{m-1}, m = sick[i] - sick[i-1] - 1
        2. 不同段之间互相不影响，例如有三段 m1 m2 m3
           则答案为 C(s, m1) * C(s-m1, m2) * C(s-m1-m2, m3) * 2^{m1+m2+m3-3}
        """
        a = sick
        m = len(a)
        total = n - m
        ans = comb(total, a[0]) * comb(total - a[0], n - a[-1] - 1) % MOD
        total -= a[0] + n - a[-1] - 1
        e = 0
        for p, q in zip(a, a[1:]):
            k = q - p - 1
            if k:
                e += k - 1
                ans = ans * comb(total, k) % MOD
                total -= k
        return ans * pow(2, e, MOD) % MOD
