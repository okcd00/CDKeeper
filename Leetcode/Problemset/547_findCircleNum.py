class Solution:
    # Kari Solution
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """

        def dfs(V, M, marked, id, count):
            if marked[V] != 0:
                return
            marked[V] = 1
            id[V] = count
            for j in range(len(M)):
                if M[V][j] == 1:
                    dfs(j, M, marked, id, count)


        N = len(M)
        if N == 0:
            return 0

        marked = dict((i, 0) for i in range(N))
        id = dict((i, 0) for i in range(N))
        count = 0
        for i in range(N):
            if marked[i] != 0:
                continue

            count += 1
            marked[i] = 1
            id[i] = count
            for j in range(N):
                if M[i][j] == 1:
                    dfs(j, M, marked, id, count)

        return count