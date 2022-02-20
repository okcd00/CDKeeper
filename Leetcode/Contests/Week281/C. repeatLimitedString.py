from collections import Counter

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        ret = ""
        times = sorted(Counter(s).items(), key=lambda x: x[0])[::-1]
        times = [[c, count] for c, count in times]
        
        last_substring = ""
        while times:
            # print(times)
            
            # main string
            if last_substring and last_substring[-1] == times[0][0]:
                used = min(times[0][1], repeatLimit - len(last_substring))
            else:
                used = min(times[0][1], repeatLimit)
            last_substring = times[0][0] * used
            
            ret += last_substring
            times[0][1] -= used
            
            # delimeter
            if len(times) < 2:
                break
            last_substring = times[1][0]
            ret += last_substring
            times[1][1] -= 1
            
            # switch main string charater
            if times[1][1] == 0:
                del times[1]
            if times[0][1] == 0:
                del times[0]
            
        return ret
        