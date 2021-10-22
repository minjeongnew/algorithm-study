from pprint import pprint


n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
sharks = {}
cur_sharks = {i+1: (0, 0, 0) for i in range(m)}
shark_dir_tmp = list(map(int, input().split()))
shark_directions = {i+1: shark_dir_tmp[i] for i in range(m)}
for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            cur_sharks[board[i][j]] = (i, j, shark_directions[board[i][j]])

time_board = [[0]*n for _ in range(n)]
for shark_num, shark in cur_sharks.items():
    x, y, d = shark
    time_board[x][y] = k

shark_dict = {i+1: dict() for i in range(m)} # shark 번호
for i in range(m):
    # 위를 향할 때의 우선순위
    shark_dict[i+1][1] = list(map(int, input().split()))
    # 아래를 향할 때의 우선순위
    shark_dict[i+1][2] = list(map(int, input().split()))
    # 왼쪽을 향할 때의 우선순위
    shark_dict[i+1][3] = list(map(int, input().split()))
    # 오른쪽을 향할 때의 우선순위
    shark_dict[i+1][4] = list(map(int, input().split()))

directions = {1: (-1, 0), 2: (1, 0), 3: (0, -1), 4: (0, 1)}


def move_shark():
    global out, time, cur_sharks, board, time_board
    for shark_num, shark in cur_sharks.items():
        x, y, d = shark # 상어 위치, 상어 머리 향하는 방향
        flag = False # False-> 내 냄새 있는 곳만 갈 수 있다,,
        for direction in shark_dict[shark_num][d]:
            nx = x + directions[direction][0]
            ny = y + directions[direction][1]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                flag = True
                cur_sharks[shark_num] = (nx, ny, direction)
                break
        if not flag:
            for direction in shark_dict[shark_num][d]:
                nx = x + directions[direction][0]
                ny = y + directions[direction][1]
                if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == shark_num:
                    cur_sharks[shark_num] = (nx, ny, direction)
                    break
    # 시간 줄이기...
    for i in range(n):
        for j in range(n):
            if time_board[i][j] > 0:
                time_board[i][j] -= 1
            if time_board[i][j] == 0:
                board[i][j] = 0
    tmp = []
    for shark_num, shark in cur_sharks.items():
        x, y, d = shark
        if board[x][y] == 0 or board[x][y] == shark_num: # 비어있거나 상어 본인 자취면
            board[x][y] = shark_num
            time_board[x][y] = k  # 시간
        elif board[x][y] != shark_num:
            out += 1
            tmp.append(shark_num) # 아웃할 상어들 목록
    for sn in tmp:
        del cur_sharks[sn]
        # 4방향 확인하기

    time += 1
out = 0 # 쫒겨난 상어 수
time = 0
while True:
    if time > 1000:
        break
    if out == m-1:
        break
    # pprint(board)
    move_shark()
    # pprint(board)
    # pprint(time_board)
    # print(cur_sharks)
    # print("---------")
if time > 1000:
    time = -1
print(time)