import sys


def solve(a, idx, answer):
    if idx == len(a):
        if len(answer) == 6:
            print(*answer)
        return
    if len(answer) == 6:
        print(*answer)
        return
    solve(a, idx+1, answer + [a[idx]])
    solve(a, idx+1, answer)
while True:
    k, *a = map(int, sys.stdin.readline().split())
    if k == 0:
        break
    solve(a, 0, [])
    print()