from collections import deque


def solution(n, computers):
    answer = 0
    visited = [-1]*(n)
    q = deque()
    for i in range(n):
        if visited[i] == -1:
            q.append(i)
            while q:
                x = q.popleft()
                visited[x] = 1
                for nx in range(n):
                    if x != nx and computers[x][nx] == 1:
                        if visited[nx] == -1:
                            q.append(nx)
            answer += 1
    return answer


if __name__ == '__main__':
    n = 3
    c = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    print(solution(n, c))