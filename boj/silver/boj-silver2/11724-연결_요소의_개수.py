import sys
from pprint import pprint
from collections import deque, defaultdict


n, m = map(int, sys.stdin.readline().split())
graph = [[0]*(n+1) for _ in range(n+1)]
vertices = {i+1:[] for i in range(n)}
visited = [0]*(n+1)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    vertices[u] = vertices.get(u, []) + [v]
    vertices[v] = vertices.get(v, []) + [u]
q = deque()
cnt = 0
for i in range(1, n+1):
    if visited[i] == 0:
        q.append(vertices[i])
        visited[i] = 1
        cnt += 1
        while q:
            current_nodes_list = q.popleft()
            for node in current_nodes_list:
                if visited[node] == 0:
                    q.append(vertices[node])
                    visited[node] = 1
print(cnt)