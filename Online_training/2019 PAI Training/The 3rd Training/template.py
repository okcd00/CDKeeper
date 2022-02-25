import math

def get_input(input_type=int):
    elem_list = input().split(' ')
    return map(input_type, elem_list)

def solve():
    a = get_input(int)
    print(list(a))

if __name__ == '__main__':
    solve()