# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7
import random


def rand7():
    return random.randint(0, 7)


class Solution:
    def rand10(self) -> int:
        while True:
            a = rand7()
            b = rand7()
            idx = (a - 1) * 7 + b
            if idx <= 40:
                return 1 + (idx - 1) % 10

            a = idx - 40
            b = rand7()
            # get uniform dist from 1 - 63
            idx = (a - 1) * 7 + b
            if idx <= 60:
                return 1 + (idx - 1) % 10
                
            a = idx - 60
            b = rand7()
            # get uniform dist from 1 - 21
            idx = (a - 1) * 7 + b
            if idx <= 20:
                return 1 + (idx - 1) % 10