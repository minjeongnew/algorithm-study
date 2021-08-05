def solution(triangle):
    lt = len(triangle)
    for i in range(lt):
        tmp = [0] + triangle[i] + [0]*(lt-i-1)
        triangle[i] = tmp

    idx = 1
    for i in range(1, lt):
        idx += 1
        for j in range(1, idx+1):
            triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])
    return max(triangle[-1])