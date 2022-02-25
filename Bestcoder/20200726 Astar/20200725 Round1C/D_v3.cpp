#include <bits/stdc++.h>
using namespace std;

int main () {
    int T; scanf("%d", &T);
    while (T--) {
        int n; scanf("%d", &n);
        int mx[2] = {0, 0};
        for (int i = 1; i <= n; ++i) {
            int x, y; scanf("%d%d", &x, &y);
            mx[2 - x] = max(mx[2 - x], y);
        }
        if (mx[0] == mx[1]) {
            printf("%d\n", mx[0] + 2);
        }
        else if (mx[1] - mx[0] == 1 && mx[0] == 0) {
            printf("%d\n", mx[1] + 1);
        }
        else if (mx[1] - mx[0] == 1) {
            printf("%d\n", mx[1] + 2);
        }
        else if (mx[1] > mx[0]) {
            printf("%d\n", mx[1] + 1);
        }
        else {
            printf("%d\n", mx[0] + 2);
        }
    }
}
