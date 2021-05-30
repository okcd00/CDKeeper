class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        
        def topsort(G):
            in_degrees = dict((u, 0) for u in G)
            topo_level = dict((u, 0) for u in G)
            for u in G:
                for v in G[u]:
                    in_degrees[v] += 1  # each node's indegree
            S, Q = [], [u for u in G if in_degrees[u] == 0]  # node with indegree 0, get level=0
            while Q:
                u = Q.pop()  # Default remove the end
                S.append(u)
                for v in G[u]:
                    in_degrees[v] -= 1  # Remove this link
                    topo_level[v] = max(topo_level[v], topo_level[u]+1)
                    if in_degrees[v] == 0:
                        Q.append(v)
            return S, list(map(lambda x: topo_level[x], S))

        G = {}  # G means graph
        nodes, links = [], []  # prepare nodes and links for toposort
        row = matrix.__len__()
        if not row: return 0
        column = matrix[0].__len__()
        for j in range(column)[::-1]:
            for i in range(row)[::-1]:
                node_value = matrix[i][j]
                cur_node = "{},{}".format(i,j)
                down_node = "{},{}".format(i+1,j) if i+1<row else None
                right_node = "{},{}".format(i,j+1) if j+1<column else None
                # print(cur_node, down_node, right_node)
                
                # add nodes
                G[cur_node] = []
                nodes.append(cur_node)
                
                # then add links
                if down_node:
                    down_value = matrix[i+1][j]
                    if node_value > down_value:
                        links.append((down_node, cur_node))
                        G[down_node].append(cur_node)
                    if down_value > node_value:
                        links.append((cur_node, down_node))
                        G[cur_node].append(down_node)
                if right_node:
                    right_value = matrix[i][j+1]
                    if node_value > right_value:
                        links.append((right_node, cur_node))
                        G[right_node].append(cur_node)
                    if right_value > node_value:
                        links.append((cur_node, right_node))
                        G[cur_node].append(right_node)

        result, topo_level = topsort(G)
        return max(topo_level)+1