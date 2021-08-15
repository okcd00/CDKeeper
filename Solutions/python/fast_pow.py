def fast_pow(base, exponent):
    # in C++ STL
    if exponent == 0:
        return 1
    elif exponent < 0:
        base = 1. / base
        exponent = -exponent
    while exponent & 1 == 0:
        exponent >>= 1
        base = base * base
    result = base
    exponent >>= 1
    while exponent != 0:
        base = base * base
        if exponent & 1 != 0:
            result *= base
        exponent >>= 1
    return result


if __name__ == "__main__":
    print(fast_pow(3, -2))
