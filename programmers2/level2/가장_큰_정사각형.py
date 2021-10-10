def solution(board):
    n, m = len(board), len(board[0])
    answer = 0
    dp = [[0]*m for _ in range(n)]
    dp[0] = board[0]
    for i in range(n):
        dp[i][0] = board[i][0]
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

    for x in dp:
        tmp = max(x)
        answer = max(answer, tmp)
    return answer**2
