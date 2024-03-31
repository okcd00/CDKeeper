class Solution:
    def cal_dist(self, x1, y1, x2, y2):
        return abs(x1-x2) + abs(y1-y2)

    def minimumDistance(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        vs1 = [(points[i][0]+points[i][1], i) for i in range(n) ]
        vs1.sort()
        vs2 = [(points[i][0]-points[i][1], i) for i in range(n) ]
        vs2.sort()
        r = 0x7fffffffff
        for i in range(n):
            if i==vs1[0][1]:
                v1 = vs1[n-1][0]-vs1[1][0]
            elif i==vs1[n-1][1]:
                v1 = vs1[n-2][0]-vs1[0][0]
            else:
                v1 = vs1[n-1][0]-vs1[0][0]
                
            if i==vs2[0][1]:
                v2 = vs2[n-1][0]-vs2[1][0]
            elif i==vs2[n-1][1]:
                v2 = vs2[n-2][0]-vs2[0][0]
            else:
                v2 = vs2[n-1][0]-vs2[0][0]
            r= min(r, max(v1, v2))
        return r

    def minimumDistance_mysolution(self, points) -> int:
        # _pv = {}
        # _points = []
        # for x, y in points:
        #     _pv[(x,y)] += 1
        #     if _pv[(x,y)] <= 2:
        #         _points.append(points)
        # points = _points
        # from collections import Counter
        # for k, v in Counter(map(tuple, points)).items():
        #     _points += [k for _ in range(min(v, 2))] 
        # points = _points
        n = len(points)
        max_dist = [-1 for _ in range(n)]
        max_neighbor = [-1 for _ in range(n)]
        second_dist = [-1 for _ in range(n)]
        second_neighbor = [-1 for _ in range(n)]
        for idx, p1 in enumerate(points):
            x1, y1 = p1 
            for _idx, p2 in enumerate(points[idx+1:]):
                idx2 = _idx + idx + 1
                x2, y2 = p2
                dist = self.cal_dist(x1,y1,x2,y2)

                # (idx, idx2)
                if max_dist[idx] < dist:
                    second_dist[idx] = max_dist[idx]
                    second_neighbor[idx] = max_neighbor[idx]
                    max_dist[idx] = dist
                    max_neighbor[idx] = idx2
                elif second_dist[idx] < dist:
                    second_dist[idx] = dist
                    second_neighbor[idx] = idx2
                
                # (idx2, idx)
                if max_dist[idx2] < dist:
                    second_dist[idx2] = max_dist[idx2]
                    second_neighbor[idx2] = max_neighbor[idx2]
                    max_dist[idx2] = dist
                    max_neighbor[idx2] = idx
                elif second_dist[idx2] < dist:
                    second_dist[idx2] = dist
                    second_neighbor[idx2] = idx

        # print(max(max_dist))
        # print(max_dist, max_neighbor)
        # print(second_dist, second_neighbor)
        pq = sorted(
            [(max_dist[idx], idx, max_neighbor[idx]) for idx in range(n)] +\
            [(second_dist[idx], idx, second_neighbor[idx]) for idx in range(n)],
            key = lambda x: -x[0]
        )
        max_distance, idx1, idx2 = pq[0]
        ans1, ans2 = 0, 0
        for idx, (d, l, r) in enumerate(pq):
            if idx == 0: continue
            if ans1 >= d and ans2 >= d:
                break
            if idx1 not in (l, r):
                ans1 = max(ans1, d)
            if idx2 not in (l, r):
                ans2 = max(ans2, d)
        return min(ans1, ans2)


if __name__ == '__main__':
    s = Solution()
    points = [[1,1],[7,3],[5,9],[6,4],[7,6],[6,4],[5,2],[4,2],[7,2],[1,1]]
    ret = s.minimumDistance(points)
    print(ret)