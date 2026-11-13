"""One-sided cumulative evidence detector; not an intent classifier."""
from math import isclose, isfinite


class OneSidedCUSUM:
    def __init__(self, reference=0.4, threshold=0.9, *, reset_on_alarm=False, atol=1e-12):
        if not isfinite(reference):
            raise ValueError("reference must be finite")
        if not isfinite(threshold) or threshold <= 0:
            raise ValueError("threshold must be finite and positive")
        if not isfinite(atol) or not 0 <= atol < threshold:
            raise ValueError("atol must be nonnegative and smaller than threshold")
        self.reference = reference
        self.threshold = threshold
        self.reset_on_alarm = reset_on_alarm
        self.atol = atol
        self.score = 0.0

    def update(self, value):
        if not isfinite(value):
            raise ValueError("value must be finite")
        self.score = max(0.0, self.score + value - self.reference)
        score = self.score
        alarm = score >= self.threshold or isclose(
            score, self.threshold, rel_tol=0.0, abs_tol=self.atol
        )
        if alarm and self.reset_on_alarm:
            self.reset()
        return score, alarm

    def reset(self):
        self.score = 0.0
