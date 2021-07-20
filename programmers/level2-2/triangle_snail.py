def solution(n):
    tmp = [[0]*n for _ in range(n)]
    answer = []
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            tmp[x][y] = num
            num += 1
    for i in range(n):
        for j in range(n):
            if tmp[i][j] != 0:
                answer.append(tmp[i][j])
    return answer


if __name__ == '__main__':
    print(solution(6))