import sys
from itertools import combinations

def get_distance(s1, e1, s2, e2):
    return abs(s1-s2) + abs(e1-e2)

n, m = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
chicken = []
home = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append([i, j])
        elif city[i][j] == 1:
            home.append([i, j])

answer = 0
for h in home:
    tmp = sys.maxsize
    for c in chicken:
        tmp = min(tmp, get_distance(h[0], h[1], c[0], c[1]))
    answer += tmp
print(answer)