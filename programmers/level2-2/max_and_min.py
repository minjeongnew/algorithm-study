def solution(s):
    n = list(map(int, s.split()))
    n.sort()
    return str(n[0]) + ' ' + str(n[-1])