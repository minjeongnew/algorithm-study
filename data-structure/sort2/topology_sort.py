import sys
from collections import deque


def topology_sort(v, indegrees, graph):
    result = []
    q = deque()
    for i in range(1, v+1):
        if indegrees[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegrees[i] -= 1
            if indegrees[i] == 0:
                q.append(i)
    return result


if __name__ == "__main__":
    v, e = map(int, sys.stdin.readline().split())
    indegrees = [0] * (v+1)
    graph = [[] for _ in range(v+1)]
    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        graph[a] = b
        indegrees[b] += 1
    result = topology_sort(v, indegrees, graph)
    print(result)