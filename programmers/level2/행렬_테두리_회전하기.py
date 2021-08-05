def turn(map_, x1, y1, x2, y2):
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    # 상단 가로
    tmp1 = map_[x1][y1:y2+1]
    # 오른쪽 세로
    tmp2 = [map_[x][y2] for x in range(x1, x2+1)]
    # 하단 가로
    tmp3 = map_[x2][y1:y2+1]
    # 왼쪽 세로
    tmp4 = [map_[x][y1] for x in range(x1, x2+1)]

    # 회전하기: 맵 변형하기
    # 상단 가로 ->
    for y in range(y1, y2):
        map_[x1][y+1] = tmp1[x1][y-y1]
    # 오른쪽 세로 (밑으로
    for x in range(x1, x2):
        map_[x+1][y2] = tmp2[x-x1]
    # 하단 가로 <-
    for y in range(y1, y2):
        map_[x2][y] = tmp3[y-y1+1]
    # 왼쪽 세로 (위로
    for x in range(x1, x2):
        map_[x][y1] = tmp4[x-x1+1]

    # tmp 1,2,3,4 중 가장 작은 값 리턴하기
    return min(tmp1+tmp2+tmp3+tmp4)


def solution(rows, columns, queries):
    m = [[j+columns*i for j in range(1,columns+1)] for i in range(rows)]
    answer = []
    for q in queries:
        x1, y1, x2, y2 = q
        answer.append(turn(m, x1, y1, x2, y2))
    return answer