import sys
from collections import deque
n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())

m = int(sys.stdin.readline())

board = [[] for _ in range(n+1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().split())
    board[x].append(y)
    board[y].append(x)


v = [0]*(n+1)
def bfs(node, target):
    q = deque()
    q.append([node, 0])
    while q:
        node, cnt = q.popleft()
        if node == target:
            return cnt
        for x in board[node]:
            if v[x] == 0:
                v[x] = v[node] + 1
                q.append([x, cnt+1])
    return -1

print(bfs(a, b))
