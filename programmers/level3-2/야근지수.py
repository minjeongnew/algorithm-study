import heapq


def solution(works, n):
    works2 = []
    for w in works:
        heapq.heappush(works2, -w)
    for _ in range(n):
        if works2:
            tmp = heapq.heappop(works2)
            if -tmp - 1 >= 0:
                heapq.heappush(works2, tmp+1)
        else:
            return 0
    return sum(x**2 for x in works2)


if __name__ == '__main__':
    w = [4, 3, 3]
    n = 4
    print(solution(w, n))
