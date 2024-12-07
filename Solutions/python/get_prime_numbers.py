def init_prime_euler():
    maxn = int(1e6)  # int(1e7)
    prime_list = [False] * (maxn+1)

    ret = []
    for i in range(2, maxn+1):
        if not prime_list[i]:
            ret.append(i)
        
        for j in ret:
            if i * j > maxn:
                break
            prime_list[i*j] = True
            if i % j == 0:
                break
    return ret


if __name__ == "__main__":
    print(init_prime_euler()[:1500])