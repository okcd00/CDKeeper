class Solution:
    def addMinimum(self, word: str) -> int:
        ret = 0
        i = 0
        pivot = 0
        pattern = 'abc'
        while i < len(word):
            while word[i] != pattern[pivot]:
                ret += 1
                pivot = (pivot + 1) % 3
            i += 1
            pivot = (pivot + 1) % 3
        ret += 2 - pattern.index(word[-1])
        return ret
                
s = Solution()
print(s.addMinimum('aaaaca'))