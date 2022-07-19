"""
https://leetcode.cn/problems/longest-palindrome-by-concatenating-two-letter-words/

给你一个字符串数组 words 。words 中每个元素都是一个包含 两个 小写英文字母的单词。
请你从 words 中选择一些元素并按 任意顺序 连接它们，并得到一个 尽可能长的回文串 。每个元素 至多 只能使用一次。
请你返回你能得到的最长回文串的 长度 。如果没办法得到任何一个回文串，请你返回 0 。
回文串 指的是从前往后和从后往前读一样的字符串。
"""
from collections import Counter


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        ret = 0
        has_mid = False
        dic = dict(Counter(words).items())
        for k in dic:
            rev = k[::-1]
            if k > rev:
                continue
            elif k == k[::-1]:
                ret += dic[k] // 2 * 2
                if dic[k] % 2 == 1:
                    has_mid = True
            elif k[::-1] in dic:
                ret += min(dic[k], dic[k[::-1]]) * 2
        return 2 * (ret + 1 if has_mid else ret)
