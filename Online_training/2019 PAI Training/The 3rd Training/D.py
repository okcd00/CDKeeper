def get_input(input_type=int):
    elem_list = input().split(' ')
    return map(input_type, elem_list)

def solve(s=None):
    if s is None:
        s = input()

    cnt = 0
    s = list(s[::-1])
    for idx, d in enumerate(s):
        if d == '0' or cnt:
            if d == '1':
                cnt -= 1
            if d == '0':
                cnt += 1
        else:  # d == 1 and cnt == 0
            s[idx] = '0'
        # print(s[idx], switch, cnt)
    print(''.join(s[::-1]))

if __name__ == '__main__':
    solve()
    # print('0111001100111011101000')
    # solve('0111001100111011101000')
    # print('0011001100001011101000')