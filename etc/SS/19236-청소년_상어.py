from copy import deepcopy
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
board = [[[] for __ in range(4)] for _ in range(4)]
tmp = [list(map(int, input().split())) for _ in range(4)]


def food(array, x, y): # 상어가 먹을 수 있는 후보
    positions = []
    direction = array[x][y][1]
    for i in range(1, 4):
        nx = x + directions[direction][0]
        ny = y + directions[direction][1]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny][0] <= 16:
            positions.append((nx, ny))
        x, y = nx, ny
    return positions


def find_fish(array, idx):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == idx:
                return (i, j)
    return None


def move_fish(array, cx, cy):
    position = []
    for i in range(1, 17):
        position = find_fish(array, i)
        if position is None:
            continue
        x, y = position[0], position[1]
        direction = array[x][y][1]
        for _ in range(8):
            nx = x + directions[direction][0]
            ny = y + directions[direction][1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == cx and ny == cy):
                    array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                    array[x][y][1], array[nx][ny][1] = array[nx][ny][1], direction
                    break
            direction = (direction+1) % 8


def dfs(array, x, y, totals):
    global answer
    array = deepcopy(array)
    # 해당 위치 물고기 먹기
    number = array[x][y][0]
    array[x][y][0] = -1
    # 물고기 이동
    move_fish(array, x, y)
    # 상어 이동할 수 있는 후보 확인
    result_positions = food(array, x, y)
    answer = max(answer, totals+number)
    for nx, ny in result_positions:
        dfs(array, nx, ny, totals+number)


for p in range(4):
    for q in range(4):
        board[p][q] = [tmp[p][q*2], tmp[p][q*2+1]-1]
answer = 0
dfs(board, 0, 0, 0)
print(answer)