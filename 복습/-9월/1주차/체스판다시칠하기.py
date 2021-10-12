import sys

n, m = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(n)]

answer = []
for i in range(n-7):
    for j in range(m-7):
        b_count = 0
        w_count = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != "W": # 검은색이어야 하는데 아닌 경우
                        w_count += 1
                    if board[k][l] != "B": # 흰색이어야 하는데 아닌 경우
                        b_count += 1
                else:
                    if board[k][l] != 'B': # 흰색이어야 하는데 아닌경우
                        w_count += 1
                    if board[k][l] != 'W': # 검은색이어야 하는데 아닌경우
                        b_count += 1
        answer.append(min(b_count, w_count))
print(min(answer))