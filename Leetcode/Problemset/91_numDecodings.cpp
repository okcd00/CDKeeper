class Solution {
public:
    int numDecodings(string s) {
        if(s.empty()) return 0;
        int pre = -1, cur = 1, tmp;
        for(int i = 1; i <= s.length(); ++i){
            tmp = cur;
            if(s[i-1] == '0'){
                if(isCode(s, i-2, i-1)) cur = pre;
                else return 0;
            }else if(isCode(s, i-2, i-1))
                cur += pre;;
            pre = tmp;
        }
        return cur;
    }
private:
    bool isCode(string &s, int i, int j){
        if(i < 0) return false;
        if(s[i] >= '3' || s[i] == '0') return false;
        if(s[i] == '2' && s[j] >= '7') return false;
        return true;
    }
};