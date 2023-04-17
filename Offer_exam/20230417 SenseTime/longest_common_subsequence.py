from pprint import pprint


def longest_common_subsequence(_str1, _str2):
    m, n = len(_str1), len(_str2)
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if _str1[i-1] == _str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] + 1 
                # pre{}
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        # pprint(dp)
    return dp[m][n]


if __name__ == "__main__":
    a = 'abcde'
    b = 'ace'
    print(longest_common_subsequence(a, b))
