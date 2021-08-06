def solution(m, n, puddles):
    # m: 열, n: 행
    # puddles에도 [열, 행] 요소들이 저장되어 있음
    v = [[0]*(m+1) for _ in range(n+1)]
    v[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j, i] != [1, 1]:
                if [j, i] in puddles:
                    v[i][j] = 0
                else:
                    v[i][j] = v[i-1][j] + v[i][j-1]
    return v[n][m]


if __name__ == '__main__':
    print(solution(4, 3, [[2, 2]]))