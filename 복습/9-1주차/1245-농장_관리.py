import sys
from collections import deque


d = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
infos = []
for i in range(n):
    for j in range(m):
        infos.append([i, j, graph[i][j]])
infos = sorted(infos, key=lambda x:-x[2])
v = [[0]*m for _ in range(n)]
cnt = 0
for info in infos:
    i, j, height = info
    if v[i][j] == 0:
        cnt += 1
        q = deque()
        q.append([i, j])
        while q:
            x, y = q.popleft()
            for k in range(8):
                nx = x + d[k][0]
                ny = y + d[k][1]
                if 0 <= nx < n and 0 <= ny < m:
                    if graph[x][y] >= graph[nx][ny] and v[nx][ny] == 0:
                        q.append([nx, ny])
                        v[nx][ny] = 1

print(cnt)