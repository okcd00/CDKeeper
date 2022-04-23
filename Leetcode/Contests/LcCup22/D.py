from collections import deque

class Solution:

    def face2lines(self, face):
        # U, R, D, L
        # 顺时针读数
        lines = [
            face[0], 
            ''.join([l[-1] for l in face]),
            face[-1][::-1],
            ''.join([l[0] for l in face][::-1]),
        ]
        return lines

    def rotate_l(self, lines):
        u, r, d, l = lines
        return [r, d, l, u]

    def rotate_r(self, lines):
        u, r, d, l = lines
        return [l, u, r, d]

    def roll_over(self, lines, mode='vertical'):
        u, r, d, l = [line[::-1] for line in lines]
        return [u, l, d, r]

    def complementary(self, line):
        return ''.join(['1' if c == '0' else '0' for c in line])

    def get_all_status(self, lines):
        ret = []
        ret.append(lines)
        lines = self.rotate_r(lines)
        ret.append(lines)
        lines = self.rotate_r(lines)
        ret.append(lines)
        lines = self.rotate_r(lines)
        ret.append(lines)
        lines = self.roll_over(lines)
        ret.append(lines)
        lines = self.rotate_r(lines)
        ret.append(lines)
        lines = self.rotate_r(lines)
        ret.append(lines)
        lines = self.rotate_r(lines)
        ret.append(lines)
        return ret

    def get_face_status(self, lines, status=0):
        u, r, d, l = lines
        if status == 0:
            return lines
        lines = self.rotate_r(lines)
        if status == 1:
            return lines
        lines = self.rotate_r(lines)
        if status == 2:
            return lines
        lines = self.rotate_r(lines)
        if status == 3:
            return lines
        if status >= 4:
            lines = self.roll_over(lines)
        if status == 4:
            return lines
        lines = self.rotate_r(lines)
        if status == 5:
            return lines
        lines = self.rotate_r(lines)
        if status == 6:
            return lines
        lines = self.rotate_r(lines)
        if status == 7:
            return lines

    def has_line(self, face_id, line, r=0):
        # r: rotate status (offset)
        ret = []
        for status_id, status in enumerate(self.status[face_id]):
            if line[1:-1] == status[r][1:-1]:
                ret.append(status_id)
        return ret

    def has_line_old(self, face, line):
        _face = [_l[1:-1] for _l in face]
        _line = line[1:-1]
        if _line in _face:
            # 0-4
            return face, _face.index(_line)  
        _line = _line[::-1]
        if _line in _face:
            # r 0-4 -> 5-8
            return self.roll_over(face), self.roll_over(_face).index(_line)  
        return None, -1

    def share_line_status(self, item_a, pos_a, 
                                face_idb, pos_b):
        face_ida, status_ida = item_a
        src_line = self.status[face_ida][status_ida][pos_a]
        src_line = src_line[::-1]
        src_line = self.complementary(src_line)
        _status = self.has_line(
            face_id=face_idb, 
            line=src_line, 
            r=pos_b)  # up/right/down/left
        return _status

    def fit_line(self, line_a, line_b):
        # TODO: bit-wize xor
        for c_a, c_b in zip(line_a[1:-1], line_b[1:-1]):
            if c_a == c_b:
                return False
        return True

    def fit_corner(self, *args):
        if sum(map(int, args)) == 1:
            return True
        return False
    
    def show_pic(self, sequence):
        mat = [['*' for _ in range(9)] for _ in range(12)]
        offset = [(3, 3), (6, 3), (3, 6), (0, 3), (3, 0), (9, 3)]
        for item_idx, item in enumerate(sequence):
            lines = self.status[item[0]][item[1]]
            _mat = [lines[0], [lines[3][1], 1, lines[1][1]], lines[2][::-1]]
            for _r, row in enumerate(_mat):
                for _c, col in enumerate(row):
                    mat[_r + offset[item_idx][0]][_c + offset[item_idx][1]] = _mat[_r][_c]
        for row in mat:
            for col in row:
                print(col, end='')
            print('')

    def dfs(self, sequence):
        # print(sequence)
        UP, RIGHT, DOWN, LEFT = 0, 1, 2, 3
        used_idx = [item[0] for item in sequence]
        current_face = len(sequence)
        if len(used_idx) == 6:
            print(used_idx)
            self.show_pic(sequence)
            return True
        # print(sequence)
        # print(used_idx, faces, current_face)
        for face_id in range(6):
            if face_id in used_idx:
                continue
            if current_face == 1:
                # share_line_01 
                _status = self.share_line_status(
                    sequence[0], DOWN, 
                    face_id, UP)                
                if _status:
                    for _status_id in _status:
                        # print(self.status[face_id][_status_id])
                        if self.dfs(sequence + [(face_id, _status_id)]):
                            return True
            if current_face == 2:
                # share_line_02
                _status1 = self.share_line_status(
                    sequence[0], RIGHT, 
                    face_id, LEFT)                
                # share_line_12
                _status2 = self.share_line_status(
                    sequence[1], RIGHT, 
                    face_id, DOWN)        

                _status = [_s for _s in set(_status1 + _status2) 
                           if _s in _status1 and _s in _status2]        
                for _status_id in _status:
                    # share_corner_012
                    if not self.fit_corner(
                        self.status[sequence[0][0]][sequence[0][1]][RIGHT][-1],
                        self.status[sequence[1][0]][sequence[1][1]][RIGHT][0],
                        self.status[face_id][_status_id][LEFT][0]
                    ):     
                        continue 
                    if self.dfs(sequence + [(face_id, _status_id)]):
                        return True
            if current_face == 3:
                # share_line_03
                _status1 = self.share_line_status(
                    sequence[0], UP, 
                    face_id, DOWN)                
                # share_line_23
                _status2 = self.share_line_status(
                    sequence[2], UP, 
                    face_id, RIGHT)        
                _status = [_s for _s in set(_status1 + _status2) 
                           if _s in _status1 and _s in _status2]        
                for _status_id in _status:
                    # share_corner_023
                    if self.fit_corner(
                        self.status[sequence[0][0]][sequence[0][1]][UP][-1],
                        self.status[sequence[2][0]][sequence[2][1]][UP][0],
                        self.status[face_id][_status_id][DOWN][0]
                    ):      
                        if self.dfs(sequence + [(face_id, _status_id)]):
                            return True
            if current_face == 4:
                # share_line_04
                _status1 = self.share_line_status(
                    sequence[0], LEFT, 
                    face_id, RIGHT)                
                # share_line_14
                _status2 = self.share_line_status(
                    sequence[1], LEFT, 
                    face_id, DOWN)
                # share_line_24
                _status3 = self.share_line_status(
                    sequence[2], RIGHT, 
                    face_id, LEFT)
                # share_line_34
                _status4 = self.share_line_status(
                    sequence[3], LEFT, 
                    face_id, UP)        
                _status = [_s for _s in set(_status1 + _status2 + _status3 + _status4) 
                           if _s in _status1 
                           and _s in _status2
                           and _s in _status3
                           and _s in _status4]        
                for _status_id in _status:
                    # share_corner_014
                    if not self.fit_corner(
                        self.status[sequence[0][0]][sequence[0][1]][LEFT][0],
                        self.status[sequence[1][0]][sequence[1][1]][LEFT][-1],
                        self.status[face_id][_status_id][RIGHT][-1]
                    ):     
                        continue
                    # share_corner_034
                    if not self.fit_corner(
                        self.status[sequence[0][0]][sequence[0][1]][LEFT][-1],
                        self.status[sequence[3][0]][sequence[3][1]][LEFT][0],
                        self.status[face_id][_status_id][RIGHT][0]
                    ):     
                        continue
                    if self.dfs(sequence + [(face_id, _status_id)]):
                        return True
            if current_face == 5:
                # share_line_15
                _status1 = self.share_line_status(
                    sequence[1], DOWN, 
                    face_id, UP)  
                # share_line_25
                _status2 = self.share_line_status(
                    sequence[2], RIGHT, 
                    face_id, RIGHT)                      
                # share_line_35
                _status3 = self.share_line_status(
                    sequence[3], UP, 
                    face_id, DOWN)
                # share_line_45
                _status4 = self.share_line_status(
                    sequence[4], LEFT, 
                    face_id, LEFT)
                # print(self.status[face_id])
                _status = [_s for _s in set(_status1 + _status2 + _status3 + _status4) 
                           if _s in _status1 
                           and _s in _status2
                           and _s in _status3
                           and _s in _status4]       

                for _status_id in _status:
                    # share_corner_125
                    if not self.fit_corner(
                        self.status[sequence[1][0]][sequence[1][1]][DOWN][0],
                        self.status[sequence[2][0]][sequence[2][1]][DOWN][0],
                        self.status[face_id][_status_id][UP][-1]
                    ):     
                        continue
                    # share_corner_235
                    if not self.fit_corner(
                        self.status[sequence[2][0]][sequence[2][1]][UP][-1],
                        self.status[sequence[3][0]][sequence[3][1]][UP][-1],
                        self.status[face_id][_status_id][DOWN][0]
                    ):     
                        continue
                    # share_corner_345
                    if not self.fit_corner(
                        self.status[sequence[3][0]][sequence[3][1]][UP][0],
                        self.status[sequence[4][0]][sequence[4][1]][UP][0],
                        self.status[face_id][_status_id][DOWN][-1]
                    ):     
                        continue
                    # share_corner_415
                    if not self.fit_corner(
                        self.status[sequence[4][0]][sequence[4][1]][DOWN][-1],
                        self.status[sequence[1][0]][sequence[1][1]][DOWN][-1],
                        self.status[face_id][_status_id][UP][0]
                    ):     
                        continue
                    if self.dfs(sequence + [(face_id, _status_id)]):
                        return True
        return False

    def composeCube(self, shapes) -> bool:
        """
        # face-id
            -----
            | 3 |
        -------------
        | 4 | 0 | 2 |
        -------------
            | 1 |
            -----
            | 5 |
            -----
        # status
        0: original
        1: rotate_r1
        2: rotate_r2
        3: rotate_r3
        4: roll_over (vertical default)
        5: roll_over_r1
        6: roll_over_r2
        7: roll_over_r3
        """
        self.faces = [self.face2lines(face) for face in shapes]
        self.status = [self.get_all_status(face) for face in self.faces]
        # if self.bfs(faces):  # starts as 0
        if self.dfs([(0, 0)]):  # starts as (face-0, status-0)
            return True  # escape with a 6-number-long string
        return False


if __name__ == '__main__':
    s = Solution()
    # shapes = [["101","111","000"],["000","010","111"],["010","011","000"],["010","111","010"],["101","111","010"],["000","010","011"]]
    shapes = [["000","110","000"],["110","011","000"],["110","011","110"],["000","010","111"],["011","111","011"],["011","010","000"]]
    print(s.composeCube(shapes=shapes))