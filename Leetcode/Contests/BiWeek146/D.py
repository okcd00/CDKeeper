from math import comb
from typing import List
from collections import defaultdict, Counter


class Solution:
    # ABCCC | ABCCE | ACCCC | ACCCE | ACCDE | BBCCC | BCCCC | CCCCC
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        n = len(nums)
        suf = Counter(nums)
        pre = defaultdict(int)
        ans = comb(n, 5)  # 所有方案数
        # 枚举 x，作为子序列正中间的数
        for left, x in enumerate(nums[:-2]):
            suf[x] -= 1
            if left > 1:
                right = n - 1 - left
                pre_x, suf_x = pre[x], suf[x]
                # 不合法：只有一个 x
                ans -= comb(left - pre_x, 2) * comb(right - suf_x, 2)
                # 不合法：只有两个 x，且至少有两个 y（y != x）
                for y, suf_y in suf.items():
                    if y == x:
                        continue
                    pre_y = pre[y]
                    # 左边有两个 y，右边有一个 x，即 yy x xz（z 可以等于 y）
                    ans -= comb(pre_y, 2) * suf_x * (right - suf_x)
                    # 右边有两个 y，左边有一个 x，即 zx x yy（z 可以等于 y）
                    ans -= comb(suf_y, 2) * pre_x * (left - pre_x)
                    # 左右各有一个 y，另一个 x 在左边，即 xy x yz（z != y）
                    ans -= pre_y * suf_y * pre_x * (right - suf_x - suf_y)
                    # 左右各有一个 y，另一个 x 在右边，即 zy x xy（z != y）
                    ans -= pre_y * suf_y * suf_x * (left - pre_x - pre_y)
            pre[x] += 1
        return ans % 1_000_000_007


if __name__ == "__main__":
    ans = Solution().subsequencesWithMiddleMode([1,2,2,3,3,4])
    print(ans)
