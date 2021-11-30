import sys
import heapq
from pprint import pprint

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def solve(k, cave):
    dp = [[float('inf')]*k for _ in range(k)]
    sx, sy = 0, 0
    dp[sx][sy] = cave[sx][sy]
    q = []
    heapq.heappush(q, [dp[0][0], 0, 0]) # 도둑루피, 위치x, 위치y
    while q:
        cost, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < k and 0 <= ny < k:
                new_cost = cost + cave[nx][ny]
                if new_cost < dp[nx][ny]:
                    dp[nx][ny] = new_cost
                    heapq.heappush(q, [new_cost, nx, ny])
    # pprint(dp)
    return dp[k-1][k-1]


i = 1
while True:
    k = int(sys.stdin.readline())
    if k == 0:
        break
    cave = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
    print('Problem {}: {}'.format(i, solve(k, cave)))
    i += 1