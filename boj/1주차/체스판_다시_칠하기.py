n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]

answer = []
for i in range(n-7):
    for j in range(m-7):
        check_w, check_b = 0, 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l)%2 == 0:
                    if board[k][l] != 'B':
                        check_b += 1
                    if board[k][l] != 'W':
                        check_w += 1
                else:
                    if board[k][l] != 'W':
                        check_b += 1
                    if board[k][l] != 'B':
                        check_w += 1
        answer.append(min(check_b, check_w))

print(min(answer))
