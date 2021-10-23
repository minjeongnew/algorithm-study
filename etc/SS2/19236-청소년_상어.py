from copy import deepcopy
directions = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]
fishes = {}
board = [[[] for __ in range(4)] for _ in range(4)]
for i in range(4):
    tmp = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = [tmp[2*j], tmp[2*j+1]-1]

def find_fish_position(array, idx):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == idx:
                return (i, j)
    return None


def move_fish(array, shark_x, shark_y):
    position = []
    for i in range(1, 17):
        position = find_fish_position(array, i)
        if position == None:
            continue
        x, y = position[0], position[1]
        direction = array[x][y][1]
        for _ in range(8):
            nx = x + directions[direction][0]
            ny = y + directions[direction][1]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == shark_x and ny == shark_y):
                    array[x][y][0], array[nx][ny][0] = array[nx][ny][0], array[x][y][0]
                    array[x][y][1], array[nx][ny][1] = array[nx][ny][1], direction
                    break
            direction = (direction+1)%8


def food_candidate(array, x, y):
    positions = []
    direction = array[x][y][1]
    for i in range(1, 4):
        nx = x + directions[direction][0]
        ny = y + directions[direction][1]
        if 0 <= nx < 4 and 0 <= ny < 4 and 1 <= array[nx][ny][0] <= 16:
            positions.append((nx, ny))
        x, y = nx, ny
    return positions


def dfs(array, x, y, total):
    global answer
    array = deepcopy(array)
    fish_num = array[x][y][0]
    array[x][y][0] = -1
    # 물고기 이동
    move_fish(array, x, y)
    # 상어 밥
    fish_candidates = food_candidate(array, x, y)
    answer = max(answer, fish_num+total)
    for nx, ny in fish_candidates:
        dfs(array, nx, ny, total+fish_num)


answer = 0
dfs(board, 0, 0, 0)
print(answer)