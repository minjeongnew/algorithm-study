# 최대/ 최소의 가격을 가지도록 물건을 담는다면
# 물건을 담는다/안담는다 -> 0/1 knapsack -> 다이나믹 프로그래밍
# 물건을 쪼개서 담을 수 있다 -> fractional knapsack -> greedy

# 처음에 fractional knapsack으로 접근해 틀림

import sys


c, n = map(int, sys.stdin.readline().split())
cc = []
for _ in range(n):
    cost, customers = map(int, sys.stdin.readline().split())
    cc.append([cost, customers])
dp = [0] + [sys.maxsize] * (c+100)
for cost, customers in cc:
    for current_customers in range(customers, c+101):
        dp[current_customers] = min(dp[current_customers], dp[current_customers - customers] + cost)
        print(dp)
print(min(dp[c:c+101]))