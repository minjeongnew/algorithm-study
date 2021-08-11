from string import ascii_uppercase


def solution(msg):
    answer = []
    uc = ascii_uppercase
    a_dict = {key: idx+1 for idx, key in enumerate(uc)}
    i, j = 0, 0
    while True:
        j += 1
        if j == len(msg):
            answer.append(a_dict[msg[i:j]])
            break
        if msg[i:j+1] not in a_dict:
            a_dict[msg[i:j+1]] = len(a_dict) + 1
            answer.append(a_dict[msg[i:j]])
            i = j
    return answer


if __name__ == '__main__':
    m = "TOBEORNOTTOBEORTOBEORNOT"
    print(solution(m))