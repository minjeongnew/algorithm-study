import sys
sys.setrecursionlimit(10**6)


sudoku = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]
zeros = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            zeros.append([i, j])


def get_promising(x, y):
    # 행, 열
    nums = set(i for i in range(1, 10))
    removed = set()
    for i in range(9):
        if sudoku[x][i] in nums:
            removed.add(sudoku[x][i])
        if sudoku[i][y] in nums:
            removed.add(sudoku[i][y])
    nums -= removed
    # 3*3
    x //= 3
    y //= 3
    removed = set()
    for i in range(x*3, (x+1)*3):
        for j in range(y*3, (y+1)*3):
            if sudoku[i][j] in nums:
                nums.remove(sudoku[i][j])
    nums -= removed
    return nums

is_print = False

def dfs(x):
    global is_print
    if is_print:
        return
    if x == len(zeros):
        for row in sudoku:
            print(*row)
        is_print = True
        return
    else:
        i, j = zeros[x]
        promising = get_promising(i, j)
        for num in promising:
            sudoku[i][j] = num
            dfs(x+1)
            sudoku[i][j] = 0

dfs(0)

