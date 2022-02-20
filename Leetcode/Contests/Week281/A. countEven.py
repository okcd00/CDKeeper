class Solution:
    def countEven(self, num: int) -> int:
        rest = sum([int(c) for c in str(num - num % 10)])
        # 0 2 4 6 8  if rest % 2 == 0
        # 1 3 5 7 9  if rest % 2 == 1        
        return (num - (rest % 2)) // 2 