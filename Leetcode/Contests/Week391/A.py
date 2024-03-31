class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        ans = sum([int(d) for d in str(x)])
        if x % ans == 0:
            return ans 
        return -1


if __name__ == '__main__':
    s = Solution()
    ret = s.sumOfTheDigitsOfHarshadNumber(11)
    print(ret)