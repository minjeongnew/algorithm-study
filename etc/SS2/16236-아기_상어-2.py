from pprint import pprint
from collections import deque

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
fish_cnt = 0
shark_size = 2
shark = (0, 0)
sx, sy = 0, 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 9:
            shark = (i, j)
            sx = i
            sy = j
        elif 0 < board[i][j] <= 6:
            fish_cnt += 1
board[sx][sy] = 0


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
def bfs(shark_x, shark_y):
    v = [[0]*n for _ in range(n)]
    q = deque()
    q.append((shark_x, shark_y, 0))
    min_distance = float('inf')
    dist_list = []
    while q:
        x, y, distance = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n and v[nx][ny] == 0:
                if board[nx][ny] <= shark_size:
                    v[nx][ny] = 1
                    if 0 < board[nx][ny] < shark_size:
                        min_distance = distance
                        dist_list.append((distance+1, nx, ny))
                    if distance + 1 <= min_distance:
                        q.append((nx, ny, distance+1))
    if dist_list:
        dist_list.sort()
        return dist_list[0]
    else:
        return 0

eat_cnt = 0
time = 0
while fish_cnt:
    result = bfs(sx, sy)
    if result == 0:
        break
    distance = result[0]
    sx, sy = result[1], result[2]
    time += distance
    eat_cnt += 1
    fish_cnt -= 1
    if eat_cnt == shark_size:
        eat_cnt = 0
        shark_size += 1
    board[sx][sy] = 0
print(time)