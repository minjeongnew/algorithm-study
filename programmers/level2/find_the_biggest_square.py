def solution(board):
    answer = 0
    for row in board:
        if sum(row):
            answer = 1
            break
    else:
        return 0
    l1 = len(board)
    for i in range(1, l1):
        for j in range(1, l1):
            if board[i][j] and board[i-1][j] and board[i-1][j-1] and board[i][j-1]:
                board[i][j] = min(board[i-1][j], board[i-1][j-1], board[i][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer ** 2


if __name__ == '__main__':
    a = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
    print(solution(a))
    b = [[0,0], [0,0]]
    print(solution(b))
    c = [[1,0], [0,1]]
    print(solution(c))