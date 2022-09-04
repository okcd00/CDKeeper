import math


def init_prime_euler():
    maxn = int(1e6)  # int(1e7)
    prime_flag = [False] * (maxn + 1)
    target_list = []
    for i in range(2, maxn+1):
        if not prime_flag[i]:
            target_list.append(i)
        
        for j in target_list:
            if i * j > maxn:
                break
            prime_flag[i*j] = True
            if i % j == 0:
                break
    is_p = [False] * (maxn + 1)
    for val_p in target_list:
        is_p[val_p] = True
    return is_p


def main():
    is_p = init_prime_euler()
    # print(len(is_p), is_p[:20])
    n = int(input().strip())
    for _ in range(n):
        a = int(input().strip())
        if a == 0:
            print("NO")
        else:
            root = int(math.sqrt(a))
            # print(root, is_p[root-2:root+3], is_p[root])
            if is_p[root] and root ** 2 == a:
                print("YES")
            else:
                print("NO")


if __name__ == '__main__':
    main();