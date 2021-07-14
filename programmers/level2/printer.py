from collections import deque


def solution(priorities, location):
    p = deque([[idx, v] for idx, v in enumerate(priorities)])
    answer = 0
    while True:
        cur = p.popleft()
        if any(cur[1] < x[1] for x in p):
            p.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
