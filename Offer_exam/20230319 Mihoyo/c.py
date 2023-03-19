import sys
if __name__ == "__main__":
    # 读取第一行的n
    t = int(sys.stdin.readline().strip())
    mhy_string = "mhy" * (int(1e5) // 3 + 1)
    for i in range(t): 
        ans = ""
        # count for strings
        c1, c2, c3 = list(map(int, sys.stdin.readline().strip().split()))
        # print(c1, c2, c3)
        if c3 > 0:
            ans += mhy_string[:c3+2]
            # print(ans)
            if c2 < 1 and c1 > 0:
                print("-1")  # Invalid
                continue
            if c2 >= 1:
                for _ in range(c2-1):
                    ans += ans[-2]
                ans += ans[-1]
            ans += ans[-1] * c1
        else:
            if c2 > 0:
                ans += "hy"
                for _ in range(c2-1):
                    ans += ans[-2]
                ans += ans[-1] * (c1+1)
            else:
                ans += 'y' * (c1+2)
        print(ans)