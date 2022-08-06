import sys
from pprint import pprint

# 读取第一行的 n
n = int(sys.stdin.readline().strip())
func = [1, 1]  # max(costs)!


def count_solutions(costs, total, taken):
    if total < 0:
        return 0

    if total == 0:
        # print(taken, len(taken), n-len(taken), func[len(taken)] * func[n-len(taken)], '=', func[len(taken)], 'x', func[n-len(taken)])
        return func[len(taken)] * func[n-len(taken)]

    ret = 0
    if costs:
        ret += count_solutions(costs[1:], total-costs[0], taken + [costs[0]])
        ret += count_solutions(costs[1:], total, taken)
    return ret


def count_solutions_deprecated(costs, total=60):
    costs.sort(reverse=True)
    # print(costs)

    dp = [0 for _ in range(total+1)]
    dp[0] = 1
    for tick in range(1, total+1):
        for item in costs:
            if tick >= item:
                # print(item, tick)
                dp[tick] += dp[tick-item]
    # pprint(dp)
    return dp[-1]       


if __name__ == "__main__":
    costs = list(map(int, sys.stdin.readline().strip().split()))
    costs.sort(reverse=True)
    if min(costs) <= 0 or len(costs) != n:
        print("0")
    else:
        for i in range(2, max(costs)):
            func.append(func[-1] * i)
        print(count_solutions(costs, 60, []))
