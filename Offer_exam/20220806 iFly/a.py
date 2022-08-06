import sys
# from pprint import pprint


def longest_common_sequence(a, b):
    dp = [[0 for _ in range(len(b)+1)] for _ in range(len(a)+1)]
    for i in range(1, len(a)+1):
        for j in range(1, len(b)+1):
            if a[i-1] == b[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
    # pprint(dp)
    return dp[len(a)][len(b)]


if __name__ == "__main__":
    # 读取第一行的n
    a = sys.stdin.readline().strip()    
    b = sys.stdin.readline().strip()
    lcs = longest_common_sequence(a, b)
    print(lcs * 2)
