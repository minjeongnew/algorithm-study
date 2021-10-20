from collections import deque
from pprint import pprint
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(r, c, idx):
    global board, v
    q = deque()
    q.append((r, c))
    color = board[r][c]
    area = 1
    rainbow = 0
    v[r][c] = idx
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == color and v[nx][ny] == 0:
                    v[nx][ny] = idx
                    area += 1
                    q.append((nx, ny))
                elif board[nx][ny] == 0 and idx not in v[nx][ny]:
                    v[nx][ny].append(idx)
                    q.append((nx, ny))
                    area += 1
                    rainbow += 1
    return area, rainbow


score = 0


def remove_block_group(idx):
    global board, score
    cnt = 0
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and v[i][j] == idx:
                board[i][j] = -2
                cnt += 1
            elif board[i][j] == 0 and idx in v[i][j]:
                board[i][j] = -2
                cnt += 1
    score += (cnt**2)
# 밑에서부터 센다
def fall(x, y):
    global board
    flag = 0
    for i in range(x+1, n):
        nx = i
        if board[i][y] > -2:
            flag = 1
            break
    if flag:
        board[nx-1][y] = board[x][y]
    else:
        board[nx][y] = board[x][y]
    board[x][y] = -2


while True:
    block_groups = []
    q = deque()
    v = [[0] * n for _ in range(n)]
    idx = 1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                v[i][j] = []
    for i in range(n):
        for j in range(n):
            if board[i][j] > 0 and v[i][j] == 0:
                cnt, rainbow = bfs(i, j, idx)
                if cnt > 1:
                    block_groups.append((cnt, rainbow, i, j, idx))
                idx += 1

    if not block_groups:
        break

    block_groups.sort()
    pivot = block_groups[-1]

    remove_block_group(pivot[-1])

    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] >= 0 and board[i+1][j] == -2:
                fall(i, j)
    # pprint(board)
    new_board = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_board[n-1-j][i] = board[i][j]
    board = new_board
    for i in range(n-2, -1, -1):
        for j in range(n):
            if board[i][j] >= 0 and board[i+1][j] == -2:
                fall(i, j)
    # print(score)
print(score)
# (0,1)->(3,0)
# (0, 3) -> (1, 0)