import sys

l, c = map(int, sys.stdin.readline().split())
pw = sorted(list(map(str, sys.stdin.readline().split())))
vowel = ['a', 'e', 'i', 'o', 'u']


def check(s):
    v = 0
    c = 0
    for x in s:
        if x in vowel:
            v += 1
        else:
            c += 1
    return True if v >= 1 and c >= 2 else False


def solve(idx, answer):
    if len(answer) == l:
        if check(answer):
            print(answer)
        return
    elif idx == c:
        return
    solve(idx+1, answer + pw[idx])
    solve(idx+1, answer)


solve(0, '')