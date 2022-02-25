def LCS(s1, s2, debug=False, output_index=False):
    # https://blog.csdn.net/weixin_42018258/article/details/80670067
    size1 = len(s1) + 1
    size2 = len(s2) + 1
    # 程序多加一行，一列，方便后面代码编写
    chess = [[["", 0] for j in list(range(size2))] for i in list(range(size1))]
    for i in list(range(1, size1)):
        chess[i][0][0] = s1[i - 1]
    for j in list(range(1, size2)):
        chess[0][j][0] = s2[j - 1]
    if debug:
        from pprint import pprint
        print("初始化数据：")
        pprint(chess)
    for i in list(range(1, size1)):
        for j in list(range(1, size2)):
            if s1[i - 1] == s2[j - 1]:
                chess[i][j] = ['↖', chess[i - 1][j - 1][1] + 1]
            elif chess[i][j - 1][1] > chess[i - 1][j][1]:
                chess[i][j] = ['←', chess[i][j - 1][1]]
            else:
                chess[i][j] = ['↑', chess[i - 1][j][1]]
    if debug:
        print("计算结果：")
        pprint(chess)
    i = size1 - 1
    j = size2 - 1
    lcs_str = []
    s1_index, s2_index = [], []
    while i > 0 and j > 0:
        if chess[i][j][0] == '↖':
            lcs_str.append(chess[i][0][0])
            s1_index.append(i)
            # lcs_str.append(chess[0][j][0])
            s2_index.append(j)
            i -= 1
            j -= 1
        if chess[i][j][0] == '←':
            j -= 1
        if chess[i][j][0] == '↑':
            i -= 1
    lcs_str.reverse()
    lcs_str = ''.join(lcs_str)
    if output_index:
        s1_index.reverse()
        s2_index.reverse()
        return lcs_str, s1_index, s2_index
    return ''.join(lcs_str)


if __name__ == "__main__":
    print(LCS('abcd', 'axybgd', True, True))
