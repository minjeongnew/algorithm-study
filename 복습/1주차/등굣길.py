def solution(m, n, puddles):
    # m: 열 n: 행
    graph = [[0]*(m+1) for _ in range(n+1)]
    graph[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                graph[i][j] = 0
            else:
                graph[i][j] = graph[i-1][j] + graph[i][j-1]
    print(graph)
    return graph[-1][-1]


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))