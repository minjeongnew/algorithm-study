import heapq as hq


def lcm(x, y):
    m = max(x, y)
    for i in range(m, x*y+1):
        if i%x == 0 and i%y == 0:
            return i


def solution(arr):
    hq.heapify(arr)
    while arr:
        if len(arr) == 1:
            return arr[0]
        x = hq.heappop(arr)
        y = hq.heappop(arr)
        hq.heappush(arr, lcm(x, y))


