class Solution:
    def findPeaks(self, mountain):
        return [i for i in range(1, len(mountain)-1) 
                if mountain[i] > max(mountain[i-1], mountain[i+1])]