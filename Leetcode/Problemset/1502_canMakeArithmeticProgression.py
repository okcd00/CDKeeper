class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        arr_len = arr.__len__()
        arr_delta = [arr[i+1] - arr[i] for i in range(arr_len - 1)]
        return arr_delta.count(arr_delta[0]) == arr_len - 1