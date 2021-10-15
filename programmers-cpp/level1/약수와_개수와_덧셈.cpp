#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int solve(int n) {
    vector <int> tmp;
    for (int i = 1; i<int(sqrt(n))+1; i++) {
        if (n % i == 0) {
            tmp.push_back(i);
            tmp.push_back(n/i);
        }
    }
    sort(tmp.begin(), tmp.end());
    tmp.erase(unique(tmp.begin(), tmp.end()), tmp.end());
    return tmp.size();
}
int solution(int left, int right) {
    int answer = 0;
    int x;
    for (int i=left;i<=right;i++){
        x = solve(i);
        if (x%2 == 0) {
            answer += i;
        }
        else answer -= i;

    }
    return answer;
}