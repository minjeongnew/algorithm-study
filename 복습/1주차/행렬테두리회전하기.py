def move(x1, y1, x2, y2):
    global graph
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    tmp = graph[x1][y1]
    answer = tmp
    # 왼쪽 세로
    for x in range(x1, x2):
        value = graph[x+1][y1]
        graph[x][y1] = value
        answer = min(answer, value)
    # 하단 가로
    for y in range(y1, y2):
        value = graph[x2][y+1]
        graph[x2][y] = value
        answer = min(answer, value)
    # 오른쪽 세로
    for x in range(x2, x1, -1):
        value = graph[x-1][y2]
        graph[x][y2] = value
        answer = min(answer, value)
    # 상단 가로
    for y in range(y2, y1, -1):
        value = graph[x1][y-1]
        graph[x1][y] = value
        answer = min(answer, value)
    graph[x1][y1+1] = tmp
    # 움직인 수들 중 가장 작은 수 리턴
    return answer

def solution(rows, columns, queries):
    global graph
    graph = [[j + (columns*i) for j in range(1, columns+1)] for i in range(rows)]
    answer = []
    for query in queries:
        x1, y1, x2, y2 = query
        answer.append(move(x1, y1, x2, y2))
    return answer


if __name__ == '__main__':
    r,c = 6, 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    print(solution(r,c,queries))
    r, c, q = 3, 3, [[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]
    print(solution(r,c,q))