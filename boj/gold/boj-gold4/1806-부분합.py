# 투포인터 알고리즘
import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
sum_ = [0] * (n+1)
for i in range(1, n+1):
    sum_[i] = sum_[i-1] + nums[i-1]
answer = sys.maxsize
start = 0
end = 1
while start != n:
    if sum_[end] - sum_[start] >= s:
        answer = min(answer, end-start)
        start += 1
    else:
        if end < n:
            end += 1
        else:
            start += 1
if answer == sys.maxsize:
    print(0)
else:
    print(answer)