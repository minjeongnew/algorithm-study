import sys


v, e = map(int, sys.stdin.readline().split())
graph = [[float('inf')]*(v+1) for _ in range(v+1)]


for _ in range(e):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, v+1):
    for i in range(1, v+1):
        for j in range(1, v+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

answer = float('inf')
for i in range(1, v+1):
    answer = min(answer, graph[i][i])
if answer == float('inf'):
    print(-1)
else:
    print(answer)