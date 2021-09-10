# 실버3
import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
cnt = 0
end = 0
interval_sum = 0
for start in range(n):
    while interval_sum < m and end < n:
        interval_sum += a[end]
        end += 1
    if interval_sum == m:
        cnt += 1
    interval_sum -= a[start]
print(cnt)