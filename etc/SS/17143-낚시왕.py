R, C, M = map(int, input().split())
shark_dict = dict()
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    shark_dict[z] = [r-1, c-1, s, d] # s 속력, d 방향

# 1 위, 2 아래, 3 오른쪽, 4 왼쪽
directions = {1: (-1, 0), 2: (1, 0), 3: (0, 1), 4: (0, -1)}
board = [[0]*C for _ in range(R)]
for shark_size, shark_info in shark_dict.items():
    r, c, s, d = shark_info
    board[r][c] = shark_size
def print_arr(arr):
    for x in arr:
        print(*x)
get_shark = 0

def switch_direction(d):
    if d == 1:
        return 2
    if d == 2:
        return 1
    if d == 3:
        return 4
    if d == 4:
        return 3
# 낚시왕이 열의 끝까지 가면 중단
def solve(fisher_c): # 하나의 과정
    global get_shark, board, shark_dict
    for i in range(R):
        if board[i][fisher_c] != 0:
            s_size = board[i][fisher_c]
            get_shark += s_size
            del shark_dict[s_size]
            break
    # 상어의 이동
    tmp_board = [[0]*C for _ in range(R)]
    out = []
    for shark_size, shark_info in shark_dict.items():
        nx, ny, s, d = shark_info
        tmp_s = s
        while tmp_s > 0:
            dx, dy = directions[d]

            nx += dx
            ny += dy
            if 0 <= nx < R and 0 <= ny < C:
                tmp_s -= 1
            else:
                nx -= dx
                ny -= dy
                d = switch_direction(d)

        if tmp_board[nx][ny] == 0:
            tmp_board[nx][ny] = shark_size
            shark_dict[shark_size] = [nx, ny, s, d]
        else:
            if tmp_board[nx][ny] < shark_size: # 이미 들어가 있는애가 작을 떄
                smaller = tmp_board[nx][ny]
                out.append(smaller)
                tmp_board[nx][ny] = shark_size
                shark_dict[shark_size] = [nx, ny, s, d]
            else:
                out.append(shark_size)
    for x in out:
        del shark_dict[x]
    board = tmp_board

for j in range(C):
    solve(j)
print(get_shark)





