import math


def solution(begin, end):
    answer = []
    # 블록의 전체 길이 -> 10 **9
    # 블록 숫자 범위 1 ~ 10**7
    # 즉, 블록 숫자가 10**7 이 넘어서는 안됨
    # 효율성 테스트에 주의할 것
    for i in range(begin, end+1):
        if i < 2:
            answer.append(0)
            continue
        for j in range(2, int(math.sqrt)+1):
            # 이 조건에 주의할 것
            if i // j > 10**7:
                continue
            if i % j == 0:
                answer.append(i//j)
                break
        else:
            answer.append(1)
    return answer