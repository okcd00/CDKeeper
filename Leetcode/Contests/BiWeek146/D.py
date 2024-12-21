from collections import defaultdict


class Solution:
    
    # ABCCC | ABCCE | ACCCC | ACCCE | ACCDE | BBCCC | BCCCC | CCCCC
    def subsequencesWithMiddleMode(self, nums) -> int:
        MOD = 10 ** 9 + 7
        n = len(nums)
        uniq = sorted(set(nums))
        mapping = {v: i for i, v in enumerate(uniq)}
        nums = [mapping[v] for v in nums]
        m = len(uniq)
        acc = [[0] * m]
        curr = [0] * m
        for i in range(n):
            curr[nums[i]] += 1
            acc.append(list(curr))
        
        ans = 0
        for i in range(2, n - 2):
            num = nums[i]
            left = acc[i][num]
            right = acc[n][num] - acc[i + 1][num]
            if left >= 2 and right >= 2:
                ans += comb(left, 2) * comb(right, 2)
            if left >= 2 and right >= 1:
                ans += comb(left, 2) * right * (n - i - 1 - right)
            if left >= 2:
                ans += comb(left, 2) * comb(n - i - 1 - right, 2)
            if right >= 2:
                ans += comb(right, 2) * comb(i - left, 2)
            if left >= 1 and right >= 2:
                ans += left * (i - left) * comb(right, 2)
            if left >= 1 and right >= 1:
                ans += left * (i - left) * right * (n - i - 1 - right)
                
            if left >= 1:
                base = left * (i - left) * comb(n - i - 1 - right, 2)
                for other in range(m):
                    if other == num:
                        continue
                    to_del = 0
                    other_left = acc[i][other]
                    other_right = acc[n][other] - acc[i + 1][other]
                    if other_left >= 1 and other_right >= 1:
                        to_del += left * other_left * other_right * (n - i - 1 - right - other_right)
                    if other_right >= 2:
                        to_del += left * (i - left - other_left) * comb(other_right, 2)
                    if other_left >= 1 and other_right >= 2:
                        to_del += left * other_left * comb(other_right, 2)
                    base -= to_del
                ans += base
                
            if right >= 1:
                base = right * (n - i - 1 - right) * comb(i - left, 2)
                for other in range(m):
                    if other == num:
                        continue
                    to_del = 0
                    other_left = acc[i][other]
                    other_right = acc[n][other] - acc[i + 1][other]
                    if other_left >= 1 and other_right >= 1:
                        to_del += right * other_left * other_right * (i - left - other_left)
                    if other_left >= 2:
                        to_del += right * (n - i - 1 - right - other_right) * comb(other_left, 2)
                    if other_left >= 2 and other_right >= 1:
                        to_del += right * other_right * comb(other_left, 2)
                    base -= to_del
                ans += base
                
            ans %= MOD
        return ans   