import sys


n, k = map(int, sys.stdin.readline().split())
ps = [[0,0]]+[list(map(int, sys.stdin.readline().split())) for _ in range(n)]
knapsack = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = ps[i][0]
        value = ps[i][1]
        if j < weight:
            knapsack[i][j] = knapsack[i-1][j]
        else:
            knapsack[i][j] = max(value+knapsack[i-1][j-weight], knapsack[i-1][j])
print(knapsack[n][k])


