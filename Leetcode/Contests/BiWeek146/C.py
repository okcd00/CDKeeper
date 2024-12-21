class Solution:

    def checkValidCuts(self, n: int, rectangles) -> bool:
        def can_cut_in_three(segments):
            segments.sort()
            merged = []
            for start, end in segments:
                if not merged or merged[-1][1] <= start:
                    merged.append([start, end])
                else:                    
                    merged[-1][1] = max(merged[-1][1], end)
            # print(merged)
            return len(merged) >= 3

        x_segments = [(x_left, x_right) for x_left, _, x_right, _ in rectangles]
        y_segments = [(y_bottom, y_top) for _, y_bottom, _, y_top in rectangles]
        return can_cut_in_three(x_segments) or can_cut_in_three(y_segments)
    
    def checkValidCuts_tle(self, n: int, rectangles) -> bool:
        x_segments = [[rectangles[0][0], rectangles[0][2]]]
        y_segments = [[rectangles[0][1], rectangles[0][3]]]
        
        for idx, (x_left, y_bottom, x_right, y_top) in enumerate(rectangles):
            if idx == 0:
                continue

            updated_segments = []
            involved_segments = [[x_left, x_right]]
            for x1, x2 in x_segments:
                if x_right <= x1 or x_left >= x2:
                    updated_segments.append([x1, x2])
                else:
                    involved_segments.append([x1, x2])
            # print(involved_segments)
            updated_segments.append([
                min([x1 for x1, x2 in involved_segments]),
                max([x2 for x1, x2 in involved_segments]),
            ])
            x_segments = updated_segments

            updated_segments = []
            involved_segments = [[y_bottom, y_top]]
            for y1, y2 in y_segments:
                if y_top <= y1 or y_bottom >= y2:
                    updated_segments.append([y1, y2])
                else:
                    involved_segments.append([y1, y2])
            # print(involved_segments)
            updated_segments.append([
                min([y1 for y1, y2 in involved_segments]),
                max([y2 for y1, y2 in involved_segments]),
            ])
            y_segments = updated_segments

        # print(x_segments, y_segments)
        if x_segments.__len__() >= 3:
            return True
        if y_segments.__len__() >= 3:
            return True
        return False   
    

if __name__ == "__main__":
    from pprint import pprint
    n = 4
    rectangles = [[1,0,5,2],[0,2,2,4],[3,2,5,3],[0,4,4,5]]
    # rectangles = [[0,0,1,1],[2,0,3,4],[0,2,2,3],[3,0,4,3]]
    ret = Solution().checkValidCuts(n,rectangles)
    pprint(ret)