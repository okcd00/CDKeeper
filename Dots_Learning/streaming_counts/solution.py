"""Exact counts over (now - width, now]; ordered integer timestamps."""
from collections import Counter, deque


class WindowCounts:
    def __init__(self, width):
        if not isinstance(width, int) or width <= 0:
            raise ValueError("width must be a positive integer")
        self.width = width
        self.events = deque()
        self.counts = Counter()
        self.last_now = None

    def evict(self, now):
        if not isinstance(now, int):
            raise ValueError("timestamps must be integers")
        if self.last_now is not None and now < self.last_now:
            raise ValueError("time cannot go backwards")
        self.last_now = now
        while self.events and self.events[0][0] <= now - self.width:
            _, category = self.events.popleft()
            self.counts[category] -= 1
            if not self.counts[category]:
                del self.counts[category]

    def add(self, now, category):
        if not isinstance(category, str):
            raise ValueError("category must be a string")
        self.evict(now)
        self.events.append((now, category))
        self.counts[category] += 1

    def query(self, now):
        self.evict(now)
        return dict(self.counts)

    def top_k(self, now, k):
        if not isinstance(k, int) or k < 0:
            raise ValueError("k must be a nonnegative integer")
        # Deliberately simple baseline; ties use category name.
        return sorted(self.query(now).items(), key=lambda item: (-item[1], item[0]))[:k]
