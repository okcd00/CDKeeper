"""
一个字符串的权重定义为：其中所有 3-gram 子串为回文串的数量
计算一个字符串所有子序列的权重和，对 1e9 + 7 取模。

输入：
abaa

输出：
4

解释：
所有长度为 1或2 的子序列权重为 0
长度为3的子序列包括：
aba 包含 aba, 计1次
aba 包含 aba, 计1次
aaa 包含 aaa, 计1次

长度为4的子序列包括：
abaa 包含 aba, 计1次

总计4次
"""
