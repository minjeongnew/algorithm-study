#include <string>
#include <vector>
#include <map>
using namespace std;

int solution(string s) {
    int answer = 0;
    map<string, string> m;
    m["zero"] = "0";
    m["one"] = "1";
    m["two"] = "2";
    m["three"] = "3";
    m["four"] = "4";
    m["five"] = "5";
    m["six"] = "6";
    m["seven"] = "7";
    m["eight"] = "8";
    m["nine"] = "9";
    string curs;
    string result;
    for (int i=0;i<s.length();i++) {
        if(isdigit(s[i]) == 0) {
            curs += s[i];
            if (m[curs] !="") {
                result += m[curs];
                curs = "";
            }
        } else{
            result += s[i];
        }
    }
    return stoi(result);
}