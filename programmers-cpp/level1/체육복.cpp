#include <string>
#include <vector>
#include <iostream>
using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve) {
    int answer = 0;
    vector <int> c(n,1);
    int i;
    for(auto l:lost) c[l-1] -= 1;
    for(auto r:reserve) c[r-1] += 1;
    for(i=0;i<n;i++) {
        if (c[i] == 0) {
            if (i!=0 && c[i-1] == 2) {
                c[i] += 1;
                c[i-1] -= 1;
            } else if(i!=n-1 && c[i+1] == 2) {
                c[i] += 1;
                c[i+1] -= 1;
            }
        }
    }

    for(i=0;i<n;i++) {
        if (c[i] >0) answer++;
    }
    return answer;
}