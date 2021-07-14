from collections import deque


def solution(n, words):
    l = len(words)
    turn = 1
    words = deque(words)
    stack = [words.popleft()]
    answer = []
    for i in range(1, l):
        if i % n == 0:
            turn += 1
        if stack:
            if words[0] not in stack and stack[-1][-1] == words[0][0]:
                stack.append(words.popleft())
            else:
                answer.append(i % n + 1)
                answer.append(turn)
                return answer
    return [0, 0]


if __name__ == '__main__':
    n1 = 3
    w1= ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
    print(solution(n1, w1))
    n2 = 5
    w2 = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]
    print(solution(n2, w2))