import sys
from collections import deque


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n = int(sys.stdin.readline())
area = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(n)]
rg_area = [['']*n for _ in range(n)]


def bfs(arr, i, j):
    q = deque()
    q.append([i, j, arr[i][j]])
    arr[i][j] = ''
    while q:
        x, y, value = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if arr[nx][ny] == value:
                    q.append([nx, ny, arr[nx][ny]])
                    arr[nx][ny] = ''


for i in range(n):
    for j in range(n):
        if area[i][j] == 'R' or area[i][j] == 'G':
            rg_area[i][j] = 'R'
        else:
            rg_area[i][j] = area[i][j]

cnt, cnt2 = 0, 0
for i in range(n):
    for j in range(n):
        if area[i][j] != '':
            bfs(area, i, j)
            cnt += 1
        if rg_area[i][j] != '':
            bfs(rg_area, i, j)
            cnt2 += 1
print(cnt, cnt2)
