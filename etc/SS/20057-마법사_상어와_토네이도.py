from pprint import pprint
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
turns = n*2 - 1

left_spread = [(1, 1, 0.01), (-1, 1, 0.01), (1, 0, 0.07), (-1, 0, 0.07), (1, -1, 0.1),
               (-1, -1, 0.1), (2, 0, 0.02), (-2, 0, 0.02), (0, -2, 0.05), (0, -1, 0)]
right_spread = [(x, -y, z) for x, y, z in left_spread]
down_spread = [(-y, x, z) for x, y, z in left_spread]
up_spread = [(y, x, z) for x, y, z in left_spread]
directions = {0: left_spread, 1: down_spread, 2: right_spread, 3: up_spread}
answer = 0
# n이 3 -> 1, 1, 2, 2, 2
# n이 5 -> 1, 1, 2, 2, 3, 3, 4, 4, 4
# n이 7 -> 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 6


def spread(x, y, direction): # y의 좌표
    global board, answer
    if y < 0:
        return
    total = 0
    for dx, dy, z in direction:
        nx = x + dx
        ny = y + dy
        if z == 0:
            new_sand = board[x][y] - total
        else:
            new_sand = int(board[x][y]*z)
            total += new_sand
        if 0 <= nx < n and 0 <= ny < n:
            board[nx][ny] += new_sand
        else:
            answer += new_sand


dx = [0, 1, 0, -1] # 왼, 아래, 오른쪽, 위
dy = [-1, 0, 1, 0]
time = 0
x, y = n//2, n//2
for i in range(turns):
    d = i % 4
    if d == 0 or d == 2: # 다음 회차가 d == 0이거나 right d == 2이면 한번 더
        time += 1
    for _ in range(time):
        nx = x + dx[d]
        ny = y + dy[d]
        spread(nx, ny, directions[d])
        x, y = nx, ny
print(answer)