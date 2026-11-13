"""Lazy exponential decay over ordered, finite timestamps; Python 3."""
from math import isfinite


class DecayedCounts:
    def __init__(self, half_life):
        if not isfinite(half_life) or half_life <= 0:
            raise ValueError("half_life must be finite and positive")
        self.half_life = half_life
        self.state = {}
        self.last_now = None

    def _check_time(self, now):
        if not isfinite(now) or (self.last_now is not None and now < self.last_now):
            raise ValueError("time must be finite and nondecreasing")
        self.last_now = now

    def _decay(self, category, now):
        value, previous = self.state.get(category, (0.0, now))
        value *= 2.0 ** (-(now - previous) / self.half_life)
        self.state[category] = (value, now)
        return value

    def add(self, now, category, weight=1.0):
        if not isinstance(category, str):
            raise ValueError("category must be a string")
        if not isfinite(weight) or weight < 0:
            raise ValueError("weight must be finite and nonnegative")
        self._check_time(now)
        value = self._decay(category, now)
        self.state[category] = (value + weight, now)

    def query(self, now):
        self._check_time(now)
        return {category: self._decay(category, now) for category in self.state}
