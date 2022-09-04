"""
小度是个粉刷匠，粉刷括号本领强。

墙上有从左到右 n 个瓷砖，小度有 k 种颜料可以在每个位置刷上一个任意一种颜色的左括号或者右括号，
问最后有多少种不同的粉刷方案，使得每一种颜色的括号构成的子序列都是合法的括号序列。

两种方案不同，当且仅当存在某个位置，两种方案中一个是左括号而另一个是右括号或者颜色不同，
输出方案数对 998244353 取模的值。

定义合法的括号序列：

1 空序列合法；
2 如果 S 合法，则 (S) 合法，这里的左右括号可以是任意一种相同的颜色；
3 如果 S 和 T 都合法，则 ST（把两者首尾相接）合法。

举例说明，如果 n=10，小度有 3 种颜料对应的左右括号分别用 ()、[]、{} 表示，
则 [[](({)])} 这种粉刷方案符合条件，因为 ()()、[[]]、{} 都是合法的括号序列，而方案 []))(())[] 不满足条件。

格式
输入格式：
一行两个正整数 n,k (1 ≤ n ≤ 5×10^5,1 ≤ k ≤ 1000)，表示瓷砖个数和颜料种数。

输出格式：
一行一个整数，表示方案数取模后的值。
"""