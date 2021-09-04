import heapq
import sys

n = int(sys.stdin.readline())
hq = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0 and hq:
        print(heapq.heappop(hq))
    elif x == 0 and not hq:
        print(0)
    else:
        heapq.heappush(hq, x)