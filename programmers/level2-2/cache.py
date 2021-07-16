from collections import deque


def solution(cacheSize, cities):
    q = deque(maxlen=cacheSize)
    answer = 0
    for c in cities:
        c = c.lower()
        if c in q:
            q.remove(c)
            q.append(c)
            answer += 1
        else:
            q.append(c)
            answer += 5
    return answer