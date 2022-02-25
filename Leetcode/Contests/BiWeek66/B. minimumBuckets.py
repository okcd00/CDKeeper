class Solution:
    def minimumBuckets(self, street: str) -> int:
        ret = 0
        st_len = street.__len__()
        need = [[0, 0] for _ in range(st_len)]
        for idx, h in enumerate(street):
            if h == 'H':
                _lef, _rig = 0, 0
                if idx > 0:
                    need[idx-1][1] += 1
                    if street[idx-1] == '.':
                        _lef = 1
                if idx < st_len - 1:
                    need[idx+1][0] += 1
                    if street[idx+1] == '.':
                        _rig = 1
                if _lef + _rig == 0:
                    return -1  
        # print(need)
        for idx, (l, r) in enumerate(need):
            if l == r == 1:
                need[idx][0] = 0
                if idx >= 2:
                    need[idx-2][1] = 0
                need[idx][1] = 0
                if idx <= st_len-3:
                    need[idx+2][0] = 0
                ret += 1
        # print(need)
        for idx, (l, r) in enumerate(need):
            if l+r == 1:
                need[idx][0] = 0
                if idx >= 2:
                    need[idx-2][1] = 0
                need[idx][1] = 0
                if idx <= st_len-3:
                    need[idx+2][0] = 0
                ret += 1
        # print(need)
        return ret