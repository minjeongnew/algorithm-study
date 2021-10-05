# gold4
import sys


n, m, x, y, k = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
# 동: 1 서: 2 북: 3 남: 4
move_dict = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
moves = list(map(int, sys.stdin.readline().split()))
dice = [0]*6 # 위(앞면), 북, 동, 서, 남, 아래(닿는면)

for move in moves:
    d = move # 방향, 횟수
    nx = x + move_dict[d][0]
    ny = y + move_dict[d][1]

    if 0 <= nx < n and 0 <= ny < m:
        if d == 1: # 동쪽으로 굴리기
            dice[2], dice[0], dice[3], dice[5] = dice[5], dice[2], dice[0], dice[3]
        elif d == 2: # 서쪽으로 굴리기
            dice[2], dice[0], dice[3], dice[5] = dice[0], dice[3], dice[5], dice[2]
        elif d == 3: # 북쪽으로 굴리기
            dice[1], dice[0], dice[4], dice[5] = dice[5], dice[1], dice[0], dice[4]
        elif d == 4: # 남쪽으로 굴리기
            dice[1], dice[0], dice[4], dice[5] = dice[0], dice[4], dice[5], dice[1]

        if graph[nx][ny] == 0:
            graph[nx][ny] = dice[5]
        else:
            dice[5] = graph[nx][ny]
            graph[nx][ny] = 0
        x, y = nx, ny
        print(dice[0])