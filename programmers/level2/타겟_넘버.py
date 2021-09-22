answer = 0


def dfs(numbers, target, result, idx):
    global answer
    if idx == len(numbers):
        if result == target:
            answer += 1
        return
    dfs(numbers, target, result+numbers[idx], idx+1)
    dfs(numbers, target, result-numbers[idx], idx+1)


if __name__ == "__main__":
    numbers = [1, 1, 1, 1, 1]
    dfs(numbers, 3, 0, 0)
    print(answer)