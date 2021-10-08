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


import sys
sys.setrecursionlimit(10**6)


def solution_dfs(maps):
    n, m = len(maps), len(maps[0])
    v = [[10001]*m for _ in range(n)]
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    def dfs(x, y, depth):
        v[x][y] = depth
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and v[nx][ny] > depth+1:
                dfs(nx, ny, depth+1)
    dfs(0, 0, 1)
    if v[-1][-1] == 10001:
        return -1
    return v[-1][-1]

