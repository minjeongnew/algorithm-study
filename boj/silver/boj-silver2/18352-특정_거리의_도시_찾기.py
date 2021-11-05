import sys
from collections import deque


n, m, k, x = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
answer = [-1]*(n+1)
answer[x] = 0
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)


q = deque()
q.append(x)
while q:
    now = q.popleft()
    for nx in graph[now]:
        if answer[nx] == -1:
            answer[nx] = answer[now] + 1
            q.append(nx)
# print(answer)
for i in range(n+1):
    if answer[i] == k:
        print(i)
if k not in answer:
    print(-1)