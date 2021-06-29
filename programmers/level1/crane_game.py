def solution(board, moves):
    answer = 0
    stack = []
    n = len(board)

    for i in moves:
        # 0 이 아닌 최초틔 숫자를 만났을 때
        # 그 숫자를 stack에 삽입하고
        # board 숫자는 0으로 치환
        for x in range(n):
            # 주어진 배열이 내가 생각하던 일반적인 2차원 배열의 행렬과 반대임
            if board[x][i-1] != 0:
                stack.append(board[x][i-1])
                board[x][i-1] = 0

                if len(stack) > 1: # 2 개 이상이면
                    # 맨 위의 두 숫자가 같으면 answer 증가시키고 없앤다
                    if stack[-1] == stack[-2]:
                        answer+=2
                        stack.pop()
                        stack.pop()
            break
    return answer
