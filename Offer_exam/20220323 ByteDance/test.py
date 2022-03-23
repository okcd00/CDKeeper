"""
Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85
"""

ret = []
while True:
    try:
        line = str(input())
    except EOFError:
        break
    ret.append(tuple(line.split(',')))

print(sorted(ret, key=lambda x: (x[0], int(x[1]), int(x[2]))))