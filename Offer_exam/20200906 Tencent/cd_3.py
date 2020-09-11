import math

L, d = input().split(' ')

if L==d:
  print(0)
else:
  print("%.4f" % (math.log(float(L)/float(d)) + 1))
