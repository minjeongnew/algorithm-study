import sys
import heapq


n = int(sys.stdin.readline())
c = []
for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    c.append([s, t])
c.sort(key=lambda x:x[0])
hq = []
heapq.heappush(hq, c[0][1]) # 끝나는 시각 넣음
for i in range(1, n):
    if hq[0] > c[i][0]:
        heapq.heappush(hq, c[i][1])
    else:
        heapq.heappop(hq)
        heapq.heappush(hq, c[i][1])
print(len(hq))