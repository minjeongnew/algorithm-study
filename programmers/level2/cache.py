from collections import deque


def solution(cacheSize, cities):
    q = deque()
    answer = 0
    flag = 0
    for c in cities:
        c = c.lower()
        if flag < cacheSize:
            if c in q:
                answer += 1
                q.append(c)
                q.remove(c)
            else:
                flag += 1
                answer += 5
                q.append(c)
                q.remove(c)
        else:
            if c in q:
                answer += 1
                q.append(c)
                q.remove(c)
            else:
                answer += 5
                q.append(c)
                q.popleft()
    return answer


# deque의 maxlen
def solution2(cacheSize, cities):
    time = 0
    cache = deque(maxlen=cacheSize)
    for c in cities:
        c = c.lower()
        if c in cache:
            cache.remove(c)
            cache.append(c)
            time += 1
        else:
            cache.append(c)
            time += 5
    return time