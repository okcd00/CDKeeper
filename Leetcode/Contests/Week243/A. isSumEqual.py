class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        dic = {chr(ord('a')+i):'{}'.format(i) for i in range(10)}
        # print(dic)
        first_val = int(''.join([dic[n] for n in firstWord]))
        second_val = int(''.join([dic[n] for n in secondWord]))
        target_val = int(''.join([dic[n] for n in targetWord]))
        # print(first_val, second_val, target_val)
        return first_val + second_val == target_val