s = list(input().strip())  # 100000

modify_n = 0
rev_pos = {}
size = len(s)

for i, c in enumerate(s):
    # 如果修改位置是c，c 和对侧位置不同
    rig_i = size - i - 1  # 0 and size-1
    if i > rig_i:
        break
    if s[i] != s[rig_i]:
        modify_n += 1
        rev_pos[i] = (s[i], s[rig_i])
        edit = min(s[i], s[rig_i])
        s[i] = edit
        s[rig_i] = edit

# if modify_n > 2:
    # print(-1)

for i, c in enumerate(s):
    rig_i = size - i - 1  # 0 and size-1
    if i > rig_i:
        break
    if modify_n == 2:
        break
    if c == 'a':
        continue
    if rev_pos.get(i):
        # l = c = r but != 'a'
        l, r = rev_pos[i]
        s[i] = 'a'
        s[rig_i] = 'a'
        modify_n += 1
    else:
        if i == rig_i:  # mid
            s[i] = 'a'
            modify_n += 1
        elif modify_n == 0:  # s[size-i-1] != 'a'
            s[i] = 'a'
            s[rig_i] = 'a'
            modify_n += 2

print(''.join(s))
# print(rev_pos, edit)

"""
acca
aaaa
"""