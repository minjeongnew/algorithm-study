from string import ascii_uppercase


def solution(msg):
    answer = []
    uc = list(ascii_uppercase)
    alphas = {alpha:idx+1 for idx, alpha in enumerate(uc)}
    i, j = 0, 0
    while True:
        j += 1
        if j == len(msg):
            answer.append(alphas[msg[i:j]])
            break
        if msg[i:j+1] not in alphas:
            alphas[msg[i:j+1]] = len(alphas) + 1
            answer.append(alphas[msg[i:j]])
            i = j
    return answer


if __name__ == "__main__":
    msg = "TOBEORNOTTOBEORTOBEORNOT"
    print(solution(msg))