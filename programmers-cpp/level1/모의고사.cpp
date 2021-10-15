#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

vector<int> solution(vector<int> answers) {
    vector<int> answer;
    vector<int> s1 = {1,2,3,4,5};
    vector<int> s2 = {2,1,2,3,2,4,2,5};
    vector<int> s3 = {3,3,1,1,2,2,4,4,5,5};
    int a1 = 0;
    int a2 = 0;
    int a3 = 0;
    for (int i=0;i<answers.size();i++) {
        if (answers[i] == s1[i%5]){
            a1 += 1;
        }
        if (answers[i] == s2[i%8]) {
            a2 += 1;
        }
        if (answers[i] == s3[i%10]) {
            a3 += 1;
        }
    }
    int a[3] = {a1, a2, a3};
    int max_ = max({a1,a2,a3});

    for (int i=0;i<3;i++) {
        if (a[i] == max_) {
            answer.push_back(i+1);
        }
    }
    return answer;
}