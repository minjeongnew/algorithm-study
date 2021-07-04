import string


def solution(s, n):
    answer = ''
    lc = list(string.ascii_lowercase)
    uc = list(string.ascii_uppercase)

    for x in s:
        if x in lc:
            idx = lc.index(x)
            answer += lc[(idx+n)%26]
        elif x in uc:
            idx = uc.index(x)
            answer += uc[(idx+n)%26]
        else:
            answer += ' '

    return answer