import sys
from pprint import pprint
from collections import deque


n, m = map(int, sys.stdin.readline().split())
farm = []

for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    farm.append(tmp)
ps = []
for x in range(n):
    for y in range(m):
        datas = [x, y, farm[x][y]]
        ps.append(datas)
ps = sorted(ps, key=lambda x: -x[2])
d = [[-1, -1], [-1, 0], [-1, 1],
     [0, -1], [0, 1],
     [1, -1], [1, 0], [1, 1]]
# pprint(farm)
v = [[-1]*m for _ in range(n)]

# print(ps)
for i in range(len(ps)):
    q = deque()
    start = ps[i]
    pivot = start[2]
    q.append(start)
    if v[start[0]][start[1]] == -1:
        v[start[0]][start[1]] = 1
        while q:
            # print(q)
            x, y, data = q.popleft()
            for k in range(8):
                dx, dy = d[k]
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and v[nx][ny] == -1:
                    if pivot >= farm[nx][ny] and farm[nx][ny] <= farm[x][y]:
                        q.append([nx, ny, farm[nx][ny]])
                        v[nx][ny] = 0
answer = 0
for i in range(n):
    for j in range(m):
        if v[i][j]:
            answer += 1
print(answer)
