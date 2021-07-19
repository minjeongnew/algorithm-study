def solution(n):
    arr = [[0]*n for _ in range(n)]
    x, y = -1, 0
    num = 1
    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            else:
                x -= 1
                y -= 1
            arr[x][y] = num
            num += 1
    answer = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] != 0:
                answer.append(arr[i][j])
    return answer


if __name__ == '__main__':
    print(solution(6))