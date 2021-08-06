import sys


def solution(n, s, a, b, fares):
    graph = [[sys.maxsize]*(n+1) for _ in range(n+1)]
    for i, j, v in fares:
        graph[i][j] = v
        graph[j][i] = v

    for i in range(1, n+1):
        graph[i][i] = 0

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    # 합승 안 한 경우
    answer = graph[s][a] + graph[s][b]
    for i in range(1, n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer


if __name__ == '__main__':
    n, s, a, b = 6, 4, 6, 2
    fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
    print(solution(n, s, a, b, fares))
    f2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]
    print(solution(7, 3, 4, 1, f2))