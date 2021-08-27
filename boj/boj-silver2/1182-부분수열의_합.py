import sys
# from itertools import combinations, 조합으로 풀지 말 것


n, s = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))
answer = 0


def solve(idx, sum_):
    global answer
    if idx == n:
        if sum_ == s:
            answer += 1
        return
    solve(idx+1, sum_+l[idx])
    solve(idx+1, sum_)
solve(0, 0)
if s == 0:
    answer -= 1
print(answer)