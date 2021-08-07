def solution(n, s, a, b, fares):
    MN = 100000 * (n+1)
    graph = [[MN]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        graph[i][i] = 0
    for i, j, v in fares:
        graph[i][j] = v
        graph[j][i] = v

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    # 탑승 안하는 경우
    answer = graph[s][a] + graph[s][b]
    for i in range(1, n+1):
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer