def solution(board):
    for r in board:
        if sum(r):
            answer = 1
            break
    else:
        return 0
    for i in range(1, len(board)):
        for j in range(1, len(board)):
            if board[i][j] and board[i-1][j] and board[i][j-1] and board[i-1][j-1]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1])
                answer = max(answer, board[i][j])
    return answer**2


if __name__ == '__main__':
    b = [[0,1,1,1],[1,1,1,1],[1,1,1,1],[0,0,1,0]]
    print(solution(b))