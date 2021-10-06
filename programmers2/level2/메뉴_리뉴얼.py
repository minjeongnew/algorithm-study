from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        tmp = []
        for order in orders:
            combi = combinations(sorted(order), c)
            tmp += combi
        counter = Counter(tmp)
        # print(counter)
        if len(counter) != 0 and max(counter.values()) != 1:
            answer += [''.join(f) for f in counter if counter[f] == max(counter.values())]
    return sorted(answer)


if __name__ == "__main__":
    o = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    c = [2, 3, 4]
    print(solution(o, c))