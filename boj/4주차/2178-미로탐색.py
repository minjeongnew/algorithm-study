import sys
from collections import deque


n, m = map(int, sys.stdin.readline().split())
# bfs
def bfs(maze):
    v = [[0]*m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    v[0][0] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if v[nx][ny] == 0 and maze[nx][ny] == 1:
                    q.append((nx, ny))
                    v[nx][ny] += v[x][y] + 1
    return v[-1][-1]


maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
print(bfs(maze))