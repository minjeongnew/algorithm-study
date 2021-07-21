def solution(files):
    answer = []
    for s in files:
        head = ''
        for x in s:
            if x.isdigit():
                break
            # 뒤의 조건 빼먹어서 계속 런타임 에러 났었음
            elif x.isalpha() or x in [' ', '-', '.']:
                head += x
        number = ''
        for n in s[len(head):len(head)+5]:
            if n.isalpha():
                break
            elif n.isdecimal():
                number += n
        answer.append([head, number, s])
    answer = sorted(answer, key= lambda x:[x[0], x[1]])
    return [x[2] for x in answer]


import re

# 정규식
def solution2(files):
    tmp = [re.split(r"([0-9]+)", s) for s in files]
    answer = sorted(tmp, key=lambda x:[x[0].lower(), int(x[1])])
    return [x[2] for x in answer]