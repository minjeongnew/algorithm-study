#include <iostream>
#define MAX 15
using namespace std;


int col[MAX];
int n;
int total = 0;

bool adjacent(int x) {
    for (int i = 0; i < x; i++) {
        // 같은 행에 있으면 안됨 || 같은 대각선에 있으면 안됨
        if (col[x] == col[i] || abs(col[x]-col[i]) == x-i) {
            return false;
        }
    }
    return true;
}
void nqueens(int x) {
    if (x == n) total ++;
    else {
        for (int i=0; i < n; i++) {
            col[x] = i; // 해당 위치에 퀸을 위치시킨다
            if (adjacent(x)) nqueens(x+1);
        }
    }

}

int main() {
    cin >> n;
    nqueens(0);
    cout << total;
}