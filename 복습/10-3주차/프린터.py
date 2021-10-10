from collections import deque

def solution(priorities, location):
    cnt = 1
    printer = deque([(idx, priority) for idx, priority in enumerate(priorities)])
    while True:
        idx, priority = printer.popleft()
        if any(priority < x[1] for x in printer):
            printer.append((idx, priority))
        else:
            if idx == location:
                return cnt
            else:
                cnt += 1