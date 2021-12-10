def read_int_list(): 
    return list(map(int, input().split()))
def read_int_tuple(): 
    return tuple(map(int, input().split()))
def read_int(): 
    return int(input())


numerals = {
    '零': 0, 
    '一': 1, '二': 2, '两': 2, '三': 3, '四': 4,
    '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, 
    '十': 10, '百': 100, '千': 1000, 
    '万': 10000, '亿': 100000000, 
    # '兆': 1000000000000
}

level_delta = {
    '万': 1, 
    '亿': 2, 
    # '兆': 3
}


def ChnString2Int(t):
    ret = 0
    parts = t.split('亿')
    for i, part in enumerate(parts[::-1]):
        val = ChnString2Int_reverse(part)
        ret += val * (int(1e8) ** (i))
    return ret


def ChnString2Int_reverse(t, debug=False):
    total = 0
    r, r_level = 1, 0  # 单位
    t = t.replace(" ", "")
    if debug:
        print(t)
    for _idx in range(len(t)-1, -1, -1):
        val = numerals.get(t[_idx])
        # 是单位：十百千万亿
        if val >= 10:
            # the first (final) char
            if val > r:
                r = val
                if _idx == 0:
                    total += val
            else:
                r = val * (10000 ** r_level)
            if t[_idx] in level_delta:
                r_level += level_delta[t[_idx]]
        else:
            total += r * val
            if debug:
                print(total, '<-', r, val)
    return total


if __name__ == "__main__":
    # Problem 
    # t = input()
    # t = "三十亿亿"
    # t = "一亿八千五百三十万"
    # t = "两千六百三十四万 五千"
    t = "一亿八千五百三十万亿 两千六百三十四万 五千"
    print(ChnString2Int(t))
