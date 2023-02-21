# https://leetcode.cn/problems/WhsWhI/

a = [100, 4, 200, 1, 3, 2]

class Solution:
    @staticmethod
    def longestConsecutive(nums) -> int:
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak

if __name__ == "__main__":
    print(Solution.longestConsecutive(a))
