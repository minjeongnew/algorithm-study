def solution(n, results):
    win = {x:set() for x in range(1, n+1)}
    lose = {x:set() for x in range(1, n+1)}
    for winner, loser in results:
        win[winner].add(loser)
        lose[loser].add(winner)
    print(win)
    print(lose)
    
    answer = 0
    return answer



if __name__ == "__main__":
    n = 5
    r = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
    print(solution(n, r))