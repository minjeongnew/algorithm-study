import copy
import sys


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, sys.stdin.readline().split())
lab = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
clean_area = 0
virus = []
for i in range(n):
    for j in range(m):
        if lab[i][j] == 2:
            virus.append([i, j])


def select_wall(start, cnt):
    global clean_area
    if cnt == 3:
        copy_lab = copy.deepcopy(lab)
        for i in range(len(virus)):
            r, c, = virus[i]
            spread_virus(r, c, copy_lab)
        cur_clean_area = sum(col.count(0) for col in copy_lab)
        clean_area = max(clean_area, cur_clean_area)
        return
    else:
        for i in range(start, n*m):
            r = i // m
            c = i % m
            if lab[r][c] == 0:
                lab[r][c] = 1
                select_wall(i, cnt + 1) # 벽 선택
                lab[r][c] = 0


def spread_virus(r, c, copy_lab_):
    if copy_lab_[r][c] == 2:
        for k in range(4):
            nr = r + dx[k]
            nc = c + dy[k]
            if 0 <= nr < n and 0 <= nc < m:
                if copy_lab_[nr][nc] == 0:
                    copy_lab_[nr][nc] = 2
                    spread_virus(nr, nc, copy_lab_)


select_wall(0, 0)
print(clean_area)