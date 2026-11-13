"""Fixed-size sliding maximum, Python 3."""
from collections import deque


def sliding_max(values, k):
    if k <= 0:
        raise ValueError("k must be positive")
    candidates = deque()
    result = []
    for i, value in enumerate(values):
        while candidates and candidates[0] <= i - k:
            candidates.popleft()
        while candidates and values[candidates[-1]] <= value:
            candidates.pop()
        candidates.append(i)
        if i >= k - 1:
            result.append(values[candidates[0]])
    return result
