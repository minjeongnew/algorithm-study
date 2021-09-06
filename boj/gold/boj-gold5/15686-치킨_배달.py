import sys
from itertools import combinations
from pprint import pprint

n, m = map(int, sys.stdin.readline().split())
# m: 남겨둘 치킨 가게 수

city = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
home = []
chicken = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])


def find_distance(home, chicken):
    distance = 0
    for h in home:
        tmp = sys.maxsize
        for c in chicken:
            tmp = min(tmp, abs((h[0]-c[0])) + abs((h[1]-c[1])))
        distance += tmp
        # print(distance)
    return distance


# 치킨 가게 후보
remove_chickens = list(combinations(chicken, m))
# pprint(remove_chickens)
distance = sys.maxsize
for combi_rc in remove_chickens:
    distance = min(distance, find_distance(home, combi_rc))

print(distance)