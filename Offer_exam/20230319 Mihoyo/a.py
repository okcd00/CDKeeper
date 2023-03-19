import sys
MODULE = int(1e9) + 7

n = int(sys.stdin.readline().strip())

MAX_INDEX = 2 ** n
s = sys.stdin.readline().strip()


def mod_mul(a, b):
    return (a % MODULE) * (b % MODULE) % MODULE


def mod_add(a, b):
    return ((a % MODULE) + (b % MODULE)) % MODULE


def mod_exp(root, order):
    if order == 0:
        return 1
    elif order == 1:
        return root % MODULE
    return mod_mul(
        mod_exp(
            (root * root) % MODULE, 
            order // 2),
        root if order % 2 else 1)


def travel(root):  
    # 中序遍历
    # Recursion depth exceeded.
    l, r = root*2, root*2+1
    if l >= MAX_INDEX:
        return 1
    if root == 0 or s[root+1] == s[root]:
        return mod_add(travel(l), travel(r))
    # this level can also be changed
    return mod_add(
        mod_mul(travel(l), 2),
        mod_mul(travel(r), 2))
    # call print(travel(0))


if __name__ == "__main__":    
    # AABABBB / AABBABB / ABAABBB / ABABABB
    #       A(4)
    #    A(2x1)   B(1)
    #  A   B    B   B
    pairs = [2 for i in range(1, len(s), 2) if s[i] != s[i+1]]
    print(mod_exp(2, len(pairs)))
