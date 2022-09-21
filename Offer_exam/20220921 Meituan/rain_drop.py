#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# max water
# @param arr int整型一维数组 the array
# @return long长整型
#
class Solution:

    def maxWater_2pointers(self, arr):
        ans = 0
        l, r = 0, len(arr)-1
        lef_max, rig_max = 0, 0
        
        while l < r:
            lef_max = max(lef_max, arr[l])
            rig_max = max(rig_max, arr[r])
            if arr[l] < arr[r]:
                ans += lef_max - arr[l]
                l += 1
            else:
                ans += rig_max - arr[r]
                r -= 1
        return ans

    def maxWater(self, arr: List[int]) -> int:
        n = len(arr)
        lef_max = [0 for _ in range(n)]
        rig_max = [0 for _ in range(n)]
        
        cur_max = arr[0]
        for i, v in enumerate(arr):
            if i == 0:
                continue
            lef_max[i] = cur_max
            if v > cur_max:
                cur_max = v
        
        cur_max = arr[-1]
        for i, v in enumerate(arr[::-1]):
            if i == 0:
                continue
            rig_max[n-1-i] = cur_max
            if v > cur_max:
                cur_max = v
        
        ans = 0
        for i, v in enumerate(arr):
            ans += max(0, min(lef_max[i], rig_max[i]) - v)

        print(ans)
        return ans
        