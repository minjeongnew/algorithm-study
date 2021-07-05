answer = 0
def dfs(numbers, target, result, idx):
    global answer
    if len(numbers)==idx and target == answer:
        answer += 1
        return
    if len(numbers) ==idx:
        return
    dfs(numbers, target, result+numbers[idx], idx+1)
    dfs(numbers, target, result-numbers[idx], idx+1)


def solution(numbers, target):
    global answer
    dfs(numbers, target)
    return answer
