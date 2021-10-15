#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<int> d, int budget) {
    int answer = 0;
    int bd = budget;
    sort(d.begin(), d.end());
    for(int i=0;i<d.size();i++) {
        if (d[i] <= bd) {
            answer += 1;
            bd -= d[i];
        }
    }
    return answer;
}