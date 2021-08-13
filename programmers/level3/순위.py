def solution(n, results):
    answer = 0
    win = {x:set() for x in range(1, n+1)}
    lose = {x:set() for x in range(1, n+1)}

    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
    print(win)
    print(lose)
    for i in range(1, n+1):
        for loser in win[i]:
            lose[loser].update(lose[i])
        for winner in lose[i]:
            win[winner].update(win[i])
    print(win)
    print(lose)
    for i in range(1, n+1):
        if len(win[i]) + len(lose[i]) == n-1:
            answer += 1
    return answer


if __name__ == "__main__":
    n = 5
    r = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, r))