from pprint import pprint


def turn(map_, x1, y1, x2, y2):
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    tmp = map_[x1][y1]
    min_n = tmp
    # 왼쪽 세로
    for x in range(x1, x2):
        value = map_[x+1][y1]
        map_[x][y1] = value
        min_n = min(min_n, value)
    # 하단 가로
    for y in range(y1, y2):
        value = map_[x2][y+1]
        map_[x2][y] = value
        min_n = min(min_n, value)
    # 오른쪽 세로
    for x in range(x2, x1, -1):
        value = map_[x-1][y2]
        map_[x][y2] = value
        min_n = min(min_n, value)
    # 상단 가로
    for y in range(y2, y1, -1):
        value = map_[x1][y-1]
        map_[x1][y] = value
        min_n = min(min_n, value)
    map_[x1][y1+1] = tmp
    return min_n


def solution(rows, columns, queries):
    m = [[j+i*columns for j in range(1, columns+1)] for i in range(rows)]
    answer = []
    for q in queries:
        x1, y1, x2, y2 = q
        answer.append(turn(m, x1, y1, x2, y2))
        pprint(m)
    return answer


if __name__ == '__main__':
    r,c = 6, 6
    queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
    print(solution(r,c,queries))