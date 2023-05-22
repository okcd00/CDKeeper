# 题目：给定一个长度为n的钢条，及每个长度对应的价格列表p = [p_1, p_2, .... p_n]，
# 求最大售卖价格 及 最大售卖价格对应的切割方法。

def cut_rod(p, n):
    def cut_rod_dp_t2b(p, n, r):
        if r[n - 1] >= 0:
            return r[n - 1]
        if n == 0:
            q = 0
        else:
            q = -1
            for i in range(1, n + 1):
                q = max(q, p[i - 1] + cut_rod_dp_t2b(p, n - i, r))
        r[n - 1] = q
        return q

    r = [-1] * n
    return cut_rod_dp_t2b(p, n, r)

def cut_rod_b2t(p, n):
    r = [-1] * n
    for i in range(n):
        q = p[i]
        for j in range(i):
            q = max(q, p[j] + p[i - j - 1])
            r[i] = q
    return r[n - 1]


def cut_rod(p, n):
    r = [-1] * n
    s = list(range(n))
    for i in range(n):
        q = p[i]
        for j in range(i):
            if q < p[j] + p[i - j - 1]:
                q =p[j] + p[i - j - 1]
                s[i] = j
            r[i] = q
    return r[n - 1], s[n - 1]


def my_trial(p, n):
    record = [0]

    def max_value(n):
        cut_result = 0
        if n > 1:
            cut_result = max([record[i] + record[n-i] for i in range(1, n//2+1)])
        record.append(max(p[n-1], cut_result))
    return record[-1]


if __name__ == "__main__":
    p = [0.1, 0.2, 0.99, 0.4]
    print(my_trial(p, len(p)))
    print(cut_rod(p, len(p)))