from collections import deque


def solution(N, road, K):
    MN = 500001
    graph = [[MN]*N for _ in range(N)]
    for r in road:
        a, b, c = r
        graph[a-1][b-1] = min(graph[a-1][b-1], c)
        graph[b-1][a-1] = min(graph[a-1][b-1], c)

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    graph[i][j] = 0
                else:
                    graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    answer = 0
    for x in graph[0]:
        if x <= K:
            answer += 1
    return answer


if __name__ == '__main__':
    N = 6
    road = [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]]
    K = 4
    print(solution(N, road, K))