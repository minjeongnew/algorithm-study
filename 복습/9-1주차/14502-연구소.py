import sys
import copy


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
n, m = map(int, sys.stdin.readline().split())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
virus = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            virus.append([i, j])

def select_wall(start, cnt):
    global safe_area
    if cnt == 3:
        cur_safe_area = 0
        copy_graph = copy.deepcopy(graph)
        for i in range(len(virus)):
            r, c = virus[i]
            spread_virus(r, c, copy_graph)
        cur_safe_area = sum(i.count(0) for i in copy_graph)
        safe_area = max(safe_area, cur_safe_area)
        return
    else:
        for i in range(start, n*m):
            r = i // m
            c = i % m
            if graph[r][c] == 0:
                graph[r][c] = 1
                select_wall(i, cnt+1)
                graph[r][c] = 0


def spread_virus(r, c, copy_graph):
    if copy_graph[r][c] == 2:
        for k in range(4):
            nr = r + dx[k]
            nc = c + dy[k]
            if 0 <= nr < n and 0 <= nc < m:
                if copy_graph[nr][nc] == 0:
                    copy_graph[nr][nc] = 2
                    spread_virus(nr, nc, copy_graph)


safe_area = 0
select_wall(0, 0)
print(safe_area)