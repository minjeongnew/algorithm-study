# 플로이드-와샬 사용
def solution(N, road, K):
    answer = 0
    MN = 10001*(N+1)
    graph = [[MN]*(N+1) for _ in range(N+1)]
    for r in road:
        a, b, c = r
        graph[a][b] = min(graph[a][b], c)
        graph[b][a] = min(graph[b][a], c)

    for i in range(1, N+1):
        graph[i][i] = 0

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if i != j:
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])

    for i in range(1, N+1):
        if graph[1][i] <= K:
            answer += 1
    return answer


if __name__ == '__main__':
    ro = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    n = 6
    k = 4
    print(solution(n, ro, k))