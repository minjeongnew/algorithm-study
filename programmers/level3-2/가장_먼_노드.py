from collections import deque


def solution(n, vertex):
    graph = [[] for _ in range(n+1)]
    for x in vertex:
        a = x[0]
        b = x[1]
        graph[a].append(b)
        graph[b].append(a)
    v = [-1] * (n + 1)
    q = deque()
    q.append(1) # idx, count
    v[1] = 0
    while q:
        x = q.popleft()
        for nx in graph[x]:
            if v[nx] == -1:
                v[nx] = v[x] + 1
                q.append(nx)
    answer = 0
    for x in v:
        if x == max(v):
            answer += 1
    return answer