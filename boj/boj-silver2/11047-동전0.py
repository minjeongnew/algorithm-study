import sys

n, k = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(n)]
coins = coins[::-1]
answer = 0
for coin in coins:
    answer += k // coin
    k %= coin
print(answer)