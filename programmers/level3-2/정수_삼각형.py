def solution(triangle):
    lt = len(triangle)
    for i in range(lt):
        tmp = [0] + triangle[i] + [0]*(lt-i-1)
        triangle[i] = tmp
    for i in range(1, lt):
        for j in range(1, lt):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])


if __name__ == '__main__':
    t = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
    print(solution(t))
