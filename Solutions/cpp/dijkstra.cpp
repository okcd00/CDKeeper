#include <bits/stdc++.h>
using namespace std;

const int MAXV = 2333;  //set max_count of nodes here
const int INF = INT_MAX;  //int32's INF
struct edge
{
    int to, cost;  // dst, cost
};
typedef pair<int, int> P;  // distance, index

int V;  //set vertex number
vector<edge> G[MAXV];  // G[src], first=dst, second=cost
int d[MAXV];  // the min-length for each node from source node

void dijkstra(int s)
{
    priority_queue<P, vector<P>, greater<P>> que;
    // index from 1 (if index from 0,there should be fill(d, d+V, INF) )
    fill(d + 1, d + V + 1, INF); 
    d[s] = 0;
    que.push(P(0, s));
    while (!que.empty())
    {
        P p = que.top();
        que.pop();
        int v = p.second;
        if (d[v] < p.first)
            continue;
        for (int i = 0; i < G[v].size(); i++)
        {
            edge e = G[v][i];
            if (d[e.to] > d[v] + e.cost)
            {
                d[e.to] = d[v] + e.cost;
                que.push(P(d[e.to], e.to));
            }
        }
    }
}


int main()
{
    dijkstra(0);   
    cout << 1 << endl;
    return 0;
}