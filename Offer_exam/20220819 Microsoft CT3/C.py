# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# the maximum depth of the Py stack is 150,000  XD
from queue import PriorityQueue
from collections import defaultdict, deque

def solution(A, B):
    N = len(A)  # n_houses
    adj_dic = defaultdict(list)

    drive_to = defaultdict(int)  # src should drive to dest
    topo_rank = {}  # the topo rank for the house
    topo_rank[0] = 0
    
    q = deque()  
    for a, b in zip(A, B):
        if a > b:
            a, b = b, a
        # adj_mat[a][b] = 1
        # adj_mat[b][a] = 1
        adj_dic[a].append(b)
        adj_dic[b].append(a)
        if a == 0:
            topo_rank[b] = 1
            drive_to[b] = 0
            q.append((1, b))  # topo_rank, house_id

    # get topo_rank for each house
    while q:
        # print(q)
        _tr, cur_node = q.popleft()
        higher_topo_level_case = []
        for _adj_node in adj_dic[cur_node]:
            if _adj_node == 0:
                continue
            if _adj_node in topo_rank and topo_rank[_adj_node] < _tr:
                continue  # visited
            if _adj_node not in topo_rank:
                topo_rank[_adj_node] = _tr + 1
                drive_to[_adj_node] = cur_node
            higher_topo_level_case.append((_tr+1, _adj_node))
        q.extend(higher_topo_level_case)

    # print(topo_rank)
    # print(drive_to)

    # travel simulation
    cost = 0
    pq = PriorityQueue()
    # pq.put( (0, 0, 0) )
    for _house_id, _tr in topo_rank.items():
        # topo_rank, house_id, person_count
        if _house_id == 0:
            continue
        # the house with the higher topo rank firstly starts
        pq.put( (-_tr, _house_id) )  
    
    person_count = [0] + [1] * N
    while not pq.empty():
        _tr, src = pq.get()
        # print('[', _tr, src, ']')

        dest = drive_to[src]
        person_count[dest] += person_count[src]

        # calculate cost
        cost += person_count[src] // 5 
        if person_count[src] % 5:
            cost += 1
        # print('[', src, '->', dest, person_count[src], cost, ']')

    # print(cost)
    return cost

