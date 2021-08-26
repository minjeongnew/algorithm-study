import sys
from pprint import pprint


n = int(sys.stdin.readline())
f = [list(map(str, sys.stdin.readline().strip())) for _ in range(n)]
v = [[0]*n for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                if f[i][j] == "Y" or (f[i][k] == "Y" and f[k][j] == "Y"):
                    v[i][j] = 1

answer = 0
for i in range(n):
    answer = max(answer, sum(v[i]))
print(answer)