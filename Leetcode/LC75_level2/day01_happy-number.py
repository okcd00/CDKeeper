"""
https://leetcode.cn/problems/happy-number/

编写一个算法来判断一个数 n 是不是快乐数。

「快乐数」 定义为：
对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和。
然后重复这个过程直到这个数变为 1，也可能是 无限循环 但始终变不到 1。
如果这个过程 结果为 1，那么这个数就是快乐数。
如果 n 是 快乐数 就返回 true ；不是，则返回 false 。
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        cycle_members = {4, 16, 37, 58, 89, 145, 42, 20}

        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                total_sum += digit ** 2
            return total_sum

        while n != 1 and n not in cycle_members:
            n = get_next(n)
        return n == 1

    def isHappy_cd(self, n: int) -> bool:
        rec = [n]
        cur = sum([int(c)**2 for c in str(n)])
        while True:
            cur = sum([int(c)**2 for c in str(rec[-1])])
            # print(cur)
            if cur == 1:
                return True
            if cur in rec:
                return False
            rec.append(cur)
