from collections import deque
n = int(input())
nums = deque([i for i in range(1, 10)])

def solve(n):
    if n - 1 == 0:
        print(0)
        return
    if n - 1 > 1022:
        print(-1)
        return
    while True:
        n -= 1
        tmp = nums.popleft()
        if n == 0:
            print(tmp)
            return
        last = tmp % 10
        for i in range(last):
            nums.append(tmp*10+i)

solve(n)