from copy import deepcopy
n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
virus = []
candidates = []
for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            virus.append((i, j))
        elif board[i][j] == 0:
            candidates.append([i, j])

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def combination(array, n):
    for i in range(len(array)):
        if n == 1:
            yield [array[i]]
        else:
            for next in combination(array[i+1:], n-1):
                yield [array[i]] + next

def spread(array, r, c):
    if array[r][c] == 2:
        for k in range(4):
            nr = r + dx[k]
            nc = c + dy[k]
            if 0 <= nr < n and 0 <= nc < m and array[nr][nc] == 0:
                array[nr][nc] = 2
                spread(array, nr, nc)


clean_area = 0
combis = combination(candidates, 3)

def build_wall(array, combi):
    global clean_area
    copy_array = deepcopy(array)
    for r, c in combi:
        copy_array[r][c] = 1
    for r, c in virus:
        spread(copy_array, r, c)
    cur_clean_area = 0

    for i in range(n):
        for j in range(m):
            if copy_array[i][j] == 0:
                cur_clean_area += 1
    clean_area = max(clean_area, cur_clean_area)


for combi in combis:
    build_wall(board, combi)


print(clean_area)