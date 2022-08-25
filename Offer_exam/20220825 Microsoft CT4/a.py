def list_to_val(digit_list, rm_idx):
    return int([d for i, d in enumerate(digit_list) if i != rm_idx])


def solution(A):
    digits = str(A)
    return max([list_to_val(digits, i) for i, d in enumerate(digits) if d == '5'])
