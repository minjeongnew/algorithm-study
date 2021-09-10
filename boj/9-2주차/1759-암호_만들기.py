import sys


vowel = ['a', 'e', 'i', 'o', 'u']
l, c = map(int, sys.stdin.readline().split())
ss = sorted(list(map(str, sys.stdin.readline().split())))


def check(s):
    ja = 0
    mo = 0
    for x in s:
        if x in vowel:
            mo += 1
        else:
            ja += 1
    if mo >= 1 and ja >= 2:
        return True
    return False


def solve(idx, answer):
    if len(answer) == l:
        if check(answer):
            print(answer)
        return
    if idx == c:
        return
    solve(idx+1, answer+ss[idx])
    solve(idx+1, answer)


solve(0, '')