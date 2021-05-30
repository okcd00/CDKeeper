import queue as Q 

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans = []
        que = Q.PriorityQueue()
        waiting = Q.PriorityQueue()
        for s_idx, weight in enumerate(servers):
            que.put((weight, s_idx))
        
        cur_time = 0
        waiting_head = None
        for t_idx, task_time in enumerate(tasks):
            if waiting_head is None and not waiting.empty():
                waiting_head = waiting.get()
            if que.empty():
                cur_time = waiting_head[0]
            while waiting_head and (cur_time >= waiting_head[0]):
                que.put((waiting_head[1], waiting_head[2]))
                waiting_head = None if waiting.empty() else waiting.get()
            weight, server_index = que.get()
            ans.append(server_index)
            waiting.put((cur_time + task_time, weight, server_index))
            if waiting_head:
                waiting.put(waiting_head)
            waiting_head = waiting.get()
            # print('{}: [{}] ({}->{})'.format(cur_time, server_index, cur_time, cur_time+task_time))
            # if waiting_head: print(*waiting_head)
            if cur_time <= t_idx:
                cur_time += 1
        return ans
        