n, k = list(map(int, input().strip().split()))
a = sorted(map(int, input().strip().split()))

# bitand, means NO zeros in a digit
# bit_case = [0 for _ in range(32)]  

# 2 ** 31 = int (2147483648)
bit_record = [[0 for _ in range(32)] for _ in range(n)]  # rec[n][i]: 0/1


def lowbit(_val):
    return _val & -_val

for _val_idx, val in enumerate(a):
    for _i, _b in enumerate(str(bin(val)[-1:1:-1])):
        if _b == '1':
            bit_record[_val_idx][_i] = 1

ret, pivot = 0, 31
while pivot >= 0:
    while pivot >= 0 and sum([rec[pivot] for rec in bit_record]) < k:
        pivot -= 1
    if pivot < 0:
        break
    ret += 1 << pivot
    bit_record = [rec for rec in bit_record if rec[pivot] == 1]
    pivot -= 1
print(ret)   