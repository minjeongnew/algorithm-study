from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for c in course:
        combis = []
        for order in orders:
            if len(order) >= c:
                combis += list(''.join(sorted(x)) for x in combinations(order, c))
        counter = Counter(combis)
        if counter:
            max_count = max(counter.values())
            for x in counter:
                if counter[x] >= 2 and counter[x] == max_count:
                    answer.append(x)
    return sorted(answer)


if __name__ == "__main__":
    orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    course = [2,3,4]
    print(solution(orders, course))