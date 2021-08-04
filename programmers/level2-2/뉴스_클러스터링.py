from collections import Counter


def jaccard(x1, x2):
    c1 = Counter(x1)
    c2 = Counter(x2)
    inter = list((c1 & c2).elements())
    union = list((c1 | c2).elements())
    if len(union) == 0:
        return 65536
    print(inter)
    print(union)
    return int((len(inter)/len(union))*65536)


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    sl1 = []
    sl2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            sl1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            sl2.append(str2[i:i+2])
    return jaccard(sl1, sl2)


def solution2(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    sl1 = []
    sl2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            sl1.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            sl2.append(str2[i:i+2])
    union = len(sl1) + len(sl2)
    if len(sl1) > len(sl2):
        inter = [sl1.remove(x) for x in sl2 if x in sl1]
    else:
        inter = [sl2.remove(x) for x in sl1 if x in sl2]
    inter = len(inter)
    union -= inter
    if union == 0:
        return 65536
    return int((inter / union) * 65536)


if __name__ == '__main__':
    s1 = 'FRANCE'
    s2 = 'french'
    print(solution2(s1, s2))
    print(solution2('handshake', 'shake hands'))