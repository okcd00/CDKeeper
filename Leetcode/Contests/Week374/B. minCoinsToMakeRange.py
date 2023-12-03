class Solution(object):
    def min_coins_to_make_range(self, coins, target):
        coins.sort()
        current = 0
        added_coins = 0
        for coin in coins:
            while coin > current + 1:
                added_coins += 1
                current += current + 1
                if current >= target:
                    return added_coins
            current += coin
            # 如果 current 已经大于或等于目标值，提前结束
            if current >= target:
                return added_coins
        while current < target:
            added_coins += 1
            current += current + 1
        return added_coins
    
    def min_coins_to_make_range_v2(self, coins, target):
        coins.sort()
        ans = 0
        rng = 1  # range(0, rng)

        i = 0
        while rng <= target:
            if i < len(coins) and coins[i] <= rng:
                rng += coins[i]
                i += 1
            else:  # coins[i] > rng
                rng *= 2  # 加一个大小为 rng 的硬币
                ans += 1
        return ans


    def minimumAddedCoins(self, coins, target):
        """
        :type coins: List[int]
        :type target: int
        :rtype: int
        """
        return self.min_coins_to_make_range_v2(coins, target)
    

if __name__ == '__main__':
    s = Solution()
    ret = s.minimumAddedCoins([1,2,3,7], 19)
    print(ret)