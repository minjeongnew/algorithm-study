import sys
from collections import deque
# 북서 북 북동 동 동남 남 남서 서
d = [[-1, -1], [-1, 0], [-1, 1],
     [0, 1], [1, 1], [1, 0], [1, -1],[0, -1]]


def solve(w, h, m):
    cnt = 0
    v = [[0]*w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if m[i][j] == 1 and v[i][j] == 0:
                q = deque()
                q.append([i, j])
                cnt += 1
                while q:
                    x, y = q.popleft()
                    for k in range(8):
                        nx = x + d[k][0]
                        ny = y + d[k][1]
                        if 0 <= nx < h and 0 <= ny < w:
                            if m[nx][ny] == 1 and v[nx][ny] == 0:
                                q.append([nx, ny])
                                v[nx][ny] = 1
    return cnt


while True:
    w, h = map(int, sys.stdin.readline().split())
    if w == 0 and h == 0:
        break
    map_ = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
    print(solve(w, h, map_))