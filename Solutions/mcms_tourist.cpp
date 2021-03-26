/**
 *    author:  tourist
 *    created: 11.04.2020 03:52:40    
 *    usage: 为带有通配符的子串计算最短公共母串 (MCMS)   
**/
#include <bits/stdc++.h>
using namespace std;

/**
INPUTS:
2
5
*CONUTS
*COCONUTS
*OCONUTS
*CONUTS
*S
2
*XZ
*XYZ

OUTPUTS:
Case #1: COCONUTS
Case #2: * 
**/


int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
  int tt;
  cin >> tt;
  for (int qq = 1; qq <= tt; qq++) {
    cout << "Case #" << qq << ": ";
    int n;
    cin >> n;
    vector<string> strs(n);
    for (int i = 0; i < n; i++) {
      cin >> strs[i];
    }
    string pref = "";
    string suf = "";
    vector<string> sub;
    bool ok = true;
    for (string& s : strs) {
      int last = -1;
      for (int i = 0; i < (int) s.size(); i++) {
        if (s[i] == '*') {
          if (last == -1) {
            string other_pref = s.substr(0, i);
            if (other_pref.size() > pref.size()) {
              swap(pref, other_pref);
            }
            if (pref.substr(0, other_pref.size()) != other_pref) {
              ok = false;
              break;
            }
          } else {
            sub.push_back(s.substr(last + 1, i - last - 1));
          }
          last = i;
        }
      }
      if (!ok) {
        break;
      }
      string other_suf = s.substr(last + 1);
      if (other_suf.size() > suf.size()) {
        swap(suf, other_suf);
      }
      if (suf.substr(suf.size() - other_suf.size()) != other_suf) {
        ok = false;
        break;
      }
    }
    if (!ok) {
      cout << "*" << '\n';
    } else {
      cout << pref;
      for (auto& s : sub) {
        cout << s;
      }
      cout << suf << '\n';
    }
  }
  return 0;
}
