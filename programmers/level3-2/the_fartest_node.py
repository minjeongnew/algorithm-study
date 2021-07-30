from collections import deque


def bfs(v, visited, graph):
    count = 0
    q = deque()
    q.append([v, count])
    while q:
        v, count = q.popleft()
        if visited[v] == -1:
            visited[v] = count
            count += 1
            for e in graph[v]:
                q.append([e, count])


def solution(n, vertex):
    answer = 0
    visited = [-1] * (n+1)
    graph = [[] for _ in range(n+1)]
    for v in vertex:
        x, y = v
        graph[x].append(y)
        graph[y].append(x)
    bfs(1, visited, graph)
    for v in visited:
        if v == max(visited):
            answer += 1
    return answer


if __name__ == '__main__':
    n = 6
    v = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

    print(solution(6, v))