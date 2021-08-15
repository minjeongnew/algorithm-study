def match(current, word):
    cnt = 0
    for c, w in zip(current, word):
        if cnt > 1:
            return False
        if c != w:
            cnt += 1
    return True if cnt == 1 else False


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = 0
    v = [False] * len(words)
    stack = [begin]
    while stack:
        current = stack.pop()
        if current == target:
            return answer
        for i in range(len(words)):
            if not v[i]:
                if match(current, words[i]):
                    stack.append(words[i])
                    v[i] = True
        answer += 1


if __name__ == "__main__":
    b = "hit"
    t = "cog"
    w = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(solution(b, t, w))