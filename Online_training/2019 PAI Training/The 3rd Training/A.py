def get_input(input_type=int):
    elem_list = input().split(' ')
    return map(input_type, elem_list)

def solve(a=None):
    if a is None:
        a = input()

    rest_len = a.__len__() - 1
    ret = rest_len // 2
    if '1' in a[1:] or rest_len % 2:
        ret += 1
    print(ret)

if __name__ == '__main__':
    solve()