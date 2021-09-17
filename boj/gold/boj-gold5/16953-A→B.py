import sys
from collections import deque

a, b = map(int, sys.stdin.readline().split())
q = deque()
q.append((a, 1))
answer = 0
while q:
    x, cnt = q.popleft()
    if x == b:
        answer = cnt
    for i in range(2):
        if i == 1:
            nx = x*2
        else:
            nx = int(str(x)+'1')
        if a < nx <= b:
            n_cnt = cnt + 1
            q.append((nx, n_cnt))
print(answer if answer else -1)