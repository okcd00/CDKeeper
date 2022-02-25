import os  
import sys  
  
# solve  
def solve():  
    n, m = map(int, raw_input().split())
    print(min(m, n - m) if m != 0 else 1)
  
# main  
if __name__ == "__main__":  
    solve()  