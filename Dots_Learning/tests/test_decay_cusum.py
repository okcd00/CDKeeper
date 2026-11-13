import math
import random
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from exponential_decay.solution import DecayedCounts
from cusum.solution import OneSidedCUSUM


class DecayTests(unittest.TestCase):
    def test_shoes_and_bag(self):
        model = DecayedCounts(5)
        model.add(0, "shoe")
        model.add(4, "bag")
        model.add(8, "shoe")
        values = model.query(10)
        self.assertAlmostEqual(values["shoe"], 0.25 + 2 ** (-2 / 5))
        self.assertAlmostEqual(values["bag"], 2 ** (-6 / 5))
        self.assertEqual(model.query(10), values)

    def test_half_life_and_same_time(self):
        model = DecayedCounts(5)
        model.add(0, "a", 2)
        model.add(0, "a")
        self.assertAlmostEqual(model.query(5)["a"], 1.5)
        self.assertAlmostEqual(model.query(10)["a"], 0.75)

    def test_matches_full_history(self):
        rng = random.Random(0)
        model = DecayedCounts(5)
        events = []
        now = 0
        for _ in range(100):
            now += rng.randrange(4)
            category = rng.choice(["a", "b"])
            model.add(now, category)
            events.append((now, category))
            actual = model.query(now)
            for key in actual:
                expected = sum(2 ** (-(now-t)/5) for t,c in events if c == key)
                self.assertAlmostEqual(actual[key], expected)

    def test_empty_and_invalid(self):
        self.assertEqual(DecayedCounts(5).query(0), {})
        for value in [0, -1, math.inf, math.nan]:
            with self.assertRaises(ValueError):
                DecayedCounts(value)
        model = DecayedCounts(5)
        model.query(5)
        with self.assertRaises(ValueError):
            model.add(4, "a")
        with self.assertRaises(ValueError):
            model.add(5, "a", -1)
        with self.assertRaises(ValueError):
            model.query(math.nan)


class CUSUMTests(unittest.TestCase):
    def test_lesson(self):
        detector = OneSidedCUSUM()
        results = [detector.update(x) for x in [0.8, 0.1, 0.8, 0.8]]
        for (score, alarm), expected in zip(results, [0.4, 0.1, 0.5, 0.9]):
            self.assertAlmostEqual(score, expected)
        self.assertEqual([alarm for _, alarm in results], [False, False, False, True])

    def test_floor_and_reset(self):
        detector = OneSidedCUSUM(reset_on_alarm=True)
        self.assertEqual(detector.update(0.1), (0.0, False))
        score, alarm = detector.update(1.3)
        self.assertTrue(alarm)
        self.assertEqual(detector.score, 0.0)
        self.assertEqual(detector.update(0.4), (0.0, False))
        detector.update(0.8)
        detector.reset()
        self.assertEqual(detector.score, 0)

    def test_tolerance_and_repeated_alarm(self):
        detector = OneSidedCUSUM(reference=0, threshold=1, atol=1e-12)
        self.assertFalse(detector.update(1-1e-8)[1])
        self.assertTrue(detector.update(1e-8)[1])
        self.assertTrue(detector.update(0)[1])

    def test_invalid(self):
        for kwargs in [{"threshold": 0}, {"reference": math.nan}, {"atol": -1},
                       {"atol": 1}]:
            with self.assertRaises(ValueError):
                OneSidedCUSUM(**kwargs)
        with self.assertRaises(ValueError):
            OneSidedCUSUM().update(math.inf)


if __name__ == "__main__":
    unittest.main()
