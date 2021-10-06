from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        p = q.popleft()
        sec = 0
        for x in p:
            sec += 1
            if x < p:
                break
        answer.append(sec)
    return answer