from pprint import pprint


def edit_distance(str1, str2):    
    # define dp[i][j] for str1[i], str2[j]
    dp = [[0 for _i in range(len(str2)+1)] for _j in range(len(str1)+1)]
    for i in range(len(str1)+1):
        dp[i][0] = i
    for j in range(len(str2)+1):
        dp[0][j] = j
    for i in range(1, len(str1)+1):
        _i = i - 1
        for j in range(1, len(str2)+1):
            _j = j - 1
            dp[i][j] = min(
                dp[i-1][j] + 1,
                dp[i][j-1] + 1,
                dp[i-1][j-1] + (0 if str1[_i] == str2[_j] else 1)
            )
    pprint(dp)
    return dp[-1][-1]


if __name__ == "__main__":
    a = "abcde"
    b = "bcdea"
    print(edit_distance(a, b))