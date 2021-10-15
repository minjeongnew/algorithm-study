from pprint import pprint


n = int(input())
board = [[0]*n for _ in range(n)]
v = [0]*(n*n)
students = {}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
for _ in range(n*n):
    tmp = list(map(int, input().split()))
    students[tmp[0]] = tmp[1:]
    max_r = 0
    max_c = 0
    max_like = -1
    max_empty = -1
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                like_cnt = 0
                empty_cnt = 0
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0 <= nx < n and 0 <= ny < n:
                        if board[nx][ny] in tmp:
                            like_cnt += 1
                        if board[nx][ny] == 0:
                            empty_cnt += 1
                if  max_like < like_cnt or (max_like == like_cnt and max_empty < empty_cnt):
                    max_r = i
                    max_c = j
                    max_like = like_cnt
                    max_empty = empty_cnt


    board[max_r][max_c] = tmp[0]
answer = 0
# pprint(board)
for i in range(n):
    for j in range(n):
        v = 0
        p = board[i][j]
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]
            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] in students[p]:
                    v += 1
        if v == 0:
            answer += 0
        elif v == 1:
            answer += 1
        elif v == 2:
            answer += 10
        elif v == 3:
            answer += 100
        elif v == 4:
            answer += 1000
print(answer)