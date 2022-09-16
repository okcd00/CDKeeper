def gcdext(a: int, b: int):
    # 扩展欧几里得算法 tuple (g, s, t)
    s, t, x, y = 1, 0, 0, 1  # 初始化s, t, x2, y2
    while b:
        q, r = divmod(a, b)
        a, b = b, r  # 求最大公约数
        s, t, x, y = x, y, s - q * x, t - q * y  # 辗转相除
    # 返回元组(g,s,t)，使 g == a*s + b*t
    return a, s, t


def gcd(a: int, b: int):
    # Ouclid gcd
    while a != 0:
        a, b = b % a, a
    return b


def invert(m:int, phi:int):
    # from gmpy2 import invert
    # calculate inv via ext-Ouclid gcd
    _, mi, _ = gcdext(m, phi)
    return mi if mi > 0 else mi + phi


def inverse(u, v):
    # from Crypto.Util.number import inverse
    # The inverse of :data:`u` *mod* :data:`v`.
    u3, v3 = u, v
    u1, v1 = 1, 0
    while v3 > 0:
        q = u3 // v3
        u1, v1 = v1, u1 - v1 * q
        u3, v3 = v3, u3 - v3 * q
    while u1 < 0:
        u1 = u1 + v
    return u1


class Permutation:

    """
    欧拉定理：
    a, m 为互质正整数时，我们有 a ^ {\phi(m)} \equiv 1 (mod m)

    费马小定理：
    a, m 互质且 k 为质数，我们有 a ^ {m-1} \equiv 1 (mod m)

    用途：
    a ^ {k} \equiv a ^ {k % (m-1)} (mod m)
    """

    def __init__(self, vmod: int = 10 ** 9 + 7):
        self._vmod = vmod
        self._size = 0
        self._cache_factorial = [1]  # 缓存阶乘
        self._cache_factorial_inv = [1]  # 缓存阶乘的乘法逆元

    def factorial(self, n: int) -> int:
        """
        费马小定理用于求模逆元：
        a * inv(a) \equiv 1 (mod m)

        a ^ {m-1} \equiv 1 (mod m)
        => a * (a ^ {m-2}) \equiv 1 (mod m)

        所以有 (a ^ {m-2}) 可以是 a 的模逆元
        """
        while self._size <= n:
            self._size += 1
            # record factorial
            self._cache_factorial.append(
                (self._cache_factorial[-1] * self._size) % self._vmod)
            # record inv
            self._cache_factorial_inv.append(
                pow(self._cache_factorial[-1], self._vmod - 2, self._vmod))
        return self._cache_factorial[n]

    def arrange(self, n: int, m: int) -> int:
        """计算排列数：A(n,m) (n>=m)"""
        return (self.factorial(n) * self._cache_factorial_inv[n - m]) % self._vmod

    def comb(self, n: int, m: int) -> int:
        """计算组合数：C(n,m) (n>=m)"""
        return (self.arrange(n, m) * self._cache_factorial_inv[m]) % self._vmod


if __name__ == "__main__":
    permutation = Permutation(vmod=int(1e9)+7)
    print(permutation.factorial(5))
    print(permutation.arrange(4, 2))
    print(permutation.comb(17, 15))
    test_res = permutation.comb(13545, 300)
    print(f"C_13545^300 = {test_res} (mod {permutation._vmod})")

