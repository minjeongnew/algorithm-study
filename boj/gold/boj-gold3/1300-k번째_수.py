# 1 2 2 3 3 4 6 6 9


import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
start, end = 1, k
answer = -1
while start <= end:
    mid = (start+end)//2
    tmp = 0
    for i in range(1, n+1):
        tmp += min(mid//i, n) # mid 이하의 숫자 개수 찾기, n이 최대기 때문에 n보다는 클 수는 없다
    if tmp >= k:
        answer = mid
        end = mid -1
    else:
        start = mid + 1

print(answer)