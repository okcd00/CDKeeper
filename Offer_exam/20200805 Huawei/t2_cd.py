t, a = input().strip().split()
a_pre, a_post = a.split('*')


def get_indexing(text, sub_str, offset=0):
    if sub_str not in text:
        return []
    index = text.index(sub_str)
    return [index + offset] + get_indexing(text[index+1:], sub_str, index + offset + 1)


all_pre = get_indexing(t, a_pre)
all_post = get_indexing(t, a_post)
# print(all_pre, all_post)

ans = 0
lef_pivot, rig_pivot = 0, 0
used = set()
while(lef_pivot < len(all_pre) and rig_pivot < len(all_post)):
    lef_pos = all_pre[lef_pivot]
    rig_pos = all_post[rig_pivot]
    lef_rng = range(lef_pos, lef_pos + a_pre.__len__())
    rig_rng = range(rig_pos, rig_pos + a_post.__len__())
    if set(lef_rng) <= used:
        lef_pivot += 1
        continue
    if set(rig_rng) <= used:
        rig_pivot += 1
        continue
    # print(lef_pivot, rig_pivot)
    # print(all_pre[lef_pivot], all_post[rig_pivot])
    if lef_pos < rig_pos:
        if set(lef_rng).intersection(set(rig_rng)):
            rig_pivot += 1
            continue
        lef_pivot += 1
        rig_pivot += 1
        ans += 1
        used = used.union(set(lef_rng))
        used = used.union(set(rig_rng))
    elif lef_pos >= rig_pos:
        rig_pivot += 1

# AAAAAA AA*AA
print(ans)