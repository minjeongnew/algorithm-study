from collections import deque


def solution(maps):
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    q = deque()
    q.append((0, 0))
    n, m = len(maps), len(maps[0])
    v = [[-1]*m for _ in range(n)]
    v[0][0] = 1
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and v[nx][ny] == -1:
                q.append((nx, ny))
                v[nx][ny] = v[x][y] + 1
    return v[-1][-1]