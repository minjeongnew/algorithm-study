from collections import Counter
from itertools import combinations


def solution(orders, course):
    answer = []
    for c in course:
        order_combinations = []
        for o in orders:
            combi = combinations(sorted(o), c)
            order_combinations += combi
        o_dict = Counter(order_combinations)
        if o_dict:
            max_ = max(list(o_dict.values()))
            if max_ >= 2:
                for key, value in o_dict.items():
                    if o_dict[key] >= max_:
                        answer.append(''.join(key))
    return sorted(answer)


if __name__ == '__main__':
    o = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
    c = [2,3,4]
    print(solution(o, c))