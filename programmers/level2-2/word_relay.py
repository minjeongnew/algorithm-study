from collections import deque


def solution(n, words):
    stack = []
    l = len(words)
    words = deque(words)
    ans = []
    turn = 0
    for i in range(l):
        if i % n == 0:
            turn += 1
        cur = words.popleft()
        if stack:
            if cur not in stack and stack[-1][-1] == cur[0][0]:
                stack.append(cur)
            else:
                ans.append(l % n + 1)
                ans.append(turn)
                return ans
    return [0, 0]
