from collections import Counter
class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        ct1 = Counter(words1)
        ct2 = dict(Counter(words2).items())
        ret = 0
        for k, v in [(k, v) for k, v in ct1.items() if v == 1]:
            if ct2.get(k, 0) == 1:
                ret += 1
        return ret