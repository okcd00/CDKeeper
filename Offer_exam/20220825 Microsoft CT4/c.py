# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python (Python 3.6)
    ret = 0
    speed = [A[i] - A[i-1] for i in range(1, len(A))]  # length = N - 1
    delta_speed = [v - speed[_i] for _i, v in enumerate(speed[1:])]  # length = N - 2
    
    streak = 0
    for _i, a in enumerate(delta_speed):
        if a != 0:
            if streak > 0:
                ret += (1 + streak) * streak // 2
            streak = 0  # clear
        else:
            streak += 1
    else:
        if streak:
            ret += (1 + streak) * streak // 2

    # print(A, speed, delta_speed, ret)
    # print(ret)
    return ret