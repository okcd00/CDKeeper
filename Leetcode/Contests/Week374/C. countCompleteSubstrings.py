from collections import Counter
class Solution(object):
    def count_perfect_substrings_TLE(self, word, k):
        count = 0
        n = len(word)

        for i in range(n):
            freq = [0] * 26
            distinct_char = 0
            for j in range(i, min(n, i + k * 3)):
                char_index = ord(word[j]) - ord('a')
                if freq[char_index] >= k:
                    break  # 超出 k 次出现
                if j > 0:
                    prev_index = ord(word[j-1]) - ord('a')
                    if distinct_char > 0 and abs(char_index - prev_index) > 2:  
                        break  # 相邻间隔过大
                freq[char_index] += 1
                if freq[char_index] == 1:
                    distinct_char += 1  # 记录新入字符个数
                if j - i == distinct_char * k - 1:
                    count += 1
                    # print(i, j, word[i:j+1])
        return count

    def top_answer(self, word, k):
        n = len(word)
        right = [0] * n
        start = 0
        while start < n:
            end = start + 1
            while end < n and abs(ord(word[end]) - ord(word[end-1])) <= 2:
                end += 1
            for i in range(start, end):
                right[i] = end
            start = end
        orda = ord('a')
        count = [[0] * 26]
        for i, c in enumerate(word):
            a = count[-1][::]
            a[ord(c)-orda] += 1
            count.append(a)
        res = 0
        for start in range(n):
            for end in range(start + k, min(n, right[start], start + k * 26) + 1, k):
                valid = True
                for i in range(26):
                    d = count[end][i] - count[start][i]
                    if d != 0 and d != k:
                        valid = False
                        break
                if valid:
                    res += 1
        return res
    
    def count_perfect_substrings(self, word, k):
        word = [ord(w)-ord('a') for w in word]
        n = len(word)

        def substring_khits(s):
            """
            s 中有多少个子串，其每个字母恰好出现k次
            枚举子串有多少个字母 m
            那么长度为 m x k 的窗口内，是否满足每个字母恰好出现 k 次
            """
            res = 0
            for m in range(1, 27):  # 枚举符合条件的子串里有 m 种字符
                size = m * k  # 那么这个子串长度应该是 m*k
                if size > len(s):
                    break
                c1 = Counter(s[:size])  # 字符 x 出现了 y 次
                c2 = Counter(c1.values())  # 出现了 x 次的有 y 种字符
                if c2[k] == m:  # 符合题目条件，O(1)
                    res += 1

                for _in, _out in zip(s[size:], s[:]):  # O(n)
                    c2[c1[_in]] -= 1  
                    c1[_in] += 1  # 字符 _in 多出现一次
                    c2[c1[_in]] += 1

                    c2[c1[_out]] -= 1  
                    c1[_out] -= 1  # 字符 _out 少出现一次
                    c2[c1[_out]] += 1

                    if c2[k] == m:  # 符合题目条件，O(1)
                        res += 1
            return res
        
        # 分组循环，外层找起始位置
        ans = i = 0
        while i < n:
            lef = i
            i += 1
            # 分组循环，内层找切断位置
            while i < n and abs(word[i] - word[i-1]) <= 2:
                i += 1
            ans += substring_khits(word[lef:i])
        return ans
    
    def countCompleteSubstrings(self, word, k):
        """
        :type word: str
        :type k: int
        :rtype: int
        """
        return self.count_perfect_substrings(word, k)
    