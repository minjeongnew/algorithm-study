import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
v = [[0]*m for _ in range(n)]
graph = []
sharks = deque()
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    graph.append(tmp)
    for j in range(m):
        if graph[i][j] == 1:
            sharks.append([i, j])

d = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

while sharks:
    x, y = sharks.popleft()
    for k in range(8):
        nx = x + d[k][0]
        ny = y + d[k][1]
        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
            graph[nx][ny] = graph[x][y] + 1
            sharks.append([nx, ny])
safe_distance = 0

for i in range(n):
    for j in range(m):
        safe_distance = max(safe_distance, graph[i][j])

print(safe_distance-1)