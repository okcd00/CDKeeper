#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>


using namespace std;
const int inf = 1e9;
const int maxn = 100001;


typedef struct Edge {
	int x, y, d;
	Edge(int x = 0, int y = 0, int d = 0) :x(x), y(y), d(d) {}
}Edge;
typedef struct State {
	int x, d;
	State(int x = 0, int d = 0) :x(x), d(d) {}
	friend bool operator < (State a, State b) {
		return a.d > b.d;
	}
}State;
vector<Edge> G[2005];
int d[2005];
bool vis[2005];
int dijkstra(int s, int e) {
	for (int i = 0; i < 2001; i++)
		d[i] = inf;
	memset(vis, 0, sizeof(vis));
	priority_queue<State> Q;
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
int main() {
	int n, m;
	long long T;
	scanf("%d%d%lld", &n, &m, &T);
	for (int i = 0; i < m; i++) {
		int x, y, d;
		scanf("%d%d%d", &x, &y, &d);
		G[x].push_back(Edge(x, y, d));
	}
	int d1 = dijkstra(1, n);
	int d2 = dijkstra(n, 1);
	printf("%lld\n", (d1 + d2) * T);
	return 0;
}
/*
5 5 3
1 2 1
2 3 1 
3 5 1 
5 1 1 
4 5 1
*/