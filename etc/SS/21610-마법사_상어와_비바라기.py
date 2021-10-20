from pprint import pprint

n, m = map(int, input().split())
directions = {1:(0, -1), 2:(-1, -1), 3:(-1, 0), 4:(-1, 1), 5:(0, 1), 6:(1, 1), 7:(1, 0), 8:(1, -1)}
board = [list(map(int, input().split())) for _ in range(n)]
ds = [list(map(int, input().split())) for _ in range(m)]

# 비바라기
biba = [[0]*n for _ in range(n)]
biba[n-2][0] = 1
biba[n-2][1] = 1
biba[n-1][0] = 1
biba[n-1][1] = 1

# 대각선
cross = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
for turn in range(m):
    d, s = ds[turn]
    nsx = directions[d][0]*s
    nsy = directions[d][1]*s
    new_biba = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_biba[(i+nsx)%n][(j+nsy)%n] = biba[i][j]
    biba = new_biba
    for i in range(n):
        for j in range(n):
            if biba[i][j]:
                board[i][j] += 1

    for i in range(n):
        for j in range(n):
            if biba[i][j]:
                for k in range(4):
                    nx = i + cross[k][0]
                    ny = j + cross[k][1]
                    if 0 <= nx < n and 0 <= ny < n and board[nx][ny]:
                        board[i][j] += 1
    new_biba = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] >= 2 and biba[i][j] == 0:
                board[i][j] -= 2
                new_biba[i][j] = 1
    biba = new_biba

answer = 0
for i in range(n):
    for j in range(n):
        answer += board[i][j]
print(answer)