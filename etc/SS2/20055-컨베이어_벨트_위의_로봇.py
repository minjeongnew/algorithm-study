from collections import deque
n, k = map(int, input().split())
arr = deque(list(map(int, input().split())))


# 1번 -> 올리는 위치, N번 -> 내리는 위치
robots = deque([0]*n)
answer = 1
while True:
    x = arr.pop()
    arr.appendleft(x)
    x = robots.pop()
    robots.appendleft(x)

    robots[-1] = 0
    if sum(robots):
        for i in range(n-2, -1, -1):
            if robots[i] != 0 and robots[i+1] == 0 and arr[i+1] > 0:
                robots[i] = 0
                robots[i+1] = 1
                arr[i+1] -= 1
        robots[-1] = 0
    if arr[0] > 0 and robots[0] == 0:
        robots[0] = 1
        arr[0] -= 1
    duration = 0
    for x in arr:
        if x == 0:
            duration += 1
    if duration >= k:
        break
    answer += 1

print(answer)