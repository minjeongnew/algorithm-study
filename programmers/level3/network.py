from collections import deque


def solution(n, computers):
    answer = 0
    q = deque()
    v = [0]*n
    for i in range(n):
        if v[i] == 0:
            q.append(i)
            while q:
                x = q.popleft()
                v[x] = 1
                for nx in range(n):
                    if nx != x and v[nx] == 0 and computers[x][nx]:
                        q.append(nx)
            answer += 1
    return answer