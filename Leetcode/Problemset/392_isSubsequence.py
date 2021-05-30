class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pivot = 0
        s_length = s.__len__()
        for idx, c in enumerate(t):
            if pivot == s_length:
                return True
            if s[pivot] == c:
                pivot += 1
        else:
            if pivot == s_length:
                return True
            return False