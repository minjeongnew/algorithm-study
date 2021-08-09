def jaccard(x1, x2):
    if len(x1) == 0 or len(x2) == 0:
        return 65536
    inter = []
    union = len(x1) + len(x2)
    if len(x1) > len(x2):
        for x in x2:
            if x in x1:
                inter.append(x1.remove(x))
    else:
        for x in x1:
            if x in x2:
                inter.append(x2.remove(x))
    union -= len(inter)
    return int((len(inter)/union)*65536)


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    sl1 = []
    sl2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            sl1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            sl2.append(str2[i]+str2[i+1])
    return jaccard(sl1, sl2)


if __name__ == '__main__':
    s1, s2 = "FRANCE", "french"
    print(solution(s1, s2))
    s1, s2 = "aa1+aa2", "AAAA12"
    print(solution(s1, s2))