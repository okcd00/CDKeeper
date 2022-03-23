from pprint import pprint


def lcs(s1, s2, debug=False, output_index=False):
    """the Longest Common Subsequence"""

    # init with one more row and one more column
    chess = [
        [[" ", 0] for j in list(range(len(s2) + 1))] 
         for i in list(range(len(s1) + 1))]
    for i in list(range(1, len(s1) + 1)):
        chess[i][0][0] = s1[i - 1]
    for j in list(range(1, len(s2) + 1)):
        chess[0][j][0] = s2[j - 1]
    if debug:
        print("初始化数据：")
        pprint(chess)

    # dp
    for i in list(range(1, len(s1) + 1)):
        for j in list(range(1, len(s2) + 1)):
            if s1[i - 1] == s2[j - 1]:  # the same char
                chess[i][j] = ['↖', chess[i - 1][j - 1][1] + 1]
            elif chess[i][j - 1][1] >= chess[i - 1][j][1]:  # left
                chess[i][j] = ['←', chess[i][j - 1][1]]
            else:  # chess[i][j - 1][1] < chess[i - 1][j][1]  # up
                chess[i][j] = ['↑', chess[i - 1][j][1]]
    if debug:
        print("计算结果：")
        pprint(chess)
    
    # generate traceback
    lcs_str = []
    i, j = len(s1), len(s2)
    s1_index, s2_index = [], []
    while i > 0 and j > 0:
        _dir, _val = chess[i][j]
        if _dir == '↖':
            assert s1[i-1] == s2[j-1]
            lcs_str.append(s1[i-1])
            # lcs_str.append(chess[i][0][0])
            # lcs_str.append(chess[0][j][0])
            s1_index.append(i)
            s2_index.append(j)
            i -= 1
            j -= 1
        if _dir == '←':
            j -= 1
        if _dir == '↑':
            i -= 1
    lcs_str = ''.join(lcs_str[::-1])
    if output_index:
        s1_index.reverse()
        s2_index.reverse()
        return lcs_str, s1_index, s2_index
    return ''.join(lcs_str)


if __name__ == "__main__":
    print(lcs('abcd', 'axybgd', True, True))
