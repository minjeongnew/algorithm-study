from collections import Counter


def jaccard(x1, x2):
    if not x1 and not x2:
        return 65536
    c1 = Counter(x1)
    c2 = Counter(x2)
    inter = c1 & c2
    union = c1 | c2
    l1 = len(list(inter.elements()))
    l2 = len(list(union.elements()))
    return int((l1/l2)*65536)


def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    s1 = []
    s2 = []
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s2.append(str2[i]+str2[i+1])
    answer = jaccard(s1, s2)
    return answer


def solution2(str1, str2):
    s1 = []
    s2 = []
    str1 = str1.lower()
    str2 = str2.lower()
    for i in range(len(str1)-1):
        if str1[i].isalpha() and str1[i+1].isalpha():
            s1.append(str1[i]+str1[i+1])
    for i in range(len(str2)-1):
        if str2[i].isalpha() and str2[i+1].isalpha():
            s2.append(str2[i]+str2[i+1])
    if len(s1) > len(s2):
        inter = [s1.remove(x) for x in s2 if x in s1]
    else:
        inter = [s2.remove(x) for x in s1 if x in s2]
    union = s1 + s2
    if not union:
        return 65536
    return int((len(inter)/len(union)) * 65536)


if __name__ == '__main__':
    s1, s2 = "FRANCE", "french"
    print(solution(s1, s2))
    s1, s2 = "aa1+aa2", "AAAA12"
    print(solution2(s1, s2))