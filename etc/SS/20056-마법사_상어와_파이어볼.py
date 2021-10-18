direction = {0: (-1, 0), 1: (-1, 1), 2: (0, 1), 3: (1, 1), 4: (1, 0), 5: (1, -1), 6: (0, -1), 7: (-1, -1)}
n, m, k = map(int, input().split())
board = [[[] for __ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    board[r-1][c-1].append([m, s, d])


def solve():
    global board
    turn_board = [[[] for __ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # print(board[i][j])
            if board[i][j]:
                ijlist = board[i][j]
                for x in ijlist:
                    m, s, d = x # 질량, 속력, 방향
                    # 방향과 속력
                    nx = (i + direction[d][0]*s) % n
                    ny = (j + direction[d][1]*s) % n
                    turn_board[nx][ny].append([m, s, d])
    for i in range(n):
        for j in range(n):
            if len(turn_board[i][j]) >= 2:
                sum_m = 0
                sum_s = 0
                s_odd = 0
                s_even = 0
                len_fireballs = len(turn_board[i][j])
                for x in turn_board[i][j]:
                    m, s, d = x
                    sum_m += m
                    sum_s += s
                    if d % 2 == 0:
                        s_even += 1
                    else:
                        s_odd += 1
                new_m = sum_m // 5
                new_s = sum_s // len_fireballs
                if new_m == 0:
                    new_fireballs = []
                else:
                    if s_odd == len_fireballs or s_even == len_fireballs:
                        new_fireballs = [[new_m, new_s, 0], [new_m, new_s, 2], [new_m, new_s, 4], [new_m, new_s, 6]]
                    else:
                        new_fireballs = [[new_m, new_s, 1], [new_m, new_s, 3], [new_m, new_s, 5], [new_m, new_s, 7]]
                turn_board[i][j] = new_fireballs
    board = turn_board

for _ in range(k):
    solve()
answer = 0
for i in range(n):
    for j in range(n):
        if board[i][j]:
            for x in board[i][j]:
                answer += x[0]
print(answer)