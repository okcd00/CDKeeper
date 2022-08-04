"""
1-n 连续整数
对应概率 p

取随机数
"""


import random
from bisect import bisect_left


class RandomSelection:
    def __init__(self, case_size, prob_list):
        self.num_list = list(range(1, case_size+1))
        self.cum_sum = [0.]
        for p in prob_list:
            self.cum_sum.append(self.cum_sum[-1] + p)
        # print(self.cum_sum)
        self.prob_list = prob_list

    def random_once(self):
        # if bisect_left is available
        random_val = random.random()
        pivot = bisect_left(self.cum_sum, random_val)
        # print(random_val, pivot)
        return pivot

    def random_multi(self):
        # with nothing
        rest = 1.0
        for i, p in enumerate(self.prob_list):
            if random.random() < p / rest:
                return self.num_list[i]
            rest -= p
        return self.num_list[-1]

    def __call__(self):
        # return self.random_once()
        return self.random_multi()


if __name__ == "__main__":
    rs = RandomSelection(5, [0.2, 0.1, 0.3, 0.3, 0.1])
    for _ in range(10):
        print(rs())
