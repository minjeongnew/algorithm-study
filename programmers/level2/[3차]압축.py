from string import ascii_uppercase


def solution(msg):
    answer = []
    uc = ascii_uppercase
    w_dict = dict()
    for idx, x in enumerate(uc):
        w_dict[x] = idx + 1
    i, j = 0, 0
    while True:
        j += 1
        if j == len(msg):
            answer.append(w_dict[msg[i:j]])
            break
        if msg[i:j+1] not in w_dict:
            w_dict[msg[i:j+1]] = len(w_dict) + 1
            answer.append(w_dict[msg[i:j]])
            i = j
    return answer


if __name__ == '__main__':
    m = "TOBEORNOTTOBEORTOBEORNOT"
    print(solution(m))