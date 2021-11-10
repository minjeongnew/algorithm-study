import sys

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
for k in range(n):
    for i in range(n):
        for j in range(n):
            if i != j:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    if graph[a-1][b-1] <= c:
        print("Enjoy other party")
    else:
        print("Stay here")