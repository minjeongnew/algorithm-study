answer = 0


def dfs(numbers, target, idx, s):
    global answer
    if idx == len(numbers):
        if s == target:
            answer += 1
        return

    dfs(numbers, target, idx+1, s+numbers[idx])
    dfs(numbers, target, idx+1, s-numbers[idx])


def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer