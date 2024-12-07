import math
from functools import cache


class Solution:
    def findMinimumTime(self, strength, K: int) -> int:
        n = len(strength)
        strength = sorted(strength)
        min_time = None
        
        @cache
        def time_cost(cost, x, yi, vis):
            x += K
            vis += 1 << yi
            nonlocal min_time
            if min_time is not None and min_time < cost:
                return 
            if vis + 1 == 1 << n:
                # print(cost, x, yi, vis)
                if min_time is None:
                    min_time = cost
                elif min_time > cost:
                    min_time = cost
            [time_cost(cost + math.ceil(y / x), x, yi, vis) 
             for yi, y in enumerate(strength) if (1<<yi) & vis == 0]
        
        [time_cost(y, 1, yi, 0) for yi, y in enumerate(strength)]
        return min_time
          
    def findMinimumTime_failed(self, strength, K: int) -> int:
        x = 1
        ret = 0
        energy = 0
        strength = sorted(strength)
        # visited = [0 for _ in strength]
        while strength:
            y = strength[0]
            cost = math.ceil((y - energy) / x)
            print(y, energy, x, '=', cost)
            ret += cost
            energy += x * cost
            for _y in strength[1:]:
                if _y <= energy:
                    y = _y
                else:
                    break
            print("remove", y, 'with', energy)
            strength.remove(y)
            x += K
            energy = 0
        return ret

if __name__ == '__main__':
    s = Solution()
    ret = s.findMinimumTime([7,3,6,18,22,50],4)
    print(ret)