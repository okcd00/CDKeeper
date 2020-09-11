class Node:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d


def dijkstra(s, e) {
	d = [999999 for _ in range(2001)]
	memset(vis, 0, sizeof(vis));
	Q = []
	d[s] = 0;
	Q.push(State(s, 0));
	while (!Q.empty()) {
		State a = Q.top();
		Q.pop();
		if (vis[a.x]) continue;
		vis[a.x] = 1;
		for (int i = 0; i < G[a.x].size(); i++) {
			Edge edge = G[a.x][i];
			if (d[edge.y] > d[a.x] + edge.d) {
				d[edge.y] = d[a.x] + edge.d;
				Q.push(State(edge.y, d[edge.y]));
			}
		}
	}
	return d[e];
}

n, m, t = input().split(' ')
n, m, t = int(n), int(m), int(t)

G = []
for i in range(m):
    x, y, d = input.split(' ')
    x, y, d = int(x), int(y), int(d)
    G.append(Node(x, y, d))
	d1 = dijkstra(1, n);
	d2 = dijkstra(n, 1);
	print((d1 + d2) * T);
}