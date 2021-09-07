import sys

sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = [[i, j] for j in range(9) for i in range(9) if sudoku[i][j] == 0]


def is_promising(i, j):
    promising = set(x for x in range(1, 10))
    removed = set()
    for k in range(9):
        if sudoku[i][k] in promising:
            removed.add(sudoku[i][k])
        if sudoku[k][j] in promising:
            removed.add(sudoku[k][j])
    promising -= removed
    # 3*3박스
    i //= 3
    j //= 3
    removed = set()
    for p in range(i*3, (i+1)*3):
        for q in range(j*3, (j+1)*3):
            if sudoku[p][q] in promising:
                removed.add(sudoku[p][q])
    promising -= removed
    return promising


flag = False # 출력되었는지 확인


def dfs(x):
    global flag
    if flag: # 답이 출력되었는지
        return
    if x == len(zeros):
        for row in sudoku:
            print(*row)
        flag = True
        return
    else:
        i, j = zeros[x]
        promising = is_promising(i, j)
        for num in promising:
            sudoku[i][j] = num
            dfs(x+1)
            sudoku[i][j] = 0
dfs(0)

# pypy로 제출해야함
# 하지만 이 코드도 시간초과