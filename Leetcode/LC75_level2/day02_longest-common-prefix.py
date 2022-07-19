"""
https://leetcode.cn/problems/longest-common-prefix/

编写一个函数来查找字符串数组中的最长公共前缀。
如果不存在公共前缀，返回空字符串 ""。
"""


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min(map(len, strs))
        for idx in range(min_length):
            if len(set(list(map(lambda x: x[idx], strs)))) != 1:
                return strs[0][:idx]
        return strs[0][:min_length]

    def longestCommonPrefix_v1(self, strs: List[str]) -> str:
        ret = ""
        for c_case in zip(*strs):
            if len(set(c_case)) == 1:
                ret += c_case[0]
            else:
                break
        return ret
