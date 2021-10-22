from pprint import pprint
from collections import deque
shark_size = 2
shark = (0, 0)
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

fish_cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark = (i, j)
        elif 0 < board[i][j] <= 6:
            fish_cnt += 1
board[shark[0]][shark[1]] = 0
dx = [-1, 1, 0, 0] # 상하좌우
dy = [0, 0, -1, 1]


time = 0

def bfs(sx, sy):
    global board, time
    q = deque()
    q.append((sx, sy, 0))
    v = [[0]*n for _ in range(n)]
    min_dist = float('inf')
    dist_list = []
    while q:
        x, y, dist = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                if board[nx][ny] <= shark_size:
                    v[nx][ny] = 1
                    if 0 < board[nx][ny] < shark_size:
                        min_dist = dist
                        dist_list.append((dist+1, nx, ny))
                    if dist + 1 <= min_dist:
                        q.append((nx, ny, dist+1))
    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return 0

eat_cnt = 0
sx, sy = shark
while fish_cnt:
    result = bfs(sx, sy)
    if result == 0:
        break
    sx, sy = result[1], result[2]
    time += result[0]
    eat_cnt += 1
    fish_cnt -= 1
    if eat_cnt == shark_size:
        shark_size += 1
        eat_cnt = 0
    board[sx][sy] = 0

print(time)