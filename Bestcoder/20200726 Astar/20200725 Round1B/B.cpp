#include <bits/stdc++.h>
using namespace std;
long long arr[100005];
int main() {
    ios::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);
    long long T, n;
    long long ans;
    cin >> T;
    while (T--) {
        cin >> n;
        for (long long i = 0; i < n; i++) cin >> arr[i];
        sort(arr, arr + n); ans = 0;
        for (long long i = 1; i < n; i++) ans += (arr[i] - arr[i-1]) * (n - i) * i;
        cout << ans << endl;
    }
    return 0;
}
