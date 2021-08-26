import sys
from pprint import pprint


n, m = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
b = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]


def convert_elem(i, j):
    for k in range(i, i+3):
        for l in range(j, j+3):
            a[k][l] = 1 - a[k][l]


answer = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            convert_elem(i, j)
            answer += 1
if a != b:
    print(-1)
else:
    print(answer)
