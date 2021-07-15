from collections import deque


def solution(priorities, location):
    pl = deque([[idx, p] for idx, p in enumerate(priorities)])
    turn = 0
    while True:
        cur = pl.popleft()
        if any(cur[1] < x[1] for x in pl):
            pl.append(cur)
        else:
            turn += 1
            if location == cur[0]:
                return turn
