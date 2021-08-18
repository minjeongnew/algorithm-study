def cmp(s1, s2):
    flag = 0
    for x1, x2 in zip(s1, s2):
        if flag > 1:
            return False
        if x1 != x2:
            flag += 1
    return True


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    stack = [begin]
    v = [False] * len(words)
    while stack:
        current = stack.pop()
        if current == target:
            return answer
        for i in range(len(words)):
            if not v[i]:
                if cmp(current, words[i]):
                    stack.append(words[i])
                    v[i] = True
        answer += 1