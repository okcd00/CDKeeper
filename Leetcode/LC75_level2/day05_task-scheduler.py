"""
https://leetcode.cn/problems/task-scheduler/

给你一个用字符数组 tasks 表示的 CPU 需要执行的任务列表。其中每个字母表示一种不同种类的任务。任务可以以任意顺序执行，并且每个任务都可以在 1 个单位时间内执行完。在任何一个单位时间，CPU 可以完成一个任务，或者处于待命状态。
然而，两个 相同种类 的任务之间必须有长度为整数 n 的冷却时间，因此至少有连续 n 个单位时间内 CPU 在执行不同的任务，或者在待命状态。
你需要计算完成所有任务所需要的 最短时间 。
"""
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0:
            return len(tasks)
        
        # 统计执行次数
        task_counts = dict(Counter(tasks).items())
        
        # 最多的执行次数
        maxExec = max(task_counts.values())
        
        # 具有最多执行次数的任务数量
        maxCount = sum(1 for v in task_counts.values() if v == maxExec)

        schedule_time = (maxExec - 1) * (n + 1) + maxCount
        return max(schedule_time, len(tasks))