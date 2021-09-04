n = int(input())
from collections import deque

q = deque([i for i in range(1, 10)])


def solve(n):
    if n-1 == 0:
        print(0)
        return
    if n-1 > 1022:
        print(-1)
        return
    n-=1
    while q:
        # print(q)
        tmp = q.popleft()
        n -= 1
        if n == 0:
            print(tmp)
            return
        last = tmp % 10
        for i in range(last):
            q.append(tmp*10 + i)


solve(n)