import random
import sys
import unittest
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from sliding_window.solution import sliding_max
from streaming_counts.solution import WindowCounts


class WindowTests(unittest.TestCase):
    def test_example(self):
        self.assertEqual(sliding_max([3, 1, 4, 2, 5], 3), [4, 4, 5])

    def test_max_edges(self):
        self.assertEqual(sliding_max([], 1), [])
        self.assertEqual(sliding_max([2], 2), [])
        self.assertEqual(sliding_max([2, 2, 2], 2), [2, 2])
        self.assertEqual(sliding_max([-1, -3, -2], 1), [-1, -3, -2])
        with self.assertRaises(ValueError):
            sliding_max([1], 0)

    def test_max_against_brute_force(self):
        rng = random.Random(0)
        for n in range(25):
            values = [rng.randrange(-5, 6) for _ in range(n)]
            for k in range(1, n + 3):
                expected = [max(values[i:i+k]) for i in range(n-k+1)]
                self.assertEqual(sliding_max(values, k), expected)

    def test_query_without_new_event(self):
        w = WindowCounts(10)
        w.add(0, "shoe")
        w.add(4, "bag")
        w.add(8, "shoe")
        self.assertEqual(w.query(10), {"shoe": 1, "bag": 1})
        self.assertEqual(w.query(14), {"shoe": 1})
        self.assertEqual(w.query(18), {})
        self.assertEqual(w.query(18), {})

    def test_equal_time_top_k_and_snapshot(self):
        w = WindowCounts(10)
        w.add(1, "b")
        w.add(1, "a")
        snapshot = w.query(1)
        snapshot["a"] = 99
        self.assertEqual(w.top_k(1, 2), [("a", 1), ("b", 1)])
        self.assertEqual(w.top_k(1, 0), [])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            WindowCounts(0)
        w = WindowCounts(10)
        w.query(5)
        with self.assertRaises(ValueError):
            w.add(4, "a")
        with self.assertRaises(ValueError):
            w.query(4)
        with self.assertRaises(ValueError):
            w.top_k(5, -1)

    def test_stream_against_brute_force(self):
        rng = random.Random(1)
        w = WindowCounts(10)
        events = []
        now = 0
        for _ in range(200):
            now += rng.randrange(4)
            if rng.randrange(2):
                category = rng.choice(["shoe", "bag", "book"])
                events.append((now, category))
                w.add(now, category)
            expected = Counter(c for t, c in events if now - 10 < t <= now)
            self.assertEqual(w.query(now), dict(expected))


if __name__ == "__main__":
    unittest.main()
