def get_input(input_type=int):
    elem_list = input().split(' ')
    return map(input_type, elem_list)

def solve():
    n, l, r = map(int, input().split())
    min_v = 2**l - 1 + (n-l) * 1
    max_v = 2**r - 1 + (n-r) * 2**(r-1)
    print('{} {}'.format(min_v, max_v))

if __name__ == '__main__':
    solve()