answer = 0


def dfs(numbers, target, idx, value):
    global answer

    if idx == len(numbers) and value == target:
        answer += 1
        return
    if idx == len(numbers):
        return

    dfs(numbers, target, idx+1, value+numbers[idx])
    dfs(numbers, target, idx+1, value-numbers[idx])


def solution(numbers, target):
    global answer
    dfs(numbers, target, 0, 0)
    return answer