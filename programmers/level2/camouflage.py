def solution(clothes):
    answer = 1
    c ={}
    for x in clothes:
        if x[1] in c.keys():
            c[x[1]] += 1
        else:
            c[x[1]] = 1
    for i in c.values():
        answer *= (i+1)
    return answer