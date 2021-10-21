from collections import deque

n, k = map(int, input().split())
arr = deque(list(map(int, input().split())))
robots = deque([0 for _ in range(n)])
level = 1


while True:
    # rotate
    x = arr.pop()
    arr.appendleft(x) # arr.rotate(1)
    x = robots.pop()
    robots.appendleft(x) # robots.rotate(1)

    robots[-1] = 0 # 로봇 내려감
    if sum(robots):
        for i in range(n-2, -1, -1):
            if robots[i] != 0 and robots[i+1] == 0 and arr[i+1] > 0:
                arr[i+1] -= 1
                robots[i+1] = 1
                robots[i] = 0
        robots[-1] = 0

    if arr[0] > 0 and robots[0] == 0:
        robots[0] = 1
        arr[0] -= 1

    durations = 0
    for a in arr:
        if a == 0:
            durations += 1
    if durations >= k:
        break
    level += 1
print(level)
