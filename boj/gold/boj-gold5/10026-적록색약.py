import sys
from collections import deque

n = int(sys.stdin.readline())
area = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs1():
    cnt = 0
    v = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if v[i][j] == 0:
                q = deque()
                q.append([i, j, area[i][j]])
                cnt += 1
                while q:
                    x, y, color = q.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if 0 <= nx < n and 0 <= ny < n:
                            if color == area[nx][ny] and v[nx][ny] == 0:
                                q.append([nx, ny, area[nx][ny]])
                                v[nx][ny] = 1
    return cnt


answer = [bfs1()]
for i in range(n):
    for j in range(n):
        if area[i][j] == 'R':
            area[i][j] = 'G'
answer.append(bfs1())
print(*answer)

