class CoinsCombination:
    def __init__(self):
        pass

    def solve(self, amount, coins):
        # dfs 
        if amount < 0:
            raise ValueError()
        ret = 0 
        # coins = sorted(coins, reverse=True)
        for _x in range(amount // coins[0], -1, -1):
            rest_coins = amount - (_x * coins[0])
            if rest_coins == 0:
                ret += 1
            elif len(coins) > 1:
                ret += self.solve(rest_coins, coins[1:])
        return ret

    def solve_dp(self, amount, coins):
        # 组合数 (零钱种类)
        # when amount=0, there is 1 selection
        # 1 = 0 + 1
        # 2 = 1+1, 0+2
        dp_case = [0] * (amount + 1)  
        dp_case[0] = 1
        # coins = sorted(coins, reverse=True)
        for _c in coins:
            for _am in range(1, amount+1):
                if _am - _c >= 0:
                    # print(f"{_am}: + {dp_case[_am - _c]} ({_am - _c})")
                    dp_case[_am] += dp_case[_am - _c]
        print(dp_case)
        return dp_case[-1]

    def solve_deprecated(self, amount, coins):
        # 排列数 (走楼梯方案)
        # when amount=0, there is 1 selection
        # 1 = 0 + 1
        # 2 = 1+1, 0+2
        dp_case = [0] * (amount + 1)  
        dp_case[0] = [1]  
        coins = sorted(coins, reverse=True)
        for _am in range(1, amount+1):
            for _c in coins:
                if _am - _c >= 0:
                    dp_case[_am] += dp_case[_am - _c]
        print(dp_case)
        return dp_case[-1]


if __name__ == "__main__":
    amount = 10000
    coins = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    sol = CoinsCombination()
    ret = sol.solve_dp(amount, coins)
    print(ret)