import heapq


def solution(works, n):
    works2 = []
    for w in works:
        heapq.heappush(works2, -w)
    for i in range(n):
        if works2:
            tmp = heapq.heappop(works2)
            if -tmp - 1 >= 0:
                heapq.heappush(works2, tmp+1)
        else:
            return 0
    return sum(w**2 for w in works2) if works2 else 0