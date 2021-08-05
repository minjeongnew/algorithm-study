def solution(m, n, puddles):
    # m: 열 n: 행
    # puddles 안의 요소들 또한 [열, 행]
    answer = [[0]*(m+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                answer[i][j] = 0
            else:
                answer[i][j] = answer[i-1][j] + answer[i][j-1]
    return answer[n][m]
