#include <bits/stdc++.h>
using namespace std;

const int N = 1010;
const double eps = 1e-8, INF = 1e9;

double f[N][N];

class Solution {
public:
    int minSkips(vector<int>& dist, int speed, int m) {
        int n = dist.size();
        for (int i = 1; i < n; i ++ ) {
            double t = (double)dist[i - 1] / speed;
            for (int j = 0; j <= i; j ++ ) {
                f[i][j] = INF;
                if (j <= i - 1) f[i][j] = ceil(f[i - 1][j] + t - eps);
                if (j) f[i][j] = min(f[i][j], f[i - 1][j - 1] + t);
            }
        }
        double t = (double)dist[n - 1] / speed;
        for (int i = 0; i < n; i ++ )
            if (f[n - 1][i] + t < m + eps) return i;
        return -1;
    }
};