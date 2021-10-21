# from pprint import pprint
R, C, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

air_clear = []
for i in range(R):
    if board[i][0] == -1:
        air_clear.append((i, 0))
        air_clear.append((i+1, 0))
        break


directions = {0:(-1, 0), 1:(0, 1), 2: (1, 0), 3: (0, -1)}
def spread():
    global board
    new_board = [x[:] for x in board]
    new_board[air_clear[0][0]][air_clear[0][1]] = -1
    new_board[air_clear[1][0]][air_clear[1][1]] = -1
    for i in range(R):
        for j in range(C):
            if board[i][j] >= 5:
                cnt = 0
                spread_v = board[i][j] // 5
                for k in range(4):
                    nx = i + directions[k][0]
                    ny = j + directions[k][1]
                    if 0 <= nx < R and 0 <= ny < C and board[nx][ny] >= 0:
                        new_board[nx][ny] += spread_v
                        cnt += 1
                new_board[i][j] = new_board[i][j] - spread_v*cnt
    board = new_board

# 위 공기청정기 -> 시계 방향으로 1칸씩
def air1():
    global board
    # 범위 (0, 0) ~ (0, C)
    #     (x, 0) ~ (x, C)
    # 공기청정기 자리에 들어간 미세먼지는
    x = air_clear[0][0]
    new_board = [k[:] for k in board]
    # 하단 가로
    tmp = board[x][-1]
    for i in range(1, C-1):
        new_board[x][i+1] = board[x][i]
    new_board[x][1] = 0
    # 오른쪽 세로
    tmp2 = board[0][-1]
    for i in range(x):
        new_board[i][-1] = board[i+1][-1]
    new_board[0][-2] = tmp2
    # 상단 가로
    tmp3 = board[0][0]
    for i in range(C-1):
        new_board[0][i] = board[0][i+1]
    # 왼쪽 세로
    for i in range(x):
        new_board[i+1][0] = board[i][0]
    new_board[1][0] = tmp3
    new_board[x][0] = -1
    # 아래 공기청정기
    # 상단 가로
    tmp = board[x+1][-1]
    for i in range(1, C-1):
        new_board[x+1][i+1] = board[x+1][i]
    new_board[x+1][1] = 0
    # 하단 가로
    tmp3 = board[-1][0]
    for i in range(C-1):
        new_board[-1][i] = board[-1][i+1]
    # 오른쪽 세로
    tmp2 = board[R-1][-1]
    for i in range(x+1, R-1):
        new_board[i+1][-1] = board[i][-1]
    new_board[x+2][-1] = tmp
    # 왼쪽 세로
    for i in range(x+1, R-1):
        new_board[i][0] = board[i+1][0]
    new_board[x+1][0] = -1
    board= new_board




for _ in range(T):
    spread()
    # pprint(board)
    air1()
    # pprint(board)
answer = 0
for i in range(R):
    for j in range(C):
        if board[i][j] > 0:
            answer += board[i][j]
print(answer)
# pprint(board)
