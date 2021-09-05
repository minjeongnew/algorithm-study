import sys
from collections import deque


n = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
info = set()
for i in range(n):
    for j in range(n):
        info.add(area[i][j])

info.add(0)
info = sorted(info)
# print(info)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(start_h):
    cnt = 0
    v = [[0]*n for _ in range(n)]
    q = deque()
    for i in range(n):
        for j in range(n):
            if area[i][j] > start_h and v[i][j] == 0:
                q.append([i, j])
                v[i][j] = 1
                cnt += 1
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if area[nx][ny] > start_h and v[nx][ny] == 0:
                                q.append([nx, ny])
                                v[nx][ny] = 1

    return cnt


answer = 0
for h in info:
    answer = max(answer, bfs(h))
print(answer)