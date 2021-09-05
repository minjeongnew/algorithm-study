import sys

n = int(sys.stdin.readline())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 0 and graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for i in range(n):
    print(*graph[i])