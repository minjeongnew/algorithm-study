import sys


# 도시 개수
n = int(sys.stdin.readline())
# 버스 개수
m = int(sys.stdin.readline())
MN = 100000*n
cities = [[MN] * n for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    cities[a-1][b-1] = min(cities[a-1][b-1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i == j:
                cities[i][j] = 0
            else:
                cities[i][j] = min(cities[i][j], cities[i][k] + cities[k][j])

for i in range(n):
    for j in range(n):
        if cities[i][j] == MN:
            print(0, end=' ')
        else:
            print(cities[i][j], end=' ')
    print()