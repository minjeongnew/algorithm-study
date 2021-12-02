import sys
import heapq


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def solve(k, graph):
    answer = 0
    dp = [[float('inf')]*k for _ in range(k)]
    q = []
    dp[0][0] = graph[0][0]
    heapq.heappush(q, [dp[0][0], 0, 0])
    while q:
        cost, x, y = heapq.heappop(q)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < k and 0 <= ny < k and cost + graph[nx][ny] < dp[nx][ny]:
                dp[nx][ny] = cost + graph[nx][ny]
                heapq.heappush(q, [dp[nx][ny], nx, ny])

    return dp[k-1][k-1]


i = 1
while True:
    k = int(sys.stdin.readline())
    if k == 0:
        break
    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
    print("Problem {}: {}".format(i, solve(k, graph)))
    i += 1