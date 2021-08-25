def star(a, x):
    result = []
    i = 0
    while True:
        if (a[i] != a[i+1]) and (a[i] == x or a[i+1] == x):
            result.append(a[i])
            result.append(a[i+1])
            i += 2
        else:
            i += 1
        if i > len(a) - 2:
            break
    return len(result)


def solution(a):
    answer = 0
    tmp = [0]*len(a)
    if len(a) < 2:
        return 0
    for x in a:
        tmp [x] += 1
    for i in range(len(tmp)):
        if tmp[i] * 2 <= answer:
            continue
        answer = max(star(a, i), answer)
    return answer