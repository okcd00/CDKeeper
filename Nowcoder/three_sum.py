#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# 
# @param num int整型一维数组 
# @return int整型二维数组
#
class Solution:
    def threeSum(self, num):
        # write code here
        ret = []
        num = sorted(num)
        for idx1, v1 in enumerate(num[:-2]):
            if idx1 > 0 and num[idx1] == num[idx1-1]:
                continue
            rest = -v1
            idx2, idx3 = idx1 + 1, len(num) - 1
            v2, v3 = num[idx2], num[idx3]
            while idx2 < idx3:
                if v2 + v3 == rest:
                    if len(ret) == 0 or (v1, v2, v3) != ret[-1]:
                        ret.append((v1, v2, v3))
                    while idx2 + 1 < idx3 and num[idx2+1] == num[idx2]:
                        idx2 += 1
                    idx2 += 1
                    while idx2 < idx3 - 1 and num[idx3] == num[idx3-1]:
                        idx3 -= 1
                    idx3 -= 1
                    v2, v3 = num[idx2], num[idx3]
                elif v2 + v3 < rest:
                    idx2 += 1
                    v2 = num[idx2]
                elif v2 + v3 > rest:
                    idx3 -= 1
                    v3 = num[idx3]
        return ret