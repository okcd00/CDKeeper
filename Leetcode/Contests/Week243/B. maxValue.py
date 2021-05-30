class Solution:
    def maxValue(self, n: str, x: int) -> str:
        sign_flag = 1
        if n.startswith('-'):
            sign_flag = -1
            n = n[1:]
        x = str(x)
        for i, c in enumerate(n):
            if sign_flag > 0 and x > c:
                n = n[:i] + x + n[i:]
                break
            if sign_flag < 0 and x < c:
                n = n[:i] + x + n[i:]
                break
        else:
            n = n + x
        if sign_flag == -1:
            n = '-' + n
        return n