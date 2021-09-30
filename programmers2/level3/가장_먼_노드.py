from collections import deque


def solution(n, edge):
    d = dict() # 한 정점과 연결된 간선 리스트
    for a, b in edge:
        d[a] = d.get(a, []) + [b]
        d[b] = d.get(b, []) + [a]
    q = deque()
    q.append(1)
    v = [-1] * (n+1)
    v[1] = 1
    while q:
        x = q.popleft()
        for next in d[x]:
            if v[next] == -1:
                q.append(next)
                v[next] = v[x] + 1
    max_distance = max(v)
    answer = 0
    for node in v:
        if node == max_distance:
            answer += 1
    return answer


if __name__ == "__main__":
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(6, edge))