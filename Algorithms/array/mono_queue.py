"""
单调队列是一种数据结构，它可以用于解决滑动窗口问题，
即在一个长度为n的数组中，求解每个长度为k的连续子数组的最大值或最小值等问题。
单调队列的主要思想是在队列中维护滑动窗口中的元素，保证队列中的元素单调递增或单调递减，
从而可以快速求解滑动窗口中的最大值或最小值。

## 定义
单调队列是一个双端队列，它具有以下两个性质：
单调队列的实现需要维护一个双端队列，队列中的元素单调递增或单调递减。
在维护队列时，需要保证队列中的元素满足单调性，并且头部元素是当前滑动窗口的最大值或最小值。

## 应用
单调队列可以应用于滑动窗口问题，如在一个长度为n的数组中，
求解每个长度为k的连续子数组的最大值或最小值等问题。
此外，单调队列还可以用于解决其他问题，如最小值覆盖问题、最大值减去最小值的问题等。
"""


from collections import deque

def monotonic_queue(nums, k):
    # 求解滑动窗口中的最大值的问题，即给定一个数组nums和一个滑动窗口大小k，
    # 求解数组nums中所有长度为k的连续子数组的最大值。
    n = len(nums)
    res = []
    queue = deque()  # 初始化单调队列
    for i in range(n):
        print(queue)
        # 当队列中的元素个数超过滑动窗口大小 k 时，
        # 即 queue[0] 下标对应的元素不在滑动窗口 [i-k+1, i] 中，
        # 需要从队列头部出队
        if queue and queue[0] < i - k + 1:
            queue.popleft()
        # 将队列中小于当前元素的元素出队，保证队列中的元素单调递增
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)  # 当前元素入队
        # 当队列中的元素个数等于滑动窗口大小k时，将头部元素加入答案数组
        if i >= k - 1:
            res.append(nums[queue[0]])
    return res


def find_min_cover(nums, k):
    n = len(nums)
    q = deque()  # 存储数组下标
    res = []  # 存储每个子数组的最小值
    for i in range(n):
        # 将不符合窗口大小的下标弹出
        while q and q[0] <= i - k:
            q.popleft()
        # 将当前下标入队，并保证单调队列单调递增
        while q and nums[q[-1]] > nums[i]:
            q.pop()
        q.append(i)
        # 当滑动窗口的大小达到k时，将队首的下标对应的元素作为当前子数组的最小值
        if i >= k - 1:
            res.append(nums[q[0]])
    return max(res)


if __name__ == '__main__':
    # 单调队列
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(monotonic_queue(nums, k))

    # 最小值覆盖问题
    nums = [4, 5, 2, 7, 1, 6, 3]
    k = 3
    print(find_min_cover(nums, k))  # 输出 2
