from collections import deque

def solution(prices):
    q = deque(prices)
    answer = []
    while q:
        p = q.popleft()
        sec = 0
        for x in q:
            sec += 1
            if p > x:
                break
        answer.append(sec)
    return answer