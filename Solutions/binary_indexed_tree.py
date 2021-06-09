class BIT(object):
    def __init__(self, n):
        # 初始化, n为BIT数组长度
        self.nums = [0] * (1 + n)

    def update(self, i, delta):
        # 更新第i个元素, 给第i个元素加上delta
        while i < len(self.nums):
            self.nums[i] += delta
            i += i & -i

    def query_sum(self, i):
        # 查询前i项的和
        ans = 0
        while i > 0:
            ans += self.nums[i]
            i -= i & -i
        return ans

    def query(self, i):
        if i == 0:
            return self.query_sum(0)
        return self.query_sum(i) - self.query_sum(i-1)

    def show_all(self):
        return [self.query(i) for i in range(self.nums.__len__())]


if __name__ == "__main__":
    b = BIT(10)
    b.update(3, 10)
    print(b.show_all())
    b.update(5, 3)
    print(b.show_all())

