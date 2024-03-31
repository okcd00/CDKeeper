class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        ans = numBottles + 0
        while numBottles >= numExchange:
            numBottles -= numExchange
            ans += 1
            numBottles += 1
            numExchange += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    ret = s.maxBottlesDrunk(10,3)
    print(ret)