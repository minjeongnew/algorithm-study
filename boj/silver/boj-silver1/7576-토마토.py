import sys
from collections import deque


m, n = map(int, sys.stdin.readline().split())
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
q = deque()
ts = []
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    ts.append(tmp)
    for j in range(m):
        if ts[i][j] == 1:
            q.append([i, j])

def bfs():
    days = -1
    while q:
        days += 1
        for i in range(len(q)):
            x, y = q.popleft()
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < n and 0 <= ny < m and ts[nx][ny] == 0:
                    q.append([nx, ny])
                    ts[nx][ny] = ts[x][y] + 1
    for i in range(n):
        if 0 in ts[i]:
            return -1
    return days


print(bfs())