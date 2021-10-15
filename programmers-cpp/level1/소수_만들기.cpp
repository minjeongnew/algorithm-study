#include <vector>
#include <iostream>
#include <cmath>
using namespace std;
bool isPrime(int n) {
    for (int i=2;i<int(sqrt(n))+1;i++) {
        if (n%i==0) return false;
    }
    return true;
}
int solution(vector<int> nums) {
    int answer = 0;
    int i, j, k, tmp;
    int n = nums.size();

    for(i=0;i<n;i++) {
        for(j=i+1;j<n;j++){
            for(k=j+1;k<n;k++) {
                tmp = nums[i]+nums[j]+nums[k];
                if(isPrime(tmp)) answer += 1;
            }
        }
    }

    return answer;
}