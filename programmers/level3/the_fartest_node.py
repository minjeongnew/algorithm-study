from collections import deque


def solution(n, edge):
    answer = 0
    ms = [[]*n for _ in range(n)]
    for e in edge:
        e1 = e[0]-1
        e2 = e[1]-1
        ms[e1].append(e2)
        ms[e2].append(e1)
    v = [-1] * n
    q = deque()
    q.append((0, 0))
    while q:
        idx, cnt = q.popleft()
        if v[idx] == -1:
            v[idx] = cnt
            cnt += 1
            for i in ms[idx]:
                q.append((i, cnt))

    m = max(v)
    for x in v:
        if x == m:
            answer += 1
    return answer


if __name__ == '__main__':
    n = 6
    edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
    print(solution(n, edge))