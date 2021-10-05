# bronze 2
import sys, math


n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
b, c = map(int, sys.stdin.readline().split())

cnt = 0
for x in s:
    cnt += 1
    x -= b
    if x > 0:
        cnt += math.ceil(x/c)
print(cnt)