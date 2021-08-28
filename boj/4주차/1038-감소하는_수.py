# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
# 10, 20, 21, 30, 31, 32, 40, 41, 42, 43
# 210
# 310 320 321
# 410 420 421 430 431 432

# 10
# 1 2 3 4 5 6 7 8 9 -> 45
# n >= 2, n(n-1)/2

from collections import deque



q = deque([i for i in range(1, 10)])
def solve(n):
    if n == 0:
        print(0)
        return
    elif n > 1022:
        print(-1)
        return
    while q:
        # print(q)
        tmp = q.popleft()
        n -= 1
        if n == 0:
            print(tmp)
            break
        last = tmp % 10
        for i in range(last):
            q.append(tmp*10 + i)


n = int(input())
solve(n)