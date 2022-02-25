/**
 *    author:  tourist
 *    created: 10.04.2021 04:21:55       
**/
#include <bits/stdc++.h>

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tt;
  cin >> tt;
  for (int qq = 1; qq <= tt; qq++) {
    cout << "Case #" << qq << ": ";
    int n;
    cin >> n;
    vector<int> p(n);
    vector<long long> cnt(n);
    long long total = 0;
    for (int i = 0; i < n; i++) {
      cin >> p[i] >> cnt[i];
      total += cnt[i] * p[i];
    }
    long long ans = 0;
    for (long long x = total; x >= max(1LL, total - 10000LL); x--) {
      long long tmp = x;
      long long sum = 0;
      bool ok = true;
      for (int i = 0; i < n; i++) {
        long long cc = 0;
        while (tmp % p[i] == 0) {
          tmp /= p[i];
          cc += 1;
        }
        if (cc > cnt[i]) {
          ok = false;
          break;
        }
        sum += (cnt[i] - cc) * p[i];
      }
      if (ok && tmp == 1 && sum == x) {
        ans = x;
        break;
      }
    }
    cout << ans << '\n';
  }
  return 0;
}
