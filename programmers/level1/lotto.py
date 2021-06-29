from collections import Counter


def solution(lottos, win_nums):
    lottos.sort() # 정렬
    win_nums.sort() # 정렬
    answer = []

    lottos_cnt = Counter(lottos) - Counter(win_nums)

    zero_cnt = lottos_cnt[0] # 0 개수
    corr = [] # 맞은 개수
    for i in win_nums:
        for j in lottos:
            if i ==j:
                corr.append(j) # k
                break
    # total = 일치 + 순위 + zero_cnt = 7

    # 7일 경우 -> 6등
    if 7-len(corr)-zero_cnt == 7:
        answer.append(6)
    else:
        answer.append(7-len(corr)-zero_cnt)
    # 7일 경우 -> 6등
    if 7-len(corr) == 7:
        worst= 6
    else:
        worst = 7-len(corr)
    answer.append(worst)
    return answer


# 다른 풀이
def solution2(lottos, win_nums):
    ranks = [6,6,5,4,3,2,1]

    zero_cnt = lottos.count(0)
    answer = 0
    for i in win_nums:
        for j in lottos:
            if i==j:
                answer+=1
    return ranks[zero_cnt+answer], ranks[answer]


if __name__ == '__main__':
    l = [44, 1, 0, 0, 31, 25]
    w = [31, 10, 45, 1, 6, 19]

    l2 = [0, 0, 0, 0, 0, 0]
    w2 = [38, 19, 20, 40, 15, 25]

    print(solution2(l2, w2))